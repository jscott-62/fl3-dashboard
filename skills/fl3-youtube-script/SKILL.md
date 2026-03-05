---
name: fl3-youtube-script
description: YouTube script generator for Freedom Life 3.0. Produces full camera-ready scripts in Scott's voice with hooks, sections, graphics cues, and CTAs. Follows the exact format of existing FL3 video scripts.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 5
  updated: 2026-02-13
---

# FL3 YouTube Script - Camera-Ready Script Generator

Produces full, camera-ready YouTube scripts in Scott MacMillan's voice. Each script is 14-20 minutes of spoken content with hook, educational sections, personal story segment, graphics cues, and CTA. Follows the exact format of existing FL3 video scripts.

## When to Use This Skill

- Creating a standalone YouTube video on a specific topic
- When the weekly content workflow needs a YouTube script
- Converting a blog post or newsletter topic into video format
- Creating a video series on a specific theme
- When the Content Director agent needs a weekly YouTube script

## Core Principles

1. **Hook in the first 15 seconds.** YouTube retention drops fast. Open with a statement that makes the viewer think "that's me" or "wait, what?"
2. **Teach, don't pitch.** FL3 YouTube videos are educational. The pitch is subtle: "want to learn more? Link in description." Never hard-sell on camera.
3. **One big idea per video.** Each video should deliver ONE clear takeaway. Multiple big ideas dilute retention.
4. **Sarah IS the viewer.** Use Sarah's story from the course to create identification. "If you're like Sarah..." or weave her situation into the educational content.
5. **Graphics cues are essential.** Scott records to camera with supporting graphics. Every data point, chart, or comparison needs a [GRAPHIC:] cue in the script.

## Complete Workflow

### Phase 1: Load Context

1. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md` (voice)
2. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` (business)
3. `Main/FL3 ZenithPro Data/FL3 Business Brief.md` (4 Pillars)
4. `Main/FL3 ZenithPro Data/SILENT TECHNOPHOBE - Content Ecosystem Architecture v2.0.md` (epiphany units)

### Phase 2: Accept Video Parameters

1. **Topic:** The main subject of the video
2. **Source:** YouTube digest insight, blog post conversion, standalone topic, or idea bank
3. **Target avatar:** Technophobe, Pursuer, Skeptic, or All
4. **FL3 Pillar:** Which of the 4 Pillars does this reinforce?
5. **Funnel stage:** Awareness (no Bitcoin), Education (Bitcoin named), Implementation
6. **Target length:** Short (8-10 min), Standard (14-18 min), Long (20-25 min)

### Phase 3: Write the Script

Follow this structure:

```markdown
# [VIDEO TITLE]

## Target: [Avatar] | Pillar: [#] | Stage: [Awareness/Education/Implementation]
## Estimated Length: [X] minutes

---

## HOOK (0:00 - 0:45)

[Opening statement that creates immediate identification or curiosity]

[GRAPHIC: Title card with video title]

[Bridge to the main topic. Why this matters to them specifically.]

---

## SECTION 1: [Section Title] (0:45 - X:XX)

[Educational content. One sub-topic per section.]

[GRAPHIC: Chart/data/comparison supporting the point]

[Personal story or Sarah story that illustrates the point]

---

## SECTION 2: [Section Title] (X:XX - X:XX)

[Continue educational content]

[GRAPHIC: Supporting visual]

---

## SECTION 3: [Section Title] (X:XX - X:XX)

[Continue. 3-5 sections depending on length.]

---

## PERSONAL STORY SEGMENT (X:XX - X:XX)

[Scott's personal experience related to the topic]
[This is where authenticity lives. Real stories, real numbers, real feelings.]

---

## WRAP-UP + CTA (X:XX - End)

[Summarize the one big takeaway]

[CTA: What to do next]
- Subscribe and hit the bell
- Link to [lead magnet/free resource] in the description
- Comment [keyword] to get [specific resource]

[GRAPHIC: End screen with subscribe button and related video]

---

## DESCRIPTION BOX

**Title:** [SEO-optimized title]
**Description:**
[3-5 line description with keywords]

**Timestamps:**
0:00 - [Hook]
X:XX - [Section 1 title]
[...]

**Links:**
- [Lead magnet link]
- [Website link]
- [Social links]

**Disclaimer:** This video is for educational purposes only and is not financial advice. Past performance does not guarantee future results. Always consult a qualified financial advisor for personalized advice.

**Tags:** [10-15 relevant tags]
```

### Phase 4: Quality Gates

1. Run `fl3-voice-check` on the script
2. Run `fl3-compliance-check` on the script
3. Verify hook is in the first 15 seconds of spoken content
4. Verify at least 3 [GRAPHIC:] cues for visual editors
5. Verify disclaimer is in description
6. Verify Reveal Sequence is respected for the video's funnel stage
7. Save to `Weekly-Content/YouTube/`

## Quality Standards

**Maintain:**
- Scott's spoken voice (conversational, not written-sounding)
- One big takeaway per video
- Graphics cues for every data point
- Hook within 15 seconds
- Educational framing throughout
- Personal/Sarah stories for identification

**Avoid:**
- Reading-voice writing (it should sound natural when spoken aloud)
- Multiple CTAs (one clear next step)
- Hard selling or pitching within the video
- Hype language
- Em dashes (they don't translate to speech anyway)
- Missing timestamps in description

## Common Mistakes to Avoid

1. **Don't write for reading, write for speaking.** Read the script aloud. If it sounds stiff, it needs rewriting. Scott speaks in fragments and pauses.
2. **Don't bury the hook.** The first sentence out of Scott's mouth should make the viewer stop scrolling.
3. **Don't skip the personal story.** It's what differentiates FL3 content from generic financial education.
4. **Don't forget SEO.** Title, description, tags, and timestamps matter for YouTube discovery.
5. **Don't make the CTA complicated.** "Link in the description" or "comment RETIRE" are clear. Don't stack 5 CTAs.

## Reference Documents

- `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
- `Main/FL3 ZenithPro Data/SILENT TECHNOPHOBE - Content Ecosystem Architecture v2.0.md` (epiphany units for topic ideas)
- Existing video scripts in the vault for format reference

---

*FL3 YouTube Script - Camera-Ready Content v1.0.0*
*"Hook them in 15 seconds. Teach them something real. Show them the path."*
