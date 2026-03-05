---
name: fl3-dashboard
description: Updates the FL3 business dashboard data, deploys to GitHub Pages. The dashboard tracks projects, goals, weekly metrics, Facebook Ads, and content production for Freedom Life 3.0.
license: Private
metadata:
  version: 2.0.0
  author: J. Scott MacMillan
  category: fl3-business-operations
  updated: 2026-03-04
---

# FL3 Dashboard Updater

Updates `docs/dashboard-data.json` with the latest business metrics, project statuses, goals, and content schedule. The dashboard (`docs/index.html`) reads this data to render KPI cards, progress bars, Facebook Ads tracking, project tabs, Content Hub, and a weekly content pipeline.

**Live URL:** https://jscott-62.github.io/fl3-dashboard/
**GitHub Repo:** https://github.com/jscott-62/fl3-dashboard

## Key Files

| File | Purpose |
|------|---------|
| `docs/index.html` | The entire dashboard app (HTML + CSS + JS, single file) |
| `docs/dashboard-data.json` | Canonical data source: projects, goals, metrics, content schedule |
| `docs/dashboard-data.js` | JS wrapper loaded via `<script src>` for fast page load |
| `docs/content-dashboard.html` | Content Command Center (separate production tracking tool) |
| `scripts/update-metrics.sh` | Pulls email list from GHL API, updates data, pushes to GitHub |
| `scripts/sync-weekly-content.sh` | Scans Weekly-Content folders, adds new items, pushes to GitHub |
| `scripts/.env` | GHL API credentials (git-ignored, never committed) |

## When to Use This Skill

- After collecting weekly metrics (pairs with `/fl3-metrics`)
- When a project asset is completed or changes status
- When adjusting business goals or targets
- After any content production skill (youtube, blog, social, newsletter)
- Before reviewing the dashboard to ensure data is current

## Accepted Commands

### Full Update
`/fl3-dashboard` (no arguments)
Prompts for all sections: metrics, project status, goals, and content.

### Section-Specific Updates
- `/fl3-dashboard metrics` - Update only the weekly metrics
- `/fl3-dashboard launch` - Update only project asset statuses
- `/fl3-dashboard goals` - Update only target goals
- `/fl3-dashboard content` - Update only the content schedule
- `/fl3-dashboard status [project] [asset] [status]` - Quick-update a single asset
- `/fl3-dashboard content-status [weekOf] [type] [status]` - Quick-update a single content item

## Data Structure (v2 Schema)

```json
{
  "lastUpdated": "YYYY-MM-DD",
  "projects": {
    "<project-key>": {
      "name": "Display Name",
      "status": "live|in_development|planned|active|in_progress",
      "description": "Short description",
      "folder": "Projects/Folder-Name/",
      "assets": {
        "<assetKey>": {
          "status": "complete|in_progress|not_started|review",
          "label": "Display Label",
          "path": "vault-relative/path/to/file.md | null"
        }
      },
      "contentFolders": { ... }
    }
  },
  "metrics": {
    "weeks": [
      {
        "date": "YYYY-MM-DD",
        "emailList": 0,
        "emailOpenRate": 0,
        "youtubeSubscribers": 0,
        "youtubeViews": 0,
        "adSpend": 0,
        "costPerLead": 0,
        "ctr": 0,
        "leads": 0,
        "courseSales": 0,
        "revenue": 0,
        "webinarRegistrations": 0,
        "webinarAttendance": 0,
        "fbAds": [
          {
            "project": "project-key",
            "campaigns": [
              { "name": "Campaign Name", "adSpend": 0, "leads": 0, "ctr": 0 }
            ]
          }
        ]
      }
    ]
  },
  "goals": {
    "emailListTarget": 5000,
    "revenueTarget": 10000,
    "courseSalesTarget": 20,
    "costPerLeadTarget": 5.00
  }
}
```

### Projects Tracked

| Key | Project | Status |
|-----|---------|--------|
| `wrong-asset-manifesto` | The Wrong Asset Manifesto (lead magnet) | live |
| `the-great-catch-up` | The Great Catch Up ($495 program) | in_development |
| `webinar` | Conversion Webinar | planned |
| `weekly-content` | Weekly Content Production | active |
| `book` | Be The Hero Of Your Financial Life | in_progress |

### Content Folders Structure (weekly-content project)

The `weekly-content` project uses `contentFolders` instead of `assets`:

```json
"contentFolders": {
  "youtube": {
    "label": "YouTube",
    "items": [
      {
        "title": "Content Title",
        "steps": { "research": false, "write": false, "film": false, "edit": false, "publish": false },
        "path": "00-ZenithPro - FL3/Projects/Weekly-Content/YouTube/filename.md"
      }
    ]
  },
  "articles": { "label": "Articles", "items": [...] },
  "social-media": { "label": "Social Media", "items": [...] },
  "email": { "label": "Email", "items": [...] }
}
```

**Steps by content type:**
- YouTube, Social Media: `research, write, film, edit, publish`
- Articles, Email: `research, write, edit, publish`

### Facebook Ads Structure

Two-level hierarchy: Projects > Campaigns.

```json
"fbAds": [
  {
    "project": "wrong-asset-manifesto",
    "campaigns": [
      { "name": "Standard Ads", "adSpend": 109.37, "leads": 16, "ctr": 2.33 },
      { "name": "Retargeting", "adSpend": 156.52, "leads": 9, "ctr": 2.83 }
    ]
  }
]
```

CPL auto-calculated per campaign, per project subtotal, and grand total. Top-level `adSpend`, `leads`, `costPerLead` fields auto-sync from grand totals.

## Complete Workflow

### Phase 1: Read Current State

Read `docs/dashboard-data.json` to understand:
- Current project statuses and asset completion
- Metric values and weekly history
- Current goals
- Content schedule status

### Phase 2: Accept Updates

Collect the relevant data based on the command used. See Accepted Commands section above for field details.

**For Metrics:** Add new entry to `metrics.weeks` array. Never overwrite previous weeks.
**For Project Status:** Update `projects.[key].assets.[assetKey].status`
**For Goals:** Update `goals` fields
**For Content:** Update items in `projects.weekly-content.contentFolders`

### Phase 3: Validate Data

1. All numeric values >= 0. Rates between 0 and 1.
2. Dates in YYYY-MM-DD format.
3. Status values only from allowed set.
4. `metrics.weeks` chronologically ordered.
5. Never remove existing week entries.
6. Asset paths are vault-relative (e.g., `00-ZenithPro - FL3/Projects/...`).

### Phase 4: Write Updated Data

1. Read current `docs/dashboard-data.json`
2. Merge updates into existing structure
3. Set `lastUpdated` to today's date
4. Write updated JSON to `docs/dashboard-data.json`
5. Regenerate `docs/dashboard-data.js`:
   ```js
   // Auto-generated by /fl3-dashboard skill. Do not edit manually.
   window.FL3_DASHBOARD_DATA = { ...json data... };
   ```

### Phase 5: Deploy to GitHub Pages

From the Business Suite root (the git repo root):

```bash
git add docs/dashboard-data.json docs/dashboard-data.js
git commit -m "Dashboard update YYYY-MM-DD"
git push
```

GitHub Pages serves from the `docs/` folder on the `main` branch. Changes go live within 1 to 2 minutes.

### Phase 6: Summary Output

```markdown
## Dashboard Updated

**Date:** [Today]
**Sections updated:** [Metrics / Projects / Goals / Content]

### Changes Made
- [Field: old -> new]

### Dashboard Status
- Projects: [X/Y assets complete]
- Content: [X items tracked]
- Weeks of data: [N]

*View online: https://jscott-62.github.io/fl3-dashboard/*
```

## GHL API Integration

**Endpoint:** `GET https://services.leadconnectorhq.com/contacts/?locationId={id}&limit=1`
**Auth:** `Authorization: Bearer {token}` + `Version: 2021-07-28`
**Response:** `meta.total` = total contact count

**Credentials:** `scripts/.env` (git-ignored)

**To update email list:** Run `scripts/update-metrics.sh`
- Fetches count from GHL
- Creates new week snapshot if 7+ days since last entry
- Updates `docs/dashboard-data.json` and `.js`
- Commits and pushes to GitHub

**To sync new content:** Run `scripts/sync-weekly-content.sh`
- Scans `Projects/Weekly-Content/` folders for new .md files
- Adds them to the dashboard content schedule
- Commits and pushes to GitHub

## Architecture

- **Single-file app**: All HTML, CSS, JS in `docs/index.html`. No framework, no build step.
- **Data loading priority**: GitHub API > bundled `dashboard-data.js` > fetch JSON > localStorage
- **Persistence**: Checkbox changes save to localStorage, then auto-sync to GitHub (2s debounce)
- **GitHub token**: `localStorage` key `fl3-github-token`, set via sync status indicator

## Design System

- **Dark theme**: Background `#0f172a`, cards `#1e293b`, text `#e2e8f0`
- **Accent**: Amber `#f59e0b`
- **Status colors**: Green (complete/live), Blue (in_progress/active), Amber (in_development), Red (errors), Purple (review), Gray (not_started/planned)
- **Fonts**: System fonts only
- **No external dependencies**

## Integration with Other Skills

Called after: `/fl3-metrics`, `/fl3-youtube`, `/fl3-blog`, `/fl3-social`, `/fl3-newsletter`, `/fl3-launch`, `/fl3-weekly-content`

## Common Mistakes to Avoid

1. Never replace `metrics.weeks`. Always append.
2. Use exact status strings. Dashboard renders based on these.
3. Always set `lastUpdated` to today.
4. Use camelCase for asset keys (`salesPage`, not `sales-page`).
5. Store rates as decimals (25% = `0.25`).
6. Set `path` when asset files are created (vault-relative paths).
7. Never overwrite `dashboard-data.js` manually. Always regenerate from JSON.

## Reference Paths

| Resource | Path (relative to Business Suite root) |
|----------|---------------------------------------|
| Dashboard data | `docs/dashboard-data.json` |
| Dashboard JS | `docs/dashboard-data.js` |
| Dashboard HTML | `docs/index.html` |
| Content Command Center | `docs/content-dashboard.html` |
| Update metrics script | `scripts/update-metrics.sh` |
| Sync content script | `scripts/sync-weekly-content.sh` |
| GHL credentials | `scripts/.env` |
| Content calendar | `calendar/content-calendar.md` |
| Weekly metric reports | `reports/weekly-reports/` |

---

*FL3 Dashboard Updater v2.0.0*
