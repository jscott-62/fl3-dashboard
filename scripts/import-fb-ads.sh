#!/bin/bash
# ============================================================
# FL3 Dashboard — Facebook Ads CSV Importer
#
# Reads a CSV export from Facebook Ads Manager, maps campaigns
# to dashboard projects, updates dashboard-data.json, regenerates
# dashboard-data.js, and pushes to GitHub.
#
# Usage:
#   ./import-fb-ads.sh                          # auto-finds CSV in drop folder
#   ./import-fb-ads.sh /path/to/export.csv      # explicit file
#
# Facebook Ads Manager export steps:
#   1. Go to Ads Manager → Campaigns tab
#   2. Select date range (this week's spend)
#   3. Click "Reports" → "Export Table Data"
#   4. Choose CSV format
#   5. Drop the file into: scripts/fb-csv-drop/
#   6. Run this script
#
# Requires: python3, git
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$SCRIPT_DIR/.."
JSON_FILE="$REPO_ROOT/docs/dashboard-data.json"
JS_FILE="$REPO_ROOT/docs/dashboard-data.js"
DROP_DIR="$SCRIPT_DIR/fb-csv-drop"
MAP_FILE="$SCRIPT_DIR/fb-campaign-map.json"

# ── Find CSV ──
if [ -n "$1" ]; then
  CSV_FILE="$1"
else
  # Auto-find the newest CSV in the drop folder
  if [ ! -d "$DROP_DIR" ]; then
    echo "Error: Drop folder not found at $DROP_DIR"
    echo "Create it or pass a CSV path as an argument."
    exit 1
  fi
  CSV_FILE=$(ls -t "$DROP_DIR"/*.csv 2>/dev/null | head -1)
  if [ -z "$CSV_FILE" ]; then
    echo "No CSV files found in $DROP_DIR"
    echo ""
    echo "Export from Facebook Ads Manager:"
    echo "  1. Go to Ads Manager → Campaigns tab"
    echo "  2. Select your date range"
    echo "  3. Click Reports → Export Table Data → CSV"
    echo "  4. Drop the file into: $DROP_DIR/"
    echo "  5. Run this script again"
    exit 1
  fi
fi

if [ ! -f "$CSV_FILE" ]; then
  echo "Error: File not found: $CSV_FILE"
  exit 1
fi

echo "Importing Facebook Ads data from: $(basename "$CSV_FILE")"
echo ""

# ── Check campaign map exists ──
if [ ! -f "$MAP_FILE" ]; then
  echo "Error: Campaign map not found at $MAP_FILE"
  echo "This file maps Facebook campaign names to dashboard project keys."
  echo "Create it — see fb-campaign-map.json.example for the format."
  exit 1
fi

# ── Parse CSV and update dashboard ──
export JSON_FILE CSV_FILE JS_FILE MAP_FILE
python3 << 'PYTHON_SCRIPT'
import csv
import json
import sys
import os
from pathlib import Path

JSON_FILE = os.environ["JSON_FILE"]
JS_FILE = os.environ["JS_FILE"]
CSV_FILE = os.environ["CSV_FILE"]
MAP_FILE = os.environ["MAP_FILE"]

# ── Load campaign map ──
with open(MAP_FILE, "r") as f:
    campaign_map = json.load(f)

# campaign_map format:
# {
#   "campaign-name-substring": "dashboard-project-key",
#   "WAM": "wrong-asset-manifesto",
#   "Great Catch": "the-great-catch-up"
# }

# ── Parse Facebook CSV ──
# Facebook Ads Manager CSVs have varying column names. We handle common variations.
COLUMN_ALIASES = {
    "campaign_name": ["campaign name", "campaign_name", "campaign"],
    "amount_spent": ["amount spent", "amount_spent", "amount spent (usd)", "spend", "cost"],
    "results": ["results", "leads", "conversions", "actions"],
    "ctr": ["ctr (link click-through rate)", "ctr (all)", "ctr", "link ctr"],
}

def find_column(headers, aliases):
    """Find the actual column name from a list of possible aliases."""
    lower_headers = [h.lower().strip() for h in headers]
    for alias in aliases:
        if alias.lower() in lower_headers:
            return headers[lower_headers.index(alias.lower())]
    return None

# Read CSV
rows = []
with open(CSV_FILE, "r", encoding="utf-8-sig") as f:
    # Skip any blank lines or reporting metadata at the top
    lines = f.readlines()

# Find the header row (first row with "Campaign" in it)
header_idx = 0
for i, line in enumerate(lines):
    if "campaign" in line.lower() and ("spent" in line.lower() or "spend" in line.lower() or "cost" in line.lower() or "result" in line.lower()):
        header_idx = i
        break

# Parse from header row
reader = csv.DictReader(lines[header_idx:])
headers = reader.fieldnames or []

col_campaign = find_column(headers, COLUMN_ALIASES["campaign_name"])
col_spend = find_column(headers, COLUMN_ALIASES["amount_spent"])
col_results = find_column(headers, COLUMN_ALIASES["results"])
col_ctr = find_column(headers, COLUMN_ALIASES["ctr"])

if not col_campaign:
    print("Error: Could not find a 'Campaign name' column in the CSV.")
    print(f"Found columns: {headers}")
    sys.exit(1)

if not col_spend:
    print("Error: Could not find an 'Amount spent' column in the CSV.")
    print(f"Found columns: {headers}")
    sys.exit(1)

print(f"Columns mapped:")
print(f"  Campaign: {col_campaign}")
print(f"  Spend:    {col_spend}")
print(f"  Results:  {col_results or '(not found, will default to 0)'}")
print(f"  CTR:      {col_ctr or '(not found, will default to 0)'}")
print()

# ── Aggregate by campaign → project ──
# Structure: { project_key: { campaigns: { campaign_name: {spend, leads, ctr} } } }
projects = {}

for row in reader:
    name = row.get(col_campaign, "").strip()
    if not name or name.lower() in ("total", "totals", ""):
        continue

    # Skip summary/total rows
    spend_raw = row.get(col_spend, "0").replace(",", "").replace("$", "").strip()
    results_raw = row.get(col_results, "0").replace(",", "").strip() if col_results else "0"
    ctr_raw = row.get(col_ctr, "0").replace(",", "").replace("%", "").strip() if col_ctr else "0"

    try:
        spend = round(float(spend_raw), 2) if spend_raw else 0
    except ValueError:
        spend = 0
    try:
        leads = int(float(results_raw)) if results_raw else 0
    except ValueError:
        leads = 0
    try:
        ctr = round(float(ctr_raw), 2) if ctr_raw else 0
    except ValueError:
        ctr = 0

    # Match campaign name to a project via substring matching
    project_key = None
    for substring, key in campaign_map.items():
        if substring.lower() in name.lower():
            project_key = key
            break

    if not project_key:
        project_key = "_unmapped"
        print(f"  Warning: No mapping for campaign '{name}' — grouped under '_unmapped'")

    if project_key not in projects:
        projects[project_key] = {"campaigns": {}}

    if name in projects[project_key]["campaigns"]:
        # Merge duplicates (e.g., same campaign name across ad sets)
        existing = projects[project_key]["campaigns"][name]
        existing["adSpend"] = round(existing["adSpend"] + spend, 2)
        existing["leads"] += leads
        # Weighted average CTR would be ideal but we take the last value
        if ctr > 0:
            existing["ctr"] = ctr
    else:
        projects[project_key]["campaigns"][name] = {
            "adSpend": spend,
            "leads": leads,
            "ctr": ctr,
        }

# ── Build fbAds array ──
fb_ads = []
total_spend = 0
total_leads = 0

for project_key, pdata in sorted(projects.items()):
    if project_key == "_unmapped":
        continue
    campaigns = []
    for cname, cdata in pdata["campaigns"].items():
        campaigns.append({
            "name": cname,
            "adSpend": cdata["adSpend"],
            "leads": cdata["leads"],
            "ctr": cdata["ctr"],
        })
        total_spend += cdata["adSpend"]
        total_leads += cdata["leads"]
    fb_ads.append({
        "project": project_key,
        "campaigns": campaigns,
    })

# Handle unmapped campaigns (still count toward totals)
if "_unmapped" in projects:
    unmapped_campaigns = []
    for cname, cdata in projects["_unmapped"]["campaigns"].items():
        unmapped_campaigns.append({
            "name": cname,
            "adSpend": cdata["adSpend"],
            "leads": cdata["leads"],
            "ctr": cdata["ctr"],
        })
        total_spend += cdata["adSpend"]
        total_leads += cdata["leads"]
    fb_ads.append({
        "project": "unmapped",
        "campaigns": unmapped_campaigns,
    })

total_spend = round(total_spend, 2)
cost_per_lead = round(total_spend / total_leads, 2) if total_leads > 0 else 0

print(f"Parsed {sum(len(p['campaigns']) for p in fb_ads)} campaigns across {len(fb_ads)} projects")
print(f"  Total spend:  ${total_spend:,.2f}")
print(f"  Total leads:  {total_leads}")
print(f"  Cost/lead:    ${cost_per_lead:.2f}")
print()

# ── Update dashboard-data.json ──
with open(JSON_FILE, "r") as f:
    data = json.load(f)

weeks = data["metrics"]["weeks"]
latest = weeks[-1]

latest["adSpend"] = total_spend
latest["leads"] = total_leads
latest["costPerLead"] = cost_per_lead
latest["fbAds"] = fb_ads

# Compute a blended CTR from all campaigns
all_ctrs = []
for p in fb_ads:
    for c in p["campaigns"]:
        if c["ctr"] > 0:
            all_ctrs.append(c["ctr"])
if all_ctrs:
    latest["ctr"] = round(sum(all_ctrs) / len(all_ctrs), 2)

with open(JSON_FILE, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")

print(f"Updated week {latest['date']} in dashboard-data.json")

# ── Regenerate dashboard-data.js ──
js = "// Auto-generated. Do not edit manually.\n"
js += "window.FL3_DASHBOARD_DATA = " + json.dumps(data, indent=2) + ";\n"

with open(JS_FILE, "w") as f:
    f.write(js)

print("Regenerated dashboard-data.js")
PYTHON_SCRIPT

if [ $? -ne 0 ]; then
  echo ""
  echo "Error: Python script failed. Check the CSV format."
  exit 1
fi

# ── Git commit and push ──
echo ""
echo "Pushing to GitHub..."
cd "$REPO_ROOT"
git add docs/dashboard-data.json docs/dashboard-data.js
git commit -m "Update Facebook Ads metrics from CSV import"
git push

# ── Archive processed CSV ──
ARCHIVE_DIR="$DROP_DIR/processed"
mkdir -p "$ARCHIVE_DIR"
mv "$CSV_FILE" "$ARCHIVE_DIR/"
echo "Archived CSV to: $ARCHIVE_DIR/$(basename "$CSV_FILE")"

echo ""
echo "Done! Dashboard updated with Facebook Ads data."
echo "Live at: https://jscott-62.github.io/fl3-dashboard/"
