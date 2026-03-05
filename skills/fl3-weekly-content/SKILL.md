---
name: fl3-weekly-content
description: Weekly content orchestrator for Freedom Life 3.0. Takes the weekly YouTube digest and produces a complete content package (YouTube script, blog post, social posts, newsletter) through the content pipeline.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 6
  element_skills: 5
  updated: 2026-02-13
---

# FL3 Weekly Content - Complete Weekly Content Package

The primary weekly workflow. Takes the latest YouTube digest and produces a complete, reviewed content package: YouTube script, companion blog post, social media batch, and newsletter. All in Scott's voice, all targeting the right avatar, all mapped to the content calendar.

## When to Use This Skill

- Every week after the YouTube digest is generated (typically Monday)
- When you want the full weekly content package in one command
- When the Content Director agent runs the weekly pipeline

**For individual pieces:** Use the specific skill (`/fl3-youtube`, `/fl3-blog`, `/fl3-social`, `/fl3-newsletter`) instead.

## Core Principles

1. **One theme, multiple formats.** The week's content should tell one cohesive story across all platforms.
2. **YouTube is the anchor.** The YouTube script is created first. Blog, social, and newsletter derive from it.
3. **Platform adaptation, not copying.** Each format is purpose-built for its platform. The blog is not a transcript. Social posts are not blog excerpts.
4. **Quality gates are mandatory.** Every piece passes voice and compliance checks before delivery.

## Element Skills Called

This orchestrator calls these skills in sequence:

1. `fl3-youtube-script` - YouTube script from the topic
2. `fl3-blog-post` - Companion blog post from the script
3. `fl3-social-batch` - Platform-specific social posts from the content
4. `fl3-newsletter` - Weekly newsletter tying everything together
5. `fl3-voice-check` - Quality validation on all outputs

## Complete Workflow

### Phase 1: Check for Weekly Brief

**Always check for a brief first.** The brief is the single source of truth for the week's content.

1. Look for a brief at `Weekly-Content/Briefs/[YYYY-MM-DD] - [Topic].md` matching this week's date
2. **If a brief exists:** Read it completely. Use its angle, key points, avatar hook, stats, CTA, tone notes, and "Do NOT say" list as the master control for ALL content produced. Skip Phase 2 (Topic Selection) entirely.
3. **If no brief exists:** Draft one from the digest/calendar/topic, save it to `Weekly-Content/Briefs/`, then proceed. The brief template is at `Weekly-Content/Briefs/_BRIEF-TEMPLATE.md`.

### Phase 2: Intake (only if no brief exists)

1. Read latest YouTube digest from `Reports/Weekly YouTube Digest *.md`
   (Or accept a specific topic if not using the digest)
2. Read content calendar (`calendar/content-calendar.md`) to determine:
   - This week's pillar focus
   - This week's avatar rotation
   - Any special events or launch activities
3. Load Voice DNA and business context

### Phase 3: Topic Selection (only if no brief exists)

1. If using the digest, identify the 1-2 strongest topics that:
   - Align with this week's pillar focus
   - Can be framed through the target avatar's lens
   - Are timely and relevant
   - Build toward course purchase (if in pre-launch or launch window)
2. Select primary topic and framing angle
3. Determine funnel stage (awareness, education, implementation)
4. **Create the brief** from this selection and save to `Weekly-Content/Briefs/`

### Phase 4: Content Production Pipeline

Execute in this order (each output feeds the next). **Pass the brief to each skill.**

**Step 1:** Call `/fl3-youtube-script` with:
- Selected topic
- Target avatar
- Pillar alignment
- Funnel stage
- Standard length (14-18 min)

**Step 2:** Call `/fl3-blog-post` with:
- YouTube script as source
- Same avatar and pillar
- Primary keyword for SEO

**Step 3:** Call `/fl3-social-batch` with:
- Blog post as source
- All platforms (IG, LinkedIn, FB)
- 2-3 posts per platform

**Step 4:** Call `/fl3-newsletter` with:
- This week's topic
- YouTube video and blog post links
- Same avatar focus

### Phase 5: Quality Review

1. Run `/fl3-voice-check` on all 4 outputs
2. Run `/fl3-compliance-check` on all 4 outputs
3. If any piece scores below 56/70 on voice check, revise before delivery
4. If any CRITICAL compliance issue, fix immediately

### Phase 6: Delivery and Calendar Update

1. Save all outputs to their respective directories:
   - YouTube script: `Weekly-Content/YouTube/[date]-[title].md`
   - Blog post: `Weekly-Content/Articles/[date]-[title].md`
   - Social batch: `Weekly-Content/Social Media/[date]-batch.md`
   - Newsletter: `Weekly-Content/Email/[date]-newsletter.md`
2. Update `calendar/content-calendar.md` with new entries
3. Produce weekly content summary:

```markdown
## WEEKLY CONTENT SUMMARY: [Date]

**Theme:** [This week's topic]
**Pillar:** [#] [Name]
**Avatar:** [Target avatar]
**Funnel Stage:** [Stage]

### PRODUCED
| Asset | File | Voice Score | Compliance |
|-------|------|-------------|------------|
| YouTube Script | [path] | [X/70] | [Cleared] |
| Blog Post | [path] | [X/70] | [Cleared] |
| Social Batch ([N] posts) | [path] | [X/70] | [Cleared] |
| Newsletter | [path] | [X/70] | [Cleared] |

### PUBLISHING SCHEDULE
| Day | Platform | Asset | Status |
|-----|----------|-------|--------|
| Tue | YouTube | Script recorded + uploaded | Pending |
| Tue | Blog | Post published | Pending |
| Wed | Instagram | Post 1 | Pending |
| Wed | LinkedIn | Post 1 | Pending |
| Thu | Newsletter | Email sent | Pending |
| Fri | Facebook | Post 1 | Pending |
| Sat | Instagram | Post 2 | Pending |

### SCOTT'S ACTION ITEMS
1. [ ] Record YouTube video from script
2. [ ] Review and publish blog post
3. [ ] Schedule social posts
4. [ ] Send newsletter via Beehiiv
```

## Quality Standards

**Maintain:** Cohesive weekly theme. Platform-appropriate adaptation. All pieces pass quality gates. Content calendar updated.

**Avoid:** Disconnected content across platforms. Skipping quality gates. Transcript-as-blog-post. Missing calendar updates.

## Reference Documents

All documents referenced by the element skills, plus:
- `calendar/content-calendar.md`
- Latest YouTube digest in `Reports/`

---

*FL3 Weekly Content - The Content Machine v1.0.0*
*"One theme. Every platform. Every week. Like clockwork."*
