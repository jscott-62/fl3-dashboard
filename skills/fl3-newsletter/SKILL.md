---
name: fl3-newsletter
description: Beehiiv newsletter creator for Freedom Life 3.0. Produces story-driven weekly newsletters with subject line options, preview text, body, and CTA. Ties into the week's YouTube and blog content.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 3
  updated: 2026-02-13
---

# FL3 Newsletter - Beehiiv Weekly Newsletter Creator

Produces a story-driven weekly newsletter for the Freedom Life 3.0 Beehiiv audience. Each newsletter opens with a personal story or insight, delivers value, and links to the week's YouTube video and blog post.

## When to Use This Skill

- Weekly newsletter creation (every Thursday)
- Standalone broadcast email to the list
- Special announcements (course launch, events, milestones)
- When the Content Director agent needs the weekly newsletter

## Core Principles

1. **Newsletters are personal letters, not broadcasts.** Write like Scott is writing to one person over coffee.
2. **Story first, link second.** The newsletter itself must deliver value. The YouTube/blog links are "want more?" not "here's the real content."
3. **Subject lines are open-or-delete decisions.** Spend as much time on the subject line as on the first paragraph. Test 3 options.
4. **One primary CTA.** Reply, click a link, or DM. One thing.

## Complete Workflow

### Phase 1: Load Context

1. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`
2. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
3. This week's YouTube script and blog post (if available)

### Phase 2: Check for Weekly Brief

**Always check for a brief first.** Look in `Weekly-Content/Briefs/` for a file matching this week's date.

- **If a brief exists:** Use its angle, key points, avatar hook, stats, CTA, tone, and "Do NOT say" as the master control for this newsletter. The brief overrides any conflicting parameters passed in.
- **If no brief exists:** Accept parameters as below and proceed normally.

### Phase 3: Accept Parameters

1. **Content context:** Weekly brief, this week's topic, YouTube video link, blog post link
2. **Newsletter type:** Weekly regular, launch announcement, special broadcast
3. **Target avatar:** Primary avatar for this week (or All) (brief overrides if present)

### Phase 4: Write the Newsletter

```markdown
## FL3 NEWSLETTER: [Date]

**Subject Line Options:**
1. [Option A - Curiosity gap]
2. [Option B - Direct value]
3. [Option C - Personal/story hook]

**Preview Text:** [First line visible in inbox - make it compelling]

---

**Body:**

[Personal opening: 2-3 sentences. A story, observation, or reflection from Scott's week. Must feel authentic and unscripted.]

[Transition to this week's topic. Natural bridge from personal to educational.]

[Core insight: 3-5 paragraphs delivering the main value of this newsletter. Teach something. Share data. Challenge a belief.]

[Link to YouTube video: "I went deeper on this in this week's video: [link]"]

[Link to blog post: "If you prefer reading, I wrote about this here: [link]"]

[Closing: Personal sign-off. Something warm, motivating, or thought-provoking.]

[CTA: One clear action. Reply, click, share.]

Stay the course. Sleep well. Relax.

J. Scott

**P.S.** [Strategic P.S. line. Often the most-read part of an email.]

---

*This is an educational newsletter. Nothing here is financial advice. Past performance does not guarantee future results.*
```

### Phase 5: Quality Gates

1. Run `fl3-voice-check`
2. Run `fl3-compliance-check`
3. Verify 3 subject line options
4. Verify one clear CTA
5. Verify links to YouTube/blog are included
6. Verify disclaimer is present
7. Save to `Weekly-Content/Email/`

## Quality Standards

**Maintain:** Personal letter tone. Story-driven opening. Value-first content. One CTA. P.S. line.

**Avoid:** Corporate newsletter voice. Multiple CTAs. Missing subject line options. Hard selling. Em dashes.

---

*FL3 Newsletter - Personal Letters That Build Trust v1.0.0*
