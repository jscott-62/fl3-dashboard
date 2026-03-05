---
name: fl3-email-sequence
description: Creates multi-email nurture and launch sequences for Freedom Life 3.0. Supports lead magnet follow-up, pre-launch warmup, launch, and post-purchase sequences. Respects the FL3 Reveal Sequence Strategy.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 8
  updated: 2026-02-13
---

# FL3 Email Sequence - Nurture and Launch Email System

Creates complete multi-email sequences for any stage of the FL3 funnel. Each email follows Scott's voice, targets the right avatar, and respects the Reveal Sequence Strategy (Bitcoin withheld in early emails, revealed progressively).

## When to Use This Skill

- Building a lead magnet follow-up sequence (after Wrong Asset Manifesto opt-in)
- Creating pre-launch warmup emails (before course cart opens)
- Writing the launch email sequence (cart open through cart close)
- Building post-purchase onboarding emails (after course purchase)
- Creating a re-engagement sequence for cold subscribers
- When the Launch Director or Content Director agent needs email content

**For elite email copy on critical sequences:** Delegate individual emails to Copy Arsenal's `/clayton-email` for maximum emotional resonance.

## Core Principles

1. **Every email has ONE job.** One belief shift. One action. One CTA. Don't try to do everything in one email.
2. **The Reveal Sequence is law.** Early emails (1-5 in a nurture sequence) build the problem and tease the solution without naming Bitcoin. The reveal happens deliberately, with reframing ready.
3. **Story-first, not pitch-first.** Scott's emails read like a personal letter from someone who's been there. They open with stories, not sales pitches.
4. **Subject lines are the whole game.** If they don't open, nothing else matters. Use FL3 signature phrases, curiosity gaps, and pattern interrupts.
5. **Each email must stand alone.** Not everyone reads every email. Each must make sense on its own while building on the sequence arc.
6. **P.S. lines are second headlines.** Many readers skip to the P.S. Use it strategically for CTA or curiosity hooks.

## Sequence Types and Templates

### Type 1: Lead Magnet Follow-Up (7 emails over 14 days)

**Purpose:** Nurture new leads from opt-in to belief-shift to consideration.
**Reveal Sequence Stage:** Awareness through Education.

| Email | Day | Job | Belief Shift | Bitcoin? |
|-------|-----|-----|-------------|----------|
| 1 | Day 0 | Deliver lead magnet + welcome | "I'm in the right place" | No |
| 2 | Day 1 | The Math Problem | "7% can't close my gap" | No |
| 3 | Day 3 | The Wrong Asset Revelation | "My assets are the problem, not my effort" | No |
| 4 | Day 5 | The Invisible Theft | "Inflation is stealing my savings" | No |
| 5 | Day 7 | The Risk Flip | "Playing it safe IS the real risk" | Teased |
| 6 | Day 10 | The Reveal | "Bitcoin makes mathematical sense" | YES (with reframe) |
| 7 | Day 14 | The Path Forward | "There's a system I can follow" | Yes, openly |

### Type 2: Pre-Launch Warmup (5 emails over 10 days)

**Purpose:** Warm the list before cart opens. Build anticipation.
**Reveal Sequence Stage:** Education through Conversion.

| Email | Day | Job | Focus |
|-------|-----|-----|-------|
| 1 | Day -10 | Story hook | "Something changed in my life that I need to share" |
| 2 | Day -7 | The problem deeper | "I almost made a terrible mistake with my retirement" |
| 3 | Day -5 | Social proof | "A student just sent me this message..." |
| 4 | Day -3 | The announcement tease | "I've been working on something for you" |
| 5 | Day -1 | Cart opens tomorrow | "Tomorrow, I'm opening the doors to..." |

### Type 3: Launch Sequence (8 emails over 7 days)

**Purpose:** Drive enrollment during the cart-open window.
**Reveal Sequence Stage:** Conversion.

| Email | Day | Job | Focus |
|-------|-----|-----|-------|
| 1 | Open Day | Cart open | Full offer reveal with value stack |
| 2 | Day +1 | The Math | "Let me show you why this works" (math proof) |
| 3 | Day +2 | FAQ/Objections | Address top objections |
| 4 | Day +3 | Social proof | Late Bloomer Heroes stories |
| 5 | Day +4 | Founding Hero | Founding Hero pricing/bonus (if applicable) |
| 6 | Day +5 | The Guarantee | Deep dive on Hero's Clarity Guarantee |
| 7 | Day +6 | 48-hour warning | "Doors close in 48 hours" |
| 8 | Close Day | Final call | Last chance, cart closing tonight |

### Type 4: Post-Purchase Onboarding (5 emails over 14 days)

**Purpose:** Welcome new students, reduce buyer's remorse, drive course engagement.
**Reveal Sequence Stage:** Implementation.

| Email | Day | Job | Focus |
|-------|-----|-----|-------|
| 1 | Day 0 | Welcome | "You just changed your financial future" |
| 2 | Day 1 | Getting started | "Here's exactly what to do first" |
| 3 | Day 3 | Module 1 nudge | "Have you met Sarah yet?" |
| 4 | Day 7 | Check-in | "How are you feeling? (This is normal)" |
| 5 | Day 14 | Milestone | "By now you should have your Hero Number" |

## Complete Workflow

### Phase 1: Load Context

1. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md` (voice)
2. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` (business)
3. `Main/FL3 ZenithPro Data/FL3 Business Brief.md` (messaging, Reveal Sequence)
4. `Main/Zenith Avatars/` (avatar profiles)
5. `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/Wrong Asset Manifesto - Email Sequence.md` (existing email reference)

### Phase 2: Accept Sequence Parameters

1. **Sequence type:** Lead magnet follow-up, pre-launch, launch, post-purchase, custom
2. **Target avatar:** Technophobe, Pursuer, Skeptic, or All
3. **Starting Reveal stage:** Where is the reader in the Reveal Sequence?
4. **Launch dates (if applicable):** Cart open, webinar, cart close
5. **Special constraints:** Any bonuses, pricing changes, or events to work in

### Phase 3: Design the Arc

1. Map the belief shifts across the sequence
2. Assign one primary belief shift per email
3. Ensure the Reveal Sequence is respected (no early Bitcoin reveals)
4. Place CTAs strategically (soft early, hard during launch)
5. Plan story hooks for each email opening

### Phase 4: Write Each Email

For each email, produce:

```markdown
## Email [#]: [Internal Name]
**Send Day:** [Day relative to trigger]
**Subject Line Options:**
1. [Option A]
2. [Option B]
3. [Option C]

**Preview Text:** [First line visible in inbox]

**Body:**

[Email body in Scott's voice]

**P.S.** [Strategic P.S. line]

**CTA:** [Primary call to action]
**CTA Link:** [Where it goes]

---
**Belief Shift:** [What belief this email moves]
**Avatar Notes:** [Any avatar-specific adjustments]
**Reveal Stage:** [Where we are in the sequence]
```

### Phase 5: Quality Gates

1. Run `fl3-voice-check` on each email
2. Run `fl3-compliance-check` on each email
3. Verify Reveal Sequence is respected across the arc
4. Verify each email has exactly ONE primary CTA
5. Verify subject lines use FL3 signature patterns
6. Save to `Projects/The-Great-Catch-Up/Email-Sequences/[sequence-name]/`

## Quality Standards

**Maintain:**
- Scott's personal, story-driven email voice
- One belief shift per email
- Reveal Sequence integrity
- "Education not advice" framing in every email
- P.S. lines on every email
- 3 subject line options per email

**Avoid:**
- Multiple CTAs in one email
- Revealing Bitcoin before the designated reveal email
- Generic email copywriting tone (must sound like Scott)
- Hype or urgency tactics that feel manipulative
- Em dashes
- Missing disclaimers on emails discussing returns

## Common Mistakes to Avoid

1. **Don't front-load the pitch.** The first 3-5 emails in a nurture sequence should be pure value and story. Earn the right to pitch.
2. **Don't reveal Bitcoin too early.** The Reveal Sequence exists because leading with "crypto" triggers the Silent Technophobe's terror and the Awakened Skeptic's shame.
3. **Don't send identical emails to all avatars.** If you can segment, adjust the opening hook and framing per avatar.
4. **Don't forget the "out."** Every email should feel like it's okay NOT to buy. This anti-pressure approach paradoxically increases trust and conversion with this audience.
5. **Don't skip the post-purchase sequence.** Buyer's remorse is real for this audience. Reassurance emails in the first 14 days protect against refunds.
6. **Don't make subject lines too clever.** This audience responds to direct, honest subject lines. "The math that kept me up at 3am" beats "You won't BELIEVE what I found."

## Reference Documents

- `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/Wrong Asset Manifesto - Email Sequence.md`
- `Main/FL3 ZenithPro Data/THE FREEDOM NUMBER REVEAL SEQUENCE.md`
- `Main/FL3 ZenithPro Data/STRATEGIC BELIEF INSTALLATION BLUEPRINT v4.0.md`
- `Main/FL3 ZenithPro Data/INVISIBLE INFLUENCE CONVERSION BLUEPRINT.md`
- `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`

---

*FL3 Email Sequence - Building Trust One Email at a Time v1.0.0*
*"Story-first. One belief at a time. Reveal when they're ready."*
