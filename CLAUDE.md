# FL3 Business Agent Suite

The complete agent and skill system for running Freedom Life 3.0 as a business. 18 skills, 5 agents, and a live business dashboard covering content production, launch infrastructure, business operations, and quality control.

## What This System Is

- **18 skills** for creating FL3 content across all platforms
- **5 agents** for autonomous multi-step workflows
- **Live business dashboard** deployed on GitHub Pages
- **Full Obsidian vault integration** with structured output folders
- **Integration with Copy Arsenal** and **Webinar Arena** for maximum quality when needed
- **Git-backed**: entire system is version-controlled and deploys the dashboard automatically

All content produced by this system must sound like J. Scott MacMillan, target the right avatar, respect the Reveal Sequence, and pass compliance checks.

## Quick Commands

### Content Production
| Command | What It Does |
|---------|-------------|
| `/fl3-weekly` | Full weekly content: YouTube + blog + social + newsletter |
| `/fl3-youtube` | Standalone YouTube script |
| `/fl3-blog` | SEO-optimized blog post |
| `/fl3-social` | Batch of platform-specific social posts |
| `/fl3-newsletter` | Beehiiv newsletter |
| `/fl3-email-sequence` | Multi-email nurture/launch sequence |
| `/fl3-ads` | Facebook/Instagram ad copy |
| `/fl3-lead-magnet` | Complete lead magnet package |

### Launch Infrastructure
| Command | What It Does |
|---------|-------------|
| `/fl3-sales-page` | Sales page for The Great Catch-Up |
| `/fl3-webinar` | Webinar brief for the Webinar Arena |
| `/fl3-launch` | Complete launch sequence (all assets) |
| `/fl3-funnel-audit` | Audit entire funnel |

### Business Operations
| Command | What It Does |
|---------|-------------|
| `/fl3-calendar` | Content calendar management |
| `/fl3-metrics` | Business metrics report |
| `/fl3-competitors` | Competitive intelligence |
| `/fl3-dashboard` | Update dashboard data (metrics, projects, goals, content) |
| `/fl3-dashboard metrics` | Update only weekly metrics |
| `/fl3-dashboard launch` | Update only project asset statuses |
| `/fl3-dashboard goals` | Update only target goals |
| `/fl3-dashboard content` | Update only the content creation pipeline |
| `/fl3-dashboard status [project] [asset] [status]` | Quick-update a single asset |
| `/fl3-dashboard content-status [weekOf] [type] [status]` | Quick-update a single content item |

### Quality Control
| Command | What It Does |
|---------|-------------|
| `/fl3-voice-check` | Voice consistency validation |
| `/fl3-compliance` | Financial compliance check |
| `/fl3-review` | Full brand review (voice + compliance + avatar) |
| `/fl3-review-batch` | Review all current drafts |

### Autonomous Workflows
| Command | What It Does |
|---------|-------------|
| `/fl3-content-week` | Content Director: full weekly production |
| `/fl3-launch-plan` | Launch Director: plan the launch |
| `/fl3-launch-go` | Launch Director: execute the launch |
| `/fl3-digest` | Digest Processor: process weekly YouTube digest |
| `/fl3-strategy` | Strategy Advisor: strategic analysis |
| `/fl3-quarterly-review` | Strategy Advisor: quarterly planning |

## Folder Structure

```
Business-Suite/                    <-- Git repo root (deploys to GitHub Pages)
  .git/                            <-- Version control + deployment
  .gitignore                       <-- Protects .env, .claude/, .DS_Store
  CLAUDE.md                        <-- You are here

  docs/                            <-- GitHub Pages serves from here
    index.html                     <-- Dashboard app (single-file HTML/CSS/JS)
    content-dashboard.html         <-- Content Command Center
    dashboard-data.json            <-- Source of truth for all dashboard data
    dashboard-data.js              <-- Auto-generated JS wrapper

  scripts/
    update-metrics.sh              <-- GHL API integration (email list)
    sync-weekly-content.sh         <-- Scans Weekly-Content, syncs to dashboard
    archive-published.sh           <-- Moves published content to Archive/
    .env                           <-- GHL API credentials (git-ignored)

  skills/                          <-- 18 skill definitions
    fl3-dashboard/                 <-- Dashboard data updater
    fl3-voice-check/               <-- Quality gate for all content
    fl3-compliance-check/          <-- Financial compliance validator
    fl3-sales-page/                <-- Sales page generator
    fl3-email-sequence/            <-- Email sequence builder
    fl3-ad-copy/                   <-- Ad copy generator
    fl3-webinar-brief/             <-- Webinar brief for arena
    fl3-launch-sequence/           <-- Launch orchestration
    fl3-funnel-audit/              <-- Funnel auditor
    fl3-youtube-script/            <-- YouTube script generator
    fl3-blog-post/                 <-- Blog post generator
    fl3-social-batch/              <-- Social media batch generator
    fl3-newsletter/                <-- Beehiiv newsletter creator
    fl3-weekly-content/            <-- Weekly content orchestrator
    fl3-content-calendar/          <-- Content calendar manager
    fl3-metrics-report/            <-- Metrics tracker
    fl3-competitor-intel/          <-- Competitive intelligence
    fl3-lead-magnet/               <-- Lead magnet creator

  agents/                          <-- 5 autonomous agents
    fl3-brand-guardian/            <-- Quality control agent
    fl3-launch-director/           <-- Launch operations manager
    fl3-content-director/          <-- Weekly content orchestrator
    fl3-strategy-advisor/          <-- Strategic planning agent
    fl3-digest-processor/          <-- Digest intake agent

  Weekly-Content/                  <-- All weekly content (scripts, articles, posts)
    Briefs/                        <-- Weekly content briefs (master control per week)
      _BRIEF-TEMPLATE.md           <-- Template for new briefs
    YouTube/                       <-- YouTube scripts and video content
    Articles/                      <-- Blog articles and written content
    Social Media/                  <-- Social media posts
    Email/                         <-- Email campaigns and newsletters
    Archive/                       <-- Published content (moved here on publish)

  calendar/                        <-- Operational planning
    content-calendar.md            <-- Content calendar + rotation
    idea-bank.md                   <-- Content idea repository

  reports/                         <-- Business intelligence
    weekly-reports/                <-- Detailed metric reports from /fl3-metrics

  archive/                         <-- Old v1 dashboard files (reference only)
```

### Content Output Locations

Weekly content lives inside Business Suite. Other content in vault project folders:

| Content Type | Save Location |
|-------------|---------------|
| YouTube scripts | `Weekly-Content/YouTube/` (in Business Suite) |
| Blog articles | `Weekly-Content/Articles/` (in Business Suite) |
| Social media | `Weekly-Content/Social Media/` (in Business Suite) |
| Email/newsletters | `Weekly-Content/Email/` (in Business Suite) |
| Weekly briefs | `Weekly-Content/Briefs/` (in Business Suite) |
| Published content | `Weekly-Content/Archive/` (moved here on publish) |
| Sales page | `Projects/The-Great-Catch-Up/Sales-Page/` |
| Email sequences | `Projects/The-Great-Catch-Up/Email-Sequences/` |
| Facebook ads | `Projects/Wrong-Asset-Manifesto/Facebook-Ads/` |
| Webinar assets | `Projects/Webinar/` |

## Weekly Content Brief Workflow

Every week's content is controlled by a **Weekly Content Brief**, a single document that defines the angle, key points, avatar hook, data, CTA, tone, and restrictions for all content produced that week. Edit the brief, regenerate the content.

### How It Works

1. **Brief is created first.** Either drafted by Claude from the calendar/digest and reviewed by Scott, or written directly by Scott.
2. **Brief lives at** `Weekly-Content/Briefs/[YYYY-MM-DD] - [Topic].md`
3. **All content skills read the brief first.** The blog, social, newsletter, and YouTube skills all check for a brief before generating content. The brief overrides any other parameters.
4. **Edit one file, regenerate everything.** If Scott wants to change the angle, add a stat, or kill a point, he edits the brief in Obsidian and says "regenerate from the brief."

### Brief Template

The template is at `Weekly-Content/Briefs/_BRIEF-TEMPLATE.md` and contains:
- **The Angle:** The specific take (not just the pillar, but the argument)
- **Key Points (3-5):** Arguments every piece of content should make
- **Avatar Hook:** How you're speaking to this avatar, what pain, what language
- **Key Stats / Data:** Numbers to cite consistently
- **CTA:** What you're driving to
- **Tone Notes:** Any voice adjustments
- **Do NOT Say:** Words, phrases, or claims to avoid
- **Content Pieces to Generate:** Checkboxes for what to produce
- **Notes:** Stories, competitors, news events, previous content to reference

### Naming Convention

`[YYYY-MM-DD] - [Topic].md` where the date matches the `weekOf` field in the calendar.

Example: `2026-03-03 - The Playbook Against Your Retirement.md`

## Dashboard

**Live URL:** https://jscott-62.github.io/fl3-dashboard/
**GitHub Repo:** https://github.com/jscott-62/fl3-dashboard

### Architecture
- **Single-file app**: All HTML, CSS, JS in `docs/index.html`. No framework, no build step.
- **Data loading priority**: GitHub API > bundled `dashboard-data.js` > fetch JSON > localStorage
- **Persistence**: Checkbox changes save to localStorage, then auto-sync to GitHub (2s debounce)
- **GitHub token**: Stored in `localStorage` as `fl3-github-token`

### Data Structure (v2)

The dashboard tracks 5 projects, weekly metrics with Facebook Ads breakdown, and business goals. See `skills/fl3-dashboard/SKILL.md` for the complete schema.

### GHL API Integration

Pulls email list count from GoHighLevel. Credentials in `scripts/.env` (git-ignored).

```bash
# Update email list count
./scripts/update-metrics.sh

# Sync new content files to dashboard
./scripts/sync-weekly-content.sh

# Move published content to Archive/ folder
./scripts/archive-published.sh
```

All scripts auto-commit and push to GitHub, deploying the update.

### Archive on Publish

When a content item's "Publish" checkbox is clicked in the dashboard, two things happen:
1. **Data update**: The item's path changes to `Weekly-Content/Archive/{title} PUB ({date}).md`, with the original path saved for unpublishing
2. **File move**: The dashboard calls the Obsidian Local REST API (port 27123) to move the actual `.md` file on disk

**Requirements**: Obsidian must be running with the Local REST API plugin enabled. On first use, the dashboard prompts for the API key (stored in localStorage as `fl3-obsidian-api-key`). Find the key in Obsidian → Settings → Community Plugins → Local REST API.

**Fallback**: `./scripts/archive-published.sh` can be run manually if Obsidian is not available.

### Deployment

Push to `main` branch. GitHub Pages serves from the `docs/` folder. Changes go live in 1 to 2 minutes.

```bash
cd <Business-Suite root>
git add docs/dashboard-data.json docs/dashboard-data.js
git commit -m "Dashboard update"
git push
```

### Design System
- **Dark theme**: `#0f172a` background, `#1e293b` cards, `#e2e8f0` text
- **Accent**: Amber `#f59e0b`
- **Status colors**: Green (complete), Blue (in_progress), Amber (in_development), Red (errors), Purple (review), Gray (not_started)
- **No external dependencies**

## Integration with Existing Systems

### Copy Arsenal
For maximum quality on critical assets, delegate to the Copy Arsenal:
- Sales page: `/arena sales-page 3` (4 competing copywriters)
- Ad hooks: `/carlton-hooks` (maximum stopping power)
- Email sequences: `/clayton-email` (emotional trigger mastery)
- VSL scripts: `/evaldo` (video sales letter specialist)

### Webinar Arena
Create a webinar brief with `/fl3-webinar`, then run `/webinar-arena` to have 6 competing experts draft the webinar.

## Key Business Concepts

| Concept | Description |
|---------|-------------|
| **The 4 Pillars** | Math Doesn't Work, Traditional Advice Fails, Better Vehicles Exist, Risk Flipped |
| **3 Avatars** | Silent Technophobe (52-58), Paralyzed Pursuer (48-56), Awakened Skeptic (50-60) |
| **Reveal Sequence** | Bitcoin withheld in cold traffic. Teased in education. Named in reveal email. Open post-reveal. |
| **The Hero Investing Method** | Proprietary framework: FREEDOM acronym, 6-week program |
| **Freedom Number** | Personalized calculation of exact retirement target |
| **Risk Inversion** | "The real risk is staying in 7% assets, not being in Bitcoin" |

## Writing Rules

All content MUST follow these rules (from vault CLAUDE.md):
- **No em dashes** (use periods, commas, colons, parentheses instead)
- Direct, conversational tone
- Short sentences for impact
- Address reader as "you"
- Validate struggles without condescending
- 85% toward language / 15% strategic away language
- Education, not financial advice

## Reference Document Locations

| Document | Path | Used By |
|----------|------|---------|
| Voice DNA | `Main/Scott MacMillan Voice DNA/Voice DNA/` | All skills |
| Business Summary | `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` | All skills |
| Business Brief | `Main/FL3 ZenithPro Data/FL3 Business Brief.md` | Content + launch skills |
| Value Prop Stack | `Main/FL3 ZenithPro Data/FREEDOM LIFE 3.0_ VALUE PROPOSITION STACK.md` | Sales page, launch |
| Course Content | `Main/The Great Catch Up Course.md` | Sales page, email sequences |
| Avatars | `Main/Zenith Avatars/` | All content skills |
| Existing Ads | `Main/FL3 ZenithPro Data/Ads.md` | Ad copy skill |
| Headlines | `Main/FL3 ZenithPro Data/HEADLINES.md` | Sales page, ads |
| Lead Magnet | `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/` | Email sequence, lead magnet |
| Content Architecture | `Main/FL3 ZenithPro Data/SILENT TECHNOPHOBE - Content Ecosystem Architecture v2.0.md` | Content strategy |

---

*FL3 Business Agent Suite v2.0.0*
*Last Updated: March 4, 2026*
