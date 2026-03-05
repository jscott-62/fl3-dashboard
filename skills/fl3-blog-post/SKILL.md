---
name: fl3-blog-post
description: SEO-optimized blog post generator for Freedom Life 3.0. Creates long-form articles in Scott's voice from topics, YouTube scripts, or digest insights. Includes meta descriptions, title tags, and internal linking.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 4
  updated: 2026-02-13
---

# FL3 Blog Post - SEO-Optimized Article Generator

Creates long-form blog posts (1,200-2,000 words) for freedomlife3.com in Scott's voice. Can convert YouTube scripts to blog format, generate from digest insights, or create standalone articles. Includes SEO elements.

## When to Use This Skill

- Creating a companion blog post for a YouTube video
- Writing a standalone article on an FL3 topic
- Converting digest insights into written content
- When the Content Director agent needs weekly blog content

## Core Principles

1. **Blog posts are not transcripts.** A YouTube companion post should cover the same topic but be written for readers, not viewers. Different structure, different pacing.
2. **SEO matters for discovery.** Use keyword-rich headlines, meta descriptions, and structured content that Google can index.
3. **The FL3 content framework applies.** Pain validation, system blame, opportunity, action. Every post follows this arc.
4. **One primary keyword, 2-3 secondary keywords.** Each post should target a specific search query.

## Complete Workflow

### Phase 1: Load Context

1. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`
2. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
3. `Main/FL3 ZenithPro Data/FL3 Business Brief.md`

### Phase 2: Check for Weekly Brief

**Always check for a brief first.** Look in `Weekly-Content/Briefs/` for a file matching this week's date.

- **If a brief exists:** Use its angle, key points, avatar hook, stats, CTA, tone, and "Do NOT say" as the master control for this article. The brief overrides any conflicting parameters passed in.
- **If no brief exists:** Accept parameters as below and proceed normally.

### Phase 3: Accept Post Parameters

1. **Source:** Weekly brief, YouTube script to convert, topic, digest excerpt, or idea bank
2. **Target avatar:** Technophobe, Pursuer, Skeptic, or All (brief overrides if present)
3. **FL3 Pillar:** Which pillar does this reinforce? (brief overrides if present)
4. **Primary keyword:** The main search term to target
5. **Funnel stage:** Awareness, Education, or Implementation (brief overrides if present)

### Phase 4: Write the Post

```markdown
# [H1: Post Title (with primary keyword)]

**Meta Description:** [155 characters, includes keyword, compelling]
**Primary Keyword:** [target keyword]
**Secondary Keywords:** [2-3 related terms]
**Target Avatar:** [Avatar]
**Pillar:** [1-4]

---

[Opening paragraph: Pain validation or hook that pulls the reader in. Establish "I've been there" credibility within the first 3 sentences.]

## [H2: Section 1 - The Problem] (keyword-rich heading)

[Explain why the traditional approach fails. Use data. Validate the reader's frustration.]

## [H2: Section 2 - Why It Failed]

[Go deeper on the system failure. Money printing, inflation, wrong assets. Build righteous anger.]

## [H2: Section 3 - The Opportunity]

[Introduce the alternative. Follow Reveal Sequence rules for the funnel stage.]

## [H2: Section 4 - The Path Forward]

[Show what action looks like. Make it feel achievable.]

## [H2: What This Means for You]

[Personal application. "If you're [age] and you have [amount]..." Make it real.]

---

**CTA:** [Single clear call to action: free resource, newsletter signup, calculator]

**Internal Links:** [Link to 2-3 related posts/pages on freedomlife3.com]

**Disclaimer:** *This content is for educational purposes only and does not constitute financial advice.*
```

### Phase 5: Quality Gates

1. Run `fl3-voice-check`
2. Run `fl3-compliance-check`
3. Verify word count (1,200-2,000 words)
4. Verify H2/H3 structure for SEO
5. Verify meta description under 155 characters
6. Verify one clear CTA
7. Save to `Weekly-Content/Articles/`

## Quality Standards

**Maintain:** Scott's written voice (slightly more polished than spoken, but same DNA). Data-driven arguments. Structured H2/H3 headings. One CTA per post.

**Avoid:** Keyword stuffing. Generic financial advice tone. Missing meta descriptions. Multiple CTAs. Em dashes.

## Reference Documents

- `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`

---

*FL3 Blog Post - Written Content That Ranks and Converts v1.0.0*
