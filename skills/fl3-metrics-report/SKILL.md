---
name: fl3-metrics-report
description: Weekly/monthly business metrics tracker for Freedom Life 3.0. Accepts key metrics, produces trend analysis, and generates actionable recommendations.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-business-operations
  framework_count: 3
  updated: 2026-02-13
---

# FL3 Metrics Report - Business Performance Tracker

Accepts manual input of key business metrics, compares to previous periods, calculates trends, and produces actionable recommendations in FL3's strategic context.

## When to Use This Skill

- Weekly business review
- Monthly performance summary
- Before making budget or strategy decisions
- Post-launch analysis
- When the Strategy Advisor agent needs data

## Complete Workflow

### Phase 1: Accept Current Metrics

Collect for the current period:

**Email Metrics:**
- List size (total subscribers)
- New subscribers this period
- Unsubscribe rate
- Open rate (newsletter)
- Click rate (newsletter)

**YouTube Metrics:**
- New subscribers
- Total views this period
- Average view duration
- Top performing video

**Social Metrics:**
- Follower growth (IG, FB, LI)
- Engagement rate
- Top performing post

**Ad Metrics:**
- Total ad spend
- Impressions
- Clicks
- Cost per click (CPC)
- Cost per lead (CPL)
- Leads generated

**Revenue Metrics:**
- Course sales (count)
- Revenue
- Refund count/rate
- Average order value

**Webinar Metrics (if applicable):**
- Registrations
- Attendance rate
- Conversion rate

### Phase 2: Compare to Previous Periods

Read previous reports from `reports/weekly-reports/` and calculate:
- Week-over-week change (%)
- Month-over-month change (%)
- Trend direction (improving, declining, stable)

### Phase 3: Produce Report

```markdown
## FL3 METRICS REPORT: [Period]

### KEY NUMBERS
| Metric | This Period | Last Period | Change | Trend |
|--------|-----------|------------|--------|-------|
| Email list size | [X] | [X] | [+/-X%] | [arrow] |
| Email open rate | [X%] | [X%] | [+/-X%] | [arrow] |
| YouTube views | [X] | [X] | [+/-X%] | [arrow] |
| Ad spend | $[X] | $[X] | [+/-X%] | [arrow] |
| Cost per lead | $[X] | $[X] | [+/-X%] | [arrow] |
| Course sales | [X] | [X] | [+/-X%] | [arrow] |
| Revenue | $[X] | $[X] | [+/-X%] | [arrow] |

### WINS
- [What's working well]

### CONCERNS
- [What needs attention]

### RECOMMENDATIONS
1. [Specific, actionable recommendation]
2. [Specific, actionable recommendation]
3. [Specific, actionable recommendation]
```

Save to `reports/weekly-reports/[date]-metrics.md`

---

*FL3 Metrics Report - Data-Driven Decisions v1.0.0*
