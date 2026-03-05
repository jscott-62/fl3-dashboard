---
name: fl3-voice-check
description: Voice consistency validator for all Freedom Life 3.0 content. Scores content against Scott MacMillan's Voice DNA, flags anti-pattern violations, and ensures avatar alignment.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-quality-control
  framework_count: 7
  updated: 2026-02-13
---

# FL3 Voice Check - Content Voice Validator

Validates any piece of FL3 content against Scott MacMillan's authenticated Voice DNA. Produces a scorecard with specific line-by-line fixes. This is the quality gate that every piece of FL3 content must pass before publishing.

## When to Use This Skill

- Before publishing ANY FL3 content (YouTube, blog, social, email, ads)
- After generating content with any other FL3 skill
- When reviewing content written by others (ghostwriters, contractors)
- When the Brand Guardian agent runs its quality check pipeline
- To train yourself on what "sounds like Scott" vs. what doesn't

**This skill does NOT create content.** It only evaluates and fixes existing content.

## Core Principles

1. **Voice is non-negotiable.** Every piece of FL3 content must sound like Scott wrote it. Not "professional copywriter." Not "generic financial educator." Scott.
2. **Anti-patterns are instant flags.** Em dashes, hype language, blame, jargon, and condescension are immediate violations regardless of how good the content otherwise is.
3. **Platform context matters.** Instagram Scott is slightly more casual than LinkedIn Scott. YouTube Scott is more educational. But the core voice DNA is identical.
4. **Avatar alignment is voice.** Speaking to the Silent Technophobe requires simpler language and more reassurance than speaking to the Awakened Skeptic. Mismatched complexity is a voice failure.
5. **Signature phrases are anchors.** Using Scott's phrases ("You did everything right. And you're still behind." / "The vehicle matters more than the time." / "Stay the course. Sleep well. Relax.") appropriately is a positive signal. Overusing or misusing them is a negative.

## Complete Workflow

### Phase 1: Load Voice DNA

Load these reference documents before evaluating:

1. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md` (primary voice patterns)
2. `Main/Scott MacMillan Voice DNA/Voice DNA/07-CORE-PHILOSOPHY.md` (philosophical alignment)
3. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` (messaging framework)
4. `Main/CLAUDE.md` (writing style rules, especially no em dashes)

### Phase 2: Accept and Classify Content

1. Accept content to review (file path or pasted text)
2. Identify content type: YouTube script, blog post, social post, email, ad, sales page, other
3. Identify target platform: Instagram, LinkedIn, Facebook, YouTube, Email, Website
4. Identify target avatar (if specified): Silent Technophobe, Paralyzed Pursuer, Awakened Skeptic, All
5. Identify funnel stage: Awareness (pre-Bitcoin), Education (Bitcoin introduced), Implementation, Conversion

### Phase 3: Score Against 7 Voice Dimensions

Score each dimension 1-10 and provide specific evidence:

**Dimension 1: Tone Accuracy (Calm Authority + Empathetic Challenger)**
- Does it speak from experience without bragging?
- Is it reassuring without being naive?
- Does it validate before challenging?
- Score 1-10

**Dimension 2: Anti-Pattern Violations**
- Count all em dashes (should be ZERO)
- Count hype language ("to the moon," "massive gains," "life-changing," "incredible")
- Count blame language (making the reader feel at fault)
- Count jargon overload (unexplained technical terms)
- Count condescension ("it's simple," "anyone can do this," "obviously")
- Each violation listed with line reference
- Score: 10 minus (violation count), minimum 1

**Dimension 3: Sentence Structure**
- Does it use short, punchy sentences for impact?
- Does it use fragments for emphasis?
- Does it use the three-beat rhythm pattern?
- Does it open with pain-first hooks or validation?
- Score 1-10

**Dimension 4: Language Ratio (85% Toward / 15% Away)**
- Count toward-language instances (BUILD, ACHIEVE, CREATE, DEVELOP, BECOME, DISCOVER)
- Count away-language instances (STOP, LOSE, STEAL, FAIL, MISS)
- Calculate ratio
- Away language should appear ONLY in problem amplification, never in CTAs or offer descriptions
- Score 1-10

**Dimension 5: Signature Phrase Usage**
- Are signature phrases used? Which ones?
- Are they used in appropriate context?
- Are they overused (more than 2 per 500 words)?
- Score 1-10

**Dimension 6: Platform Fit**
- Does the tone match the target platform?
- Instagram: shorter, punchier, hashtags, DM CTA
- LinkedIn: polished, paragraph structure, professional
- Facebook: conversational, community-focused
- YouTube: educational framing, step-by-step
- Email: personal, story-driven, single CTA
- Score 1-10

**Dimension 7: Avatar Alignment**
- Does the complexity match the target avatar?
- Silent Technophobe: simplest language, most reassurance, "no tech required" framing
- Paralyzed Pursuer: action-oriented, deadline-driven, "done is better than perfect"
- Awakened Skeptic: data-driven, validates their worldview, "you were right"
- If no avatar specified, check that it works for all three
- Score 1-10

### Phase 4: Produce Scorecard

Output format:

```markdown
## FL3 VOICE CHECK SCORECARD

**Content:** [Title or first 20 words]
**Type:** [YouTube/Blog/Social/Email/Ad/Sales Page]
**Platform:** [IG/LinkedIn/FB/YouTube/Email/Website]
**Target Avatar:** [Technophobe/Pursuer/Skeptic/All]
**Funnel Stage:** [Awareness/Education/Implementation/Conversion]

### SCORES

| Dimension | Score | Notes |
|-----------|-------|-------|
| 1. Tone Accuracy | X/10 | [Brief note] |
| 2. Anti-Pattern Violations | X/10 | [Count of violations] |
| 3. Sentence Structure | X/10 | [Brief note] |
| 4. Language Ratio | X/10 | [Actual ratio] |
| 5. Signature Phrases | X/10 | [Which used, appropriately?] |
| 6. Platform Fit | X/10 | [Brief note] |
| 7. Avatar Alignment | X/10 | [Brief note] |
| **OVERALL** | **X/70** | **[PASS/NEEDS REVISION/FAIL]** |

### THRESHOLD
- 56-70 (80%+): PASS - Ready to publish
- 42-55 (60-79%): NEEDS REVISION - Fix flagged issues
- Below 42 (<60%): FAIL - Significant rewrite needed

### VIOLATIONS (if any)

| Line | Issue | Fix |
|------|-------|-----|
| [#] | [What's wrong] | [Specific replacement] |

### RECOMMENDATIONS

[2-5 specific, actionable recommendations]
```

### Phase 5: Apply Fixes (Optional)

If requested, apply all recommended fixes and save the corrected version:

1. Replace all em dashes with appropriate alternatives (periods, commas, colons, parentheses)
2. Replace hype language with calm authority alternatives
3. Replace blame language with validation language
4. Simplify jargon for target avatar
5. Adjust language ratio if off-target
6. Save corrected version alongside original

## Quality Standards

**Maintain:**
- Honest assessment (don't inflate scores)
- Specific, actionable fixes (not vague "improve tone")
- Line-level references for every violation
- Respect for Scott's authentic voice (don't over-polish into generic)

**Avoid:**
- Passing content with em dashes (automatic dimension 2 penalty)
- Ignoring platform context (LinkedIn post shouldn't read like Instagram)
- Over-correcting personality out of the content
- Flagging Scott's authentic phrases as violations

## Common Mistakes to Avoid

1. **Don't confuse "professional" with "Scott."** Scott is professional but also uses fragments, rhetorical questions, and personal stories. Generic professional copy fails the voice check.
2. **Don't miss hidden em dashes.** They sometimes appear as two hyphens (--) or in pasted content. All forms are violations.
3. **Don't penalize strategic away-language.** "Money printing that's been stealing your retirement" is intentional and correct in problem amplification sections.
4. **Don't require signature phrases in every piece.** They should appear naturally, not forced. A post without any is fine if the overall voice is right.
5. **Don't ignore the Reveal Sequence.** If content is awareness-stage but mentions Bitcoin by name, that's a compliance issue for the compliance-check skill, not a voice issue. But note it.

## Reference Documents

- `Main/Scott MacMillan Voice DNA/Voice DNA/` (all 7 files)
- `Main/CLAUDE.md` (style rules)
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`

---

*FL3 Voice Check - Quality Gate v1.0.0*
*Every word represents the brand. Every word must sound like Scott.*
