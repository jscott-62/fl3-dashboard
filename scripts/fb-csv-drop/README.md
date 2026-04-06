# Facebook Ads CSV Drop Folder

Drop your Facebook Ads Manager CSV export here, then run:

```bash
cd /Users/macmini/fl3-dashboard
./scripts/import-fb-ads.sh
```

## How to export from Facebook Ads Manager

1. Open Facebook Ads Manager
2. Select the **Campaigns** tab
3. Set the date range to the current week (or whatever period you want)
4. Click **Reports** (top right) → **Export Table Data**
5. Choose **CSV** format
6. Save the file to this folder
7. Run the script

The script will parse the CSV, update the dashboard, push to GitHub, and move the CSV to `processed/`.

## Column requirements

The CSV needs at minimum:
- **Campaign name** (required)
- **Amount spent** (required)
- **Results** or **Leads** (optional, defaults to 0)
- **CTR** (optional, defaults to 0)

## Campaign mapping

Edit `scripts/fb-campaign-map.json` to map Facebook campaign names to dashboard project keys. The script uses substring matching (case-insensitive).
