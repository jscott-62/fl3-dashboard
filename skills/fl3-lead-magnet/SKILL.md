---
name: fl3-lead-magnet
description: Lead magnet creation system for Freedom Life 3.0. Designs and writes complete lead magnets including content, landing page copy, thank-you page, and follow-up email sequence.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 5
  updated: 2026-02-13
---

# FL3 Lead Magnet - Complete Lead Magnet Package Creator

Designs and writes complete lead magnets for FL3 including the content itself, landing page copy, thank-you page copy, and the follow-up email sequence. Uses the existing Wrong Asset Manifesto as a reference for what works.

## When to Use This Skill

- Creating a new lead magnet for a different avatar or angle
- Refreshing the existing Wrong Asset Manifesto
- Building a calculator, checklist, or mini-course as a lead magnet
- Testing a new top-of-funnel offer

## Core Principles

1. **The lead magnet IS the first impression.** It sets expectations for everything that follows. If it's high quality, the audience trusts the paid offer will be even better.
2. **Teach something real.** Don't create thin content that's just a pitch in disguise. Give genuine value that creates the "if the free stuff is this good..." reaction.
3. **The Reveal Sequence starts here.** Most lead magnets are awareness-stage. Bitcoin is teased, not named. The lead magnet earns the right for the email sequence to reveal.
4. **Match the lead magnet to the avatar.** Technophobe needs simplicity (checklist, calculator). Pursuer needs action steps (action plan). Skeptic needs data (manifesto, report).

## Complete Workflow

### Phase 1: Load Context

1. `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/` (existing lead magnet reference)
2. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
3. `Main/Zenith Avatars/` (avatar profiles)
4. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`

### Phase 2: Design the Lead Magnet

Accept parameters:
1. **Target avatar:** Which avatar is this optimized for?
2. **Lead magnet type:** Manifesto, checklist, calculator guide, mini-course, report, cheat sheet
3. **Core promise:** What will the reader gain?
4. **Reveal stage:** How far along the Reveal Sequence does this go?

### Phase 3: Produce the Package

**Component 1: Lead Magnet Content**
- Write the actual lead magnet (manifesto, checklist, etc.)
- 8-15 pages of genuine value
- Follow FL3 content framework (pain, system blame, opportunity, action)
- Respect Reveal Sequence stage

**Component 2: Landing Page Copy**
- Headline + sub-headline
- 3-5 bullet points of what they'll learn
- Social proof (if available)
- Opt-in form CTA
- Can delegate to Copy Arsenal for maximum conversion

**Component 3: Thank-You Page Copy**
- Delivery confirmation
- "While you wait" next step (watch a video, join the community)
- Sets expectations for the email sequence

**Component 4: Follow-Up Email Sequence**
- Call `/fl3-email-sequence` with type "lead magnet follow-up"
- 7 emails over 14 days
- Follows the Reveal Sequence from awareness to education

### Phase 4: Quality Gates

1. Run `fl3-voice-check` on all components
2. Run `fl3-compliance-check` on all components
3. Verify Reveal Sequence consistency across the entire package
4. Save to `Projects/The-Great-Catch-Up/` or designated subfolder

## Reference Documents

- `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/` (all files)
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
- `Main/Zenith Avatars/`

---

*FL3 Lead Magnet - First Impressions That Convert v1.0.0*
