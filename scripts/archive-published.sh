#!/bin/bash
# ============================================================
# FL3 Dashboard — Archive Published Content
# Reads dashboard-data.json to find content items marked as
# published (steps.publish = true), then moves the actual .md
# files from their original folder into Weekly-Content/Archive/
# with the publish date appended to the filename.
#
# This script is idempotent: running it multiple times is safe.
# It skips files that are already in Archive/ or don't exist
# at the original location.
#
# Usage: ./archive-published.sh
# Requires: python3, git
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$SCRIPT_DIR/.."
JSON_FILE="$REPO_ROOT/docs/dashboard-data.json"
JS_FILE="$REPO_ROOT/docs/dashboard-data.js"
WEEKLY_DIR="$REPO_ROOT/Weekly-Content"
ARCHIVE_DIR="$WEEKLY_DIR/Archive"

if [ ! -f "$JSON_FILE" ]; then
  echo "Error: dashboard-data.json not found at $JSON_FILE"
  exit 1
fi

# Ensure Archive directory exists
mkdir -p "$ARCHIVE_DIR"

echo "Scanning for published content to archive..."

# ── Find and move published files ──
RESULT=$(REPO_ROOT="$REPO_ROOT" WEEKLY_DIR="$WEEKLY_DIR" ARCHIVE_DIR="$ARCHIVE_DIR" python3 << 'PYEOF'
import json, os, shutil, re

REPO_ROOT = os.environ["REPO_ROOT"]
WEEKLY_DIR = os.environ["WEEKLY_DIR"]
ARCHIVE_DIR = os.environ["ARCHIVE_DIR"]
JSON_FILE = os.path.join(REPO_ROOT, "docs", "dashboard-data.json")

# Vault prefix for path matching
VAULT_PREFIX = "00-ZenithPro - FL3/Systems/Business-Suite/Weekly-Content/"

# Map dashboard folder keys to disk folder names
FOLDER_DISK = {
    "youtube": "YouTube",
    "articles": "Articles",
    "social-media": "Social Media",
    "email": "Email",
}

with open(JSON_FILE, "r") as f:
    data = json.load(f)

wc = data.get("projects", {}).get("weekly-content", {})
folders = wc.get("contentFolders", {})

moved_count = 0

for folder_key, folder_data in folders.items():
    # Skip briefs and archive folders
    if folder_key in ("briefs", "archive"):
        continue

    disk_name = FOLDER_DISK.get(folder_key)
    if not disk_name:
        continue

    items = folder_data.get("items", [])

    for item in items:
        steps = item.get("steps", {})

        # Only process items marked as published
        if not steps.get("publish"):
            continue

        # Check if already archived (path points to Archive/)
        current_path = item.get("path", "")
        if "/Archive/" in current_path:
            # Already archived in data, check if file needs moving
            original_path = item.get("originalPath", "")
            if original_path:
                # Try to find the file at the original location
                original_rel = original_path.replace(VAULT_PREFIX, "")
                original_disk = os.path.join(WEEKLY_DIR, original_rel)

                if os.path.isfile(original_disk):
                    # Derive archive filename from the path field
                    archive_rel = current_path.replace(VAULT_PREFIX + "Archive/", "")
                    archive_disk = os.path.join(ARCHIVE_DIR, archive_rel)

                    # Handle potential filename collision
                    if os.path.exists(archive_disk):
                        base, ext = os.path.splitext(archive_disk)
                        counter = 2
                        while os.path.exists(archive_disk):
                            archive_disk = f"{base} ({counter}){ext}"
                            counter += 1

                    shutil.move(original_disk, archive_disk)
                    print(f"  Archived: {os.path.basename(original_disk)} -> Archive/{os.path.basename(archive_disk)}")
                    moved_count += 1
            continue

        # Published but path not yet pointing to Archive
        # This handles items published before the dashboard was updated
        # (e.g., items with steps.publish=true but no originalPath/publishedDate)
        original_rel = current_path.replace(VAULT_PREFIX, "")
        original_disk = os.path.join(WEEKLY_DIR, original_rel)

        if not os.path.isfile(original_disk):
            continue

        # Generate publish date
        pub_date = item.get("publishedDate", "")
        if not pub_date:
            from datetime import date
            pub_date = str(date.today())
            item["publishedDate"] = pub_date

        # Sanitize title for filename
        title = item.get("title", "Untitled")
        safe_title = re.sub(r'[/\\:*?"<>|]', '', title).strip()

        archive_filename = f"{safe_title} PUB ({pub_date}).md"
        archive_disk = os.path.join(ARCHIVE_DIR, archive_filename)

        # Handle collision
        if os.path.exists(archive_disk):
            base, ext = os.path.splitext(archive_disk)
            counter = 2
            while os.path.exists(archive_disk):
                archive_disk = f"{base} ({counter}){ext}"
                counter += 1

        # Update data model
        item["originalPath"] = current_path
        item["path"] = VAULT_PREFIX + "Archive/" + os.path.basename(archive_disk)

        # Move the file
        shutil.move(original_disk, archive_disk)
        print(f"  Archived: {os.path.basename(original_disk)} -> Archive/{os.path.basename(archive_disk)}")
        moved_count += 1

# Save updated data
with open(JSON_FILE, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")

print(f"\n{moved_count} file(s) archived.")
PYEOF
)

echo "$RESULT"

# Check if anything was moved
if echo "$RESULT" | grep -q "0 file(s) archived"; then
  echo "Nothing to archive."
  exit 0
fi

# ── Regenerate dashboard-data.js ──
echo "Regenerating dashboard-data.js..."

python3 -c "
import json

with open('$JSON_FILE', 'r') as f:
    data = json.load(f)

js = '// Auto-generated by archive-published.sh. Do not edit manually.\n'
js += 'window.FL3_DASHBOARD_DATA = ' + json.dumps(data, indent=2) + ';\n'

with open('$JS_FILE', 'w') as f:
    f.write(js)

print('Regenerated dashboard-data.js')
"

# ── Git commit and push ──
echo "Committing and pushing..."
cd "$REPO_ROOT"
git add Weekly-Content/ docs/dashboard-data.json docs/dashboard-data.js
git commit -m "Archive published content"
git push

echo ""
echo "Done. Published content archived."
echo "Live at: https://jscott-62.github.io/fl3-dashboard/"
