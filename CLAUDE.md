# FL3 Business Dashboard

## What This Is

The Freedom Life 3.0 (FL3) Business Dashboard is a single-page HTML app hosted on GitHub Pages. It tracks project status, company goals, weekly metrics, and content production for the FL3 business.

**Live URL:** https://jscott-62.github.io/fl3-dashboard/
**GitHub Repo:** https://github.com/jscott-62/fl3-dashboard
**Branch:** main (GitHub Pages deploys from main)

## Key Files

| File | Purpose |
|------|---------|
| `index.html` | The entire dashboard app (HTML + CSS + JS, single file) |
| `dashboard-data.json` | Canonical data source: projects, goals, metrics, content schedule |
| `dashboard-data.js` | JS wrapper around the JSON data (loaded via `<script src>` for fast page load) |
| `content-dashboard.html` | Content Command Center (separate tool for tracking content production steps) |
| `update-metrics.sh` | Pulls email list count from GHL API, updates data files, pushes to GitHub |
| `.env` | GHL API credentials (never committed to git) |
| `.gitignore` | Keeps `.env` out of the repo |
| `archive/` | Old v1 dashboard files for reference only |

## Architecture

- **Single-file app**: All HTML, CSS, and JS live in `index.html`. No build step, no framework.
- **Data loading priority**: GitHub API (if token configured) > bundled `dashboard-data.js` > fetch `dashboard-data.json` > localStorage fallback
- **Persistence**: Checkbox changes save to localStorage immediately, then auto-sync to GitHub via the Contents API after a 2-second debounce. Both `dashboard-data.json` and `dashboard-data.js` are updated on each sync.
- **GitHub token**: Stored in `localStorage` as `fl3-github-token`. Users set this up once via the sync status indicator in the header.

## Page Layout (top to bottom)

1. **Header**: Title + last updated date + GitHub sync status
2. **Goals Progress**: 2x2 grid of progress bars (Email List, Revenue, Course Sales, Cost Per Lead)
3. **Weekly Metrics**: 4-card row (New Emails This Week, Email Open Rate, YouTube Views, Webinar Registrations)
4. **Facebook Ads**: Project groups with nested campaigns, click-to-edit metrics, subtotals per project, grand total
5. **Project Tabs**: Content Hub (first, active by default) + tabbed views for each project (Wrong Asset Manifesto, The Great Catch Up, Webinar, Weekly Content, Book)
6. **Instructions**: How-to text for updating the dashboard
7. **Save Bar**: Fixed bottom bar showing sync status
8. **Modals**: Token setup overlay, Markdown preview overlay

## Data Structure (dashboard-data.json)

```
{
  "lastUpdated": "YYYY-MM-DD",
  "projects": {
    "<project-key>": {
      "name": "Display Name",
      "status": "live|in_development|planned|active|in_progress",
      "description": "Short description",
      "folder": "Projects/Folder-Name/",
      "assets": {                    // For asset-based projects
        "<assetKey>": { "status": "complete|in_progress|not_started|review", "label": "Display Label", "path": null }
      },
      "contentSchedule": [...]       // For weekly-content project only
    }
  },
  "metrics": {
    "weeks": [
      {
        "date": "YYYY-MM-DD",
        "emailList": 2510,
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
            "project": "wrong-asset-manifesto",
            "campaigns": [
              { "name": "Standard Ads", "adSpend": 0, "leads": 0, "ctr": 0 },
              { "name": "Retargeting", "adSpend": 0, "leads": 0, "ctr": 0 }
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

## Content Schedule Structure (weekly-content project)

Each week in `contentSchedule` has:
```
{
  "weekOf": "YYYY-MM-DD",
  "weekLabel": "Week of Mon DD",
  "pillar": "Content pillar name",
  "avatar": "Target avatar",
  "items": [
    {
      "type": "youtube|blog|social|newsletter",
      "title": "Content title",
      "steps": { "research": bool, "script|write": bool, "film": bool, "edit": bool, "publish": bool },
      "dueDate": "YYYY-MM-DD" or null,
      "path": "relative/path/to/file.md" or null
    }
  ]
}
```

## Content Command Center (content-dashboard.html)

A separate tool for tracking individual content piece production. Uses localStorage (key: `contentCommandCenter`). Supports:
- Card view and Pipeline view
- Content types: Blog Post, YouTube Video, Short Video, FB Post
- Each type has defined production steps
- Blog posts track publish status across Medium, LinkedIn, Website

## GHL API Integration

The dashboard pulls the email list count from GoHighLevel via their REST API.

**API Endpoint:** `GET https://services.leadconnectorhq.com/contacts/?locationId={id}&limit=1`
**Auth Header:** `Authorization: Bearer {token}`
**Version Header:** `Version: 2021-07-28`
**Response:** `meta.total` contains the total contact count.

**Credentials** are stored in `.env` (git-ignored, never committed):
```
GHL_API_TOKEN=pit-...
GHL_LOCATION_ID=AIb...
```

**To update the email list count:**
```bash
./update-metrics.sh
```
This fetches the count from GHL, updates `dashboard-data.json` and `dashboard-data.js`, commits, and pushes to GitHub.

**Automatic weekly snapshots:** The script checks the date of the latest week entry in `metrics.weeks`. If it is 7 or more days old, it freezes the current week as a historical snapshot and creates a new week entry with fresh data. If less than 7 days old, it updates the current week in place. This is what powers the "New Emails This Week" metric card, which computes the difference between the two most recent week entries.

**"New Emails This Week" metric:** Calculated in `index.html` render function as `latest.emailList - previous.emailList`. Displays in green when positive. Shows `+0` when there is only one week of data.

**Claude can also update directly** by:
1. Reading credentials from `.env` at `Projects/fl3-dashboard/.env`
2. Calling the GHL API with curl
3. Checking if a new week entry is needed (latest week date 7+ days old)
4. Updating `emailList` in `dashboard-data.json` (new week entry or update in place)
5. Regenerating `dashboard-data.js`
6. Committing and pushing to GitHub

## Facebook Ads Section

Tracks Facebook ad metrics in a two-level hierarchy: **Projects > Campaigns**.

**Data structure:** `fbAds[]` contains project entries. Each has `project` (project key) and `campaigns[]`. Each campaign has `name`, `adSpend`, `leads`, `ctr`. CPL is auto-calculated per campaign, per project subtotal, and grand total.

**UI layout:**
- **"+ Add Project"** button in header shows picker (excludes weekly-content and book)
- Each project group has a header bar with the project name, "+ Campaign" button, and remove X
- Campaigns listed in a table with click-to-edit Ad Spend, Leads, CTR
- **Subtotal row** per project sums all campaigns
- **Grand total** shown when 2+ projects exist (spend-weighted average CTR)

**Migration:** Old flat format (`{campaign, adSpend, leads, ctr}`) is auto-migrated to the new nested format on first render.

**Top-level sync:** The `adSpend`, `leads`, `costPerLead` fields at the week level are auto-synced from grand totals, keeping the Cost Per Lead goal bar working.

**Future automation:** When Facebook Marketing API integration is added, a script can populate the `fbAds` array in `dashboard-data.json` directly. The same UI will display without changes.

## Content Hub Tab

A unified view of all content across all projects. This is the first tab (active by default) in the Project Tabs section.

**Features:**
- **Stats bar**: 4 cards showing Total Content, Completed, Linked Files, Progress %
- **Collapsible project sections**: Each project shows its content items grouped together
- **Type badges**: Color-coded badges (YouTube=red, Blog=blue, Social=purple, Newsletter=teal, Asset=gray, Chapter=amber)
- **Step dots**: Weekly content items show production step progress as colored dots (green=done, gray=pending)
- **Status badges**: Complete, In Progress, Not Started, Review
- **Preview button**: Opens markdown files in the existing markdown preview modal (works locally only)
- **Open in Obsidian button**: Uses `obsidian://open` URI scheme to open files directly in Obsidian
- **Book collapsed by default**: 14 chapter items are collapsed to avoid dominating the view

**Architecture:**
- Virtual tab, not in `PROJECT_ORDER`. Hardcoded as first tab in `renderProjectTabs()`.
- Read-only aggregate view. No editing in the hub; users edit in project tabs or Obsidian.
- Key functions: `buildContentHubView(data)`, `buildObsidianLink(path)`, `getContentTypeConfig(type)`
- Reuses existing functions: `getStepDefs()`, `getStatusFromSteps()`, `escapeHtml()`, `escapeAttr()`, `openMdPreview()`

**File paths**: Asset `path` fields in `dashboard-data.json` store vault-relative paths (e.g., `00-ZenithPro - FL3/Projects/Book/Drafts/Chapter_1_The_2_AM_reckoning.md`). These are used for both Obsidian URI links and markdown preview.

**Book project**: Expanded from single "manuscript" asset to 14 individual chapter assets, each with a path to its draft file.

## How to Deploy Changes

All changes must be pushed to the `main` branch of `jscott-62/fl3-dashboard` on GitHub. GitHub Pages auto-deploys from main. After pushing, changes go live within 1 to 2 minutes.

```bash
cd <this-directory>
git add <files>
git commit -m "Description of changes"
git push
```

## Design System

- **Dark theme**: Background `#0f172a`, cards `#1e293b`, text `#e2e8f0`
- **Accent color**: Amber `#f59e0b` (used for headers, highlights, active states)
- **Status colors**: Green (complete/live), Blue (in progress/active), Amber (in development), Red (errors/overdue), Purple (review), Gray (not started/planned)
- **Font**: System fonts (-apple-system, BlinkMacSystemFont, Segoe UI)
- **No external dependencies**: No frameworks, no build tools, no CDN resources

## Business Context

FL3 (Freedom Life 3.0) targets people aged 40 to 65 who are behind on retirement savings. The marketing funnel is:

```
Facebook Ads > Wrong Asset Manifesto (lead magnet) > Email Capture
  > Email Nurture Sequence > Webinar Registration > Webinar
  > The Great Catch Up (6-week program, $495)
```

Projects tracked:
1. **Wrong Asset Manifesto** (lead magnet, LIVE)
2. **The Great Catch Up** (core revenue product, in development)
3. **Webinar** (conversion event, planned)
4. **Weekly Content** (ongoing content production)
5. **Book: Be The Hero Of Your Financial Life** (authority builder)
