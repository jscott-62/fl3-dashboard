---
name: fl3-funnel-audit
description: Audits the complete FL3 funnel for messaging consistency, avatar alignment, conversion optimization, and compliance. Reviews ads, landing pages, lead magnets, emails, webinars, and sales pages.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-launch-infrastructure
  framework_count: 5
  updated: 2026-02-13
---

# FL3 Funnel Audit - Complete Funnel Analysis System

Audits every stage of the FL3 funnel for messaging consistency, voice alignment, avatar targeting, compliance, and conversion optimization. Identifies gaps, misalignments, and opportunities.

## When to Use This Skill

- Before a course launch (ensure everything is aligned)
- When conversion rates need improvement
- After adding new funnel assets (new ads, new emails, etc.)
- Quarterly funnel health check
- When the Launch Director agent runs pre-launch verification

## Core Principles

1. **The funnel is one conversation.** Each stage should feel like the next sentence in a conversation, not a new conversation. Tone shifts, messaging contradictions, and audience mismatches break the flow.
2. **Audit the journey, not just the assets.** The transition between stages (ad to landing page, landing page to email, email to webinar) is where most funnels leak.
3. **The Reveal Sequence IS the funnel architecture.** The entire funnel is designed around the progressive revelation of Bitcoin as the catch-up asset. Any break in this sequence confuses and loses people.
4. **Compliance compounds.** A borderline claim in one asset becomes a clear violation when repeated across 5 assets.

## Complete Workflow

### Phase 1: Load All Funnel Assets

Load everything in the current funnel:

1. **Ads:** `Main/FL3 ZenithPro Data/Ads.md` and any in `Projects/Wrong-Asset-Manifesto/Facebook-Ads/`
2. **Landing pages:** `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/landing-page.html`
3. **Lead magnets:** `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/`
4. **Email sequences:** All in `Projects/The-Great-Catch-Up/Email-Sequences/` and `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/Wrong Asset Manifesto - Email Sequence.md`
5. **Sales page:** `Projects/The-Great-Catch-Up/Sales-Page/`
6. **Webinar:** `Main/FL3 ZenithPro Data/Webinar Arena Outputs/`
7. **Course:** `Main/The Great Catch Up Course.md`

### Phase 2: Map the Funnel Stages

Create a visual map of the current funnel:

```markdown
## CURRENT FUNNEL MAP

TRAFFIC → [Ad] → [Landing Page] → [Lead Magnet Delivery]
                                        ↓
                              [Email Sequence: 7 emails]
                                        ↓
                              [Webinar Invitation]
                                        ↓
                              [Webinar]
                                        ↓
                              [Sales Page]
                                        ↓
                              [Purchase]
                                        ↓
                              [Post-Purchase Onboarding]
```

### Phase 3: Audit Each Stage Against 5 Dimensions

For each funnel stage, score:

**Dimension 1: Reveal Sequence Compliance**
- Does this stage use appropriate Bitcoin language for its position?
- Is there a premature reveal or a missed reveal opportunity?

**Dimension 2: Voice Consistency**
- Does this asset sound like Scott?
- Run abbreviated voice check (key metrics only)

**Dimension 3: Avatar Alignment**
- Which avatar is this targeting?
- Is it consistent with adjacent funnel stages?

**Dimension 4: Message Continuity**
- Does the promise in the previous stage get delivered here?
- Is the CTA clear and consistent with the next stage?

**Dimension 5: Compliance**
- Any compliance issues at this stage?
- Are disclaimers present and visible?

### Phase 4: Identify Transition Gaps

The most critical audit happens BETWEEN stages:

| Transition | Check |
|---|---|
| Ad to Landing Page | Does the landing page deliver what the ad promised? |
| Landing Page to Lead Magnet | Does the lead magnet match the landing page description? |
| Lead Magnet to Email Sequence | Does email 1 reference the lead magnet they just received? |
| Email Sequence to Webinar | Does the webinar invitation match the email narrative? |
| Webinar to Sales Page | Does the sales page match the webinar offer exactly? |
| Sales Page to Purchase | Are pricing, bonuses, and guarantee identical? |
| Purchase to Onboarding | Does onboarding deliver on the purchase promise? |

### Phase 5: Produce Audit Report

```markdown
## FL3 FUNNEL AUDIT REPORT

**Date:** [Date]
**Funnel Version:** [Description]

### FUNNEL MAP
[Visual map from Phase 2]

### STAGE-BY-STAGE SCORES

| Stage | Reveal | Voice | Avatar | Continuity | Compliance | Overall |
|-------|--------|-------|--------|------------|------------|---------|
| Ads | X/10 | X/10 | X/10 | X/10 | X/10 | X/50 |
| Landing Page | X/10 | X/10 | X/10 | X/10 | X/10 | X/50 |
| Lead Magnet | X/10 | X/10 | X/10 | X/10 | X/10 | X/50 |
| Email Seq | X/10 | X/10 | X/10 | X/10 | X/10 | X/50 |
| Webinar | X/10 | X/10 | X/10 | X/10 | X/10 | X/50 |
| Sales Page | X/10 | X/10 | X/10 | X/10 | X/10 | X/50 |
| Onboarding | X/10 | X/10 | X/10 | X/10 | X/10 | X/50 |
| **TOTAL** | | | | | | **X/350** |

### TRANSITION GAPS
| Transition | Status | Issue | Fix |
|---|---|---|---|
| Ad → Landing | [OK/GAP] | [Description] | [Recommendation] |
[...]

### CRITICAL ISSUES (Fix Before Launch)
1. [Issue + specific fix]

### WARNINGS (Should Fix)
1. [Issue + specific fix]

### OPPORTUNITIES (Could Improve)
1. [Suggestion]

### OVERALL FUNNEL HEALTH: [READY / NEEDS WORK / NOT READY]
```

Save to `reports/`

## Quality Standards

**Maintain:**
- Honest, unflinching assessment
- Specific, actionable fixes for every issue
- Visual funnel mapping
- Transition-focused analysis (that's where funnels leak)

**Avoid:**
- Surface-level reviews that miss the transitions
- Vague recommendations ("improve the copy")
- Ignoring compliance in favor of conversion
- Only checking assets without checking the journey

## Reference Documents

- All FL3 funnel assets (ads, landing pages, emails, webinar, sales page)
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
- `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`

---

*FL3 Funnel Audit - Find the Leaks Before They Cost You v1.0.0*
*"The funnel is one conversation. Make sure it flows."*
