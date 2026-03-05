---
name: fl3-content-calendar
description: Content calendar manager for Freedom Life 3.0. Plans, updates, and maintains the master content calendar with pillar rotation, avatar targeting, and launch window integration.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-business-operations
  framework_count: 3
  updated: 2026-02-13
---

# FL3 Content Calendar - Master Calendar Manager

Plans, updates, and maintains the master FL3 content calendar. Ensures healthy rotation across the 4 Pillars and 3 Avatars, accounts for launch windows, and tracks content status from planned through published.

## When to Use This Skill

- Weekly: Update with this week's content and plan next week
- Monthly: Plan the full month ahead
- Quarterly: Strategic content planning session
- Before a launch: Insert launch content into the calendar
- When checking what's coming up

## Core Principles

1. **Pillar rotation prevents monotony.** Don't hit the same pillar 3 weeks in a row. Rotate across Math, Traditional Advice, Better Vehicles, and Risk Flip.
2. **Avatar rotation ensures reach.** Each avatar needs to see themselves in the content at least once per month.
3. **Launch windows override rotation.** During a launch, all content points toward the offer. Normal rotation resumes after.
4. **The calendar is the source of truth.** If it's not on the calendar, it doesn't exist.

## Complete Workflow

### Phase 1: Read Current State

Read `calendar/content-calendar.md` to understand:
- What's been published recently
- What's scheduled upcoming
- Which pillars and avatars have been covered
- Any gaps or imbalances

### Phase 2: Accept Planning Parameters

1. **Planning horizon:** 1 week, 1 month, or 1 quarter
2. **Launch windows:** Any upcoming launches to account for?
3. **Special events:** Bitcoin halving, market events, holidays, etc.
4. **Topic preferences:** Any specific topics Scott wants covered?

### Phase 3: Generate Calendar

Apply content mix rules:

**Pillar Rotation (monthly cycle):**
- Week 1: Pillar 1 (The Math Doesn't Work)
- Week 2: Pillar 3 (Better Vehicles Exist)
- Week 3: Pillar 2 (Traditional Advice Fails)
- Week 4: Pillar 4 (Risk Flipped)

**Avatar Rotation (monthly cycle):**
- Week 1: Silent Technophobe
- Week 2: Awakened Skeptic
- Week 3: Paralyzed Pursuer
- Week 4: All (universal content)

**Funnel Stage Balance (monthly):**
- 2 weeks: Awareness content (broad reach)
- 1 week: Education content (deeper engagement)
- 1 week: Implementation content (action-oriented)

### Phase 4: Update Calendar File

Calendar format:

```markdown
# FL3 Content Calendar

## [Month Year]

| Week | Date | Pillar | Avatar | Topic | YouTube | Blog | Social | Email | Status |
|------|------|--------|--------|-------|---------|------|--------|-------|--------|
| 1 | [Date] | 1: Math | Technophobe | [Topic] | [link] | [link] | [count] | [type] | [Status] |
| 2 | [Date] | 3: Vehicles | Skeptic | [Topic] | [link] | [link] | [count] | [type] | [Status] |
| 3 | [Date] | 2: Trad Advice | Pursuer | [Topic] | [link] | [link] | [count] | [type] | [Status] |
| 4 | [Date] | 4: Risk Flip | All | [Topic] | [link] | [link] | [count] | [type] | [Status] |

### Status Legend
- Planned: Topic selected, not yet produced
- Drafted: Content produced, not yet reviewed
- Reviewed: Passed quality gates
- Published: Live on platform
- Archived: Moved to archive

### Launch Windows
- [Date range]: [Launch name] - all content supports launch
```

### Phase 5: Archive and Maintain

1. Move completed months to `calendar/content-calendar-archive.md`
2. Flag any gaps (missed weeks, imbalanced rotations)
3. Update idea bank with unused topics

Save to `calendar/content-calendar.md`

## Reference Documents

- `calendar/content-calendar.md` (current calendar)
- `calendar/idea-bank.md` (topic queue)
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` (pillar definitions)

---

*FL3 Content Calendar - Strategic Consistency v1.0.0*
