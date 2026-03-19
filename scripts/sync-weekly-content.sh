#!/bin/bash
# ============================================================
# FL3 Dashboard — Weekly Content Sync
# Scans the Weekly-Content subfolders in the Obsidian vault,
# detects new .md files not yet tracked in dashboard-data.json,
# and adds them to the appropriate content folder section.
#
# Content is organized by WEEK folders (not by type):
#   Weekly-Content/Week of Mar 3/   <- all types for that week
#   Weekly-Content/Week of Mar 10/
#   Weekly-Content/Unscheduled/     <- content not yet assigned to a week
#
# Type detection uses **Type:** tag in file or filename inference.
# Skips: Archive/, Briefs/, non-.md files
#
# Usage: ./sync-weekly-content.sh
# Requires: python3, git
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$SCRIPT_DIR/.."
JSON_FILE="$REPO_ROOT/docs/dashboard-data.json"
JS_FILE="$REPO_ROOT/docs/dashboard-data.js"
WEEKLY_DIR="$REPO_ROOT/Weekly-Content"

if [ ! -d "$WEEKLY_DIR" ]; then
  echo "Error: Weekly-Content folder not found at $WEEKLY_DIR"
  exit 1
fi

if [ ! -f "$JSON_FILE" ]; then
  echo "Error: dashboard-data.json not found at $JSON_FILE"
  exit 1
fi

echo "Scanning Weekly-Content folders for new files..."

# ── Scan folders and update dashboard-data.json ──
ADDED=$(WEEKLY_DIR="$WEEKLY_DIR" JSON_FILE="$JSON_FILE" python3 << 'PYEOF'
import json, os, re

WEEKLY_DIR = os.environ["WEEKLY_DIR"]
JSON_FILE = os.environ["JSON_FILE"]

# Vault-relative path prefix
VAULT_PREFIX = "00-ZenithPro - FL3/Projects/fl3-dashboard/Weekly-Content/"

# Steps per content type
STEPS = {
    "youtube":      ["research", "write", "film", "edit", "publish"],
    "social-media": ["research", "write", "film", "edit", "publish"],
    "articles":     ["research", "write", "edit", "publish"],
    "email":        ["research", "write", "edit", "publish"],
}

# Folders to skip
SKIP_FOLDERS = {"Archive", "Briefs", ".git"}

def detect_type(filepath, filename):
    """Detect content type from file metadata or filename."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # Read first 20 lines looking for Type tag
            for i, line in enumerate(f):
                if i > 20:
                    break
                line = line.strip()
                # Check for **Type:** tag
                m = re.match(r'\*\*Type:\*\*\s*(.+)', line, re.IGNORECASE)
                if m:
                    t = m.group(1).strip().lower()
                    if "youtube" in t:
                        return "youtube"
                    elif "social" in t:
                        return "social-media"
                    elif "email" in t or "newsletter" in t:
                        return "email"
                    elif "article" in t:
                        return "articles"
    except Exception:
        pass

    # Fallback: infer from filename
    fn = filename.lower()
    if "youtube" in fn or "script" in fn:
        return "youtube"
    elif "social" in fn or "batch" in fn:
        return "social-media"
    elif "newsletter" in fn or "email" in fn:
        return "email"
    elif "pillar" in fn and ("vid" in fn or "estimated length" in open(filepath, "r", encoding="utf-8").read(500).lower()):
        return "youtube"
    else:
        return "articles"

with open(JSON_FILE, "r") as f:
    data = json.load(f)

wc = data["projects"]["weekly-content"]
folders = wc.setdefault("contentFolders", {})

# Collect ALL existing paths across all categories for dedup
existing_paths = set()
for folder_key, folder_data in folders.items():
    for item in folder_data.get("items", []):
        if item.get("path"):
            existing_paths.add(item["path"])

added_count = 0

# Walk all week folders and Unscheduled
for entry in sorted(os.listdir(WEEKLY_DIR)):
    entry_path = os.path.join(WEEKLY_DIR, entry)
    if not os.path.isdir(entry_path):
        continue
    if entry in SKIP_FOLDERS:
        continue

    # Determine weekOf from folder name (e.g., "Week of Mar 3" -> find matching calendar entry)
    week_folder = entry  # e.g., "Week of Mar 10" or "Unscheduled"

    # Scan .md files in this folder (and immediate subfolders)
    for root, dirs, files in os.walk(entry_path):
        # Skip nested Archive/Briefs
        dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS]

        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue

            full_path = os.path.join(root, fname)
            # Build vault-relative path
            rel_from_wc = os.path.relpath(full_path, WEEKLY_DIR)
            vault_path = VAULT_PREFIX + rel_from_wc

            if vault_path in existing_paths:
                continue

            # Detect content type
            content_type = detect_type(full_path, fname)

            # Ensure category exists
            if content_type not in folders:
                label_map = {
                    "youtube": "YouTube",
                    "articles": "Articles",
                    "social-media": "Social Media",
                    "email": "Email",
                }
                folders[content_type] = {"label": label_map.get(content_type, content_type), "items": []}

            # Extract title from first # heading
            title = fname[:-3]  # fallback
            try:
                with open(full_path, "r", encoding="utf-8") as mdf:
                    for line in mdf:
                        line = line.strip()
                        if line.startswith("# ") and not line.startswith("## "):
                            title = line[2:].strip()
                            break
            except Exception:
                pass

            # Build step dict (research + write = true since file exists)
            step_keys = STEPS.get(content_type, ["research", "write", "edit", "publish"])
            steps = {k: (k in ("research", "write")) for k in step_keys}

            item = {
                "title": title,
                "steps": steps,
                "path": vault_path,
            }

            # Try to match weekOf from calendar
            if week_folder != "Unscheduled":
                calendar = wc.get("calendar", [])
                for cal in calendar:
                    if cal.get("weekLabel") == week_folder:
                        item["weekOf"] = cal["weekOf"]
                        break

            folders[content_type]["items"].append(item)
            existing_paths.add(vault_path)

            print(f"  + [{content_type}] {title} ({week_folder})")
            added_count += 1

# Update timestamp
from datetime import date
data["lastUpdated"] = str(date.today())

with open(JSON_FILE, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")

print(f"\n{added_count} new item(s) added.")
PYEOF
)

echo "$ADDED"

# Check if anything was added
if echo "$ADDED" | grep -q "0 new item(s) added"; then
  echo "Nothing new to sync."
  exit 0
fi

# ── Regenerate dashboard-data.js ──
echo "Regenerating dashboard-data.js..."

python3 -c "
import json

with open('$JSON_FILE', 'r') as f:
    data = json.load(f)

js = '// Auto-generated by sync-weekly-content.sh. Do not edit manually.\n'
js += 'window.FL3_DASHBOARD_DATA = ' + json.dumps(data, indent=2) + ';\n'

with open('$JS_FILE', 'w') as f:
    f.write(js)

print('Regenerated dashboard-data.js')
"

# ── Git commit and push ──
echo "Pushing to GitHub..."
cd "$REPO_ROOT"
git add docs/dashboard-data.json docs/dashboard-data.js
git commit -m "Sync weekly content: add new files from vault"
git push

echo ""
echo "Done. Dashboard synced."
echo "Live at: https://jscott-62.github.io/fl3-dashboard/"
