---
name: fl3-social-batch
description: Social media batch generator for Freedom Life 3.0. Creates platform-specific posts for Instagram, LinkedIn, and Facebook from a single content source. Adapts voice per platform.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 4
  updated: 2026-02-13
---

# FL3 Social Batch - Platform-Specific Social Media Generator

Creates 5-10 platform-specific social posts from a single content source. Adapts Scott's voice per platform: IG (short, punchy, hashtags), LinkedIn (polished, paragraph structure), FB (conversational, community).

## When to Use This Skill

- Creating a batch of social posts for the week
- Repurposing a YouTube video or blog post into social content
- Creating launch countdown social posts
- When the Content Director agent needs weekly social content

## Core Principles

1. **Platform-specific voice, same DNA.** IG Scott is punchier. LinkedIn Scott is more polished. Facebook Scott is more conversational. But all three are authentically Scott.
2. **One post, one idea.** Social posts should deliver one clear thought. Not a mini-blog.
3. **Engagement over broadcast.** Ask questions. Invite DMs. Spark conversation. Don't just announce.
4. **Hashtags are IG only.** LinkedIn uses 3-5 max. Facebook uses none.

## Complete Workflow

### Phase 1: Load Context

1. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md` (platform voice variations)
2. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`

### Phase 2: Check for Weekly Brief

**Always check for a brief first.** Look in `Weekly-Content/Briefs/` for a file matching this week's date.

- **If a brief exists:** Use its angle, key points, avatar hook, stats, CTA, tone, and "Do NOT say" as the master control for all social posts. The brief overrides any conflicting parameters passed in.
- **If no brief exists:** Accept parameters as below and proceed normally.

### Phase 3: Accept Parameters

1. **Content source:** Weekly brief, YouTube script, blog post, topic, or free-standing
2. **Target avatar:** Technophobe, Pursuer, Skeptic, or All (brief overrides if present)
3. **Platforms:** Instagram, LinkedIn, Facebook, or All
4. **Post count:** How many per platform (default: 2-3 per platform)
5. **Purpose:** Awareness, engagement, lead gen, launch promotion

### Phase 4: Generate Platform Posts

**Instagram Format:**
```markdown
## IG Post [#]: [Internal Name]

**Type:** [Quote card / Carousel concept / Hook post / Story series]

**Caption:**
[Short, punchy. 1-3 lines max for above the fold.]

[Optional: 1-2 more lines below the fold]

**CTA:** DM "[keyword]" for [resource]

**Hashtags:**
#RetirementCatchUp #FinancialFreedom #RetirementPlanning #BitcoinRetirement #InvestingTips #LateStart #SecondHalf #SmartMoney #Over50 #RetirementGoals

**Visual Concept:** [What the image/graphic should show]
```

**LinkedIn Format:**
```markdown
## LI Post [#]: [Internal Name]

[Opening line that stops the scroll. Short. Standalone.]

[Paragraph 2: The insight or story. 3-4 sentences.]

[Paragraph 3: The application or takeaway. 2-3 sentences.]

[CTA: Soft. "What do you think?" or "Share your experience."]

#RetirementPlanning #FinancialLiteracy #InvestingOverFifty
```

**Facebook Format:**
```markdown
## FB Post [#]: [Internal Name]

[Conversational opening. Like talking to a friend.]

[Story or insight. Natural, flowing tone.]

[Question to spark comments or shares.]

[Optional: Link to blog/YouTube]
```

### Phase 5: Quality Gates

1. Run `fl3-voice-check` on all posts
2. Verify platform-specific formatting
3. Verify hashtag usage matches platform norms
4. Verify Reveal Sequence compliance
5. Save to `Weekly-Content/Social Media/`

## Quality Standards

**Maintain:** Platform-specific voice. One idea per post. Engagement hooks. Scott's signature phrases where natural.

**Avoid:** Same copy across all platforms. Hashtags on Facebook. Long-form on Instagram. Hype language. Em dashes. Hard selling.

---

*FL3 Social Batch - Platform-Native Content at Scale v1.0.0*
