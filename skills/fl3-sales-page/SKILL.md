---
name: fl3-sales-page
description: Complete long-form sales page generator for The Great Catch-Up course. Produces full sales page using FL3 offer stack, avatar pain points, transformation promise, and guarantee structure. Can delegate to Copy Arsenal for competitive copywriting.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-launch-infrastructure
  framework_count: 12
  updated: 2026-02-13
---

# FL3 Sales Page - The Great Catch-Up Course Sales Page Generator

Produces a complete long-form sales page for The Great Catch-Up course. This skill knows the course content, pricing, bonuses, guarantee, avatars, and messaging frameworks. It follows the FL3 Presentation Sequence from the Value Proposition Stack.

## When to Use This Skill

- Creating the main sales page for The Great Catch-Up
- Creating variant sales pages for different traffic sources or avatars
- Refreshing/updating an existing sales page
- Creating a VSL (Video Sales Letter) script version of the sales page
- When the Launch Director agent needs the core conversion asset

**For maximum quality:** Delegate to the Copy Arsenal via `/arena sales-page 3` to have 4 competing copywriters draft versions. Use this skill for quick, FL3-context-aware sales pages.

## Core Principles

1. **The Presentation Sequence is the architecture.** Follow the 12-step sequence from the Value Proposition Stack exactly. It was engineered for this specific offer and audience.
2. **Sarah IS the reader.** Sarah's story from the course IS the reader's story. Use it as the narrative spine.
3. **The math is the hero.** Don't lead with emotion alone. Lead with the math that proves traditional advice fails, then let emotion reinforce.
4. **Claims are 2nd order.** Never claim specific dollar returns. Claim clarity, understanding, and the path. "The math finally works" not "You'll make $500,000."
5. **The guarantee does the heavy lifting.** The Hero's Clarity Guarantee is stronger than most price objections. Present it fully.
6. **85% toward language.** The sales page should feel empowering, not fear-driven. Problem amplification is 15% max.

## Complete Workflow

### Phase 1: Load All FL3 Context

Load these reference documents:

1. `Main/FL3 ZenithPro Data/FREEDOM LIFE 3.0_ VALUE PROPOSITION STACK.md` (offer architecture)
2. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` (business context)
3. `Main/FL3 ZenithPro Data/FL3 Business Brief.md` (messaging pillars)
4. `Main/The Great Catch Up Course.md` (course content for module descriptions)
5. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md` (voice)
6. `Main/Zenith Avatars/` (avatar profiles)
7. `Main/FL3 ZenithPro Data/HEADLINES.md` (headline options)
8. `Main/FL3 ZenithPro Data/STRATEGIC BELIEF INSTALLATION BLUEPRINT v4.0.md` (belief shift architecture)

### Phase 2: Determine Sales Page Variant

1. **Primary avatar target:** Which avatar is this page optimized for? (Or "All")
2. **Traffic source:** Cold traffic (from ads), warm traffic (from email), or hot traffic (from webinar)?
3. **Format:** Long-form text, VSL script, or hybrid (video + text)?
4. **Pricing version:** $697 pay-in-full, $297x3 payment plan, or $497 Founding Hero?

### Phase 3: Write the 12-Step Presentation Sequence

Follow this exact structure from the Value Proposition Stack:

**Step 1: Pre-Headline (Identity Qualification)**
"For People 45+ Who Did Everything Right and Still Fell Behind"
- Immediate self-identification
- Removes shame
- Creates tribal belonging

**Step 2: Headline (Full Formula)**
Current State + Desired State + Mechanism + Unique Element + Timeline
Use headline from Value Proposition Stack or generate variant.

**Step 3: Sub-Headline (Objection Elimination)**
Remove top 3 objections: Wall Street trust, advisor costs, broken system

**Step 4: Hook (Emotional Activation)**
Sarah's story opening. The 3am anxiety. The shame. The math that doesn't work.
Draw from course Module 01 (Sarah at 51, $65K in 401k, $1.8M gap).

**Step 5: Problem Amplification (Vindication + Urgency)**
Money printing expose. Real inflation at 7-12% vs. reported CPI.
The invisible theft framework. "Your money isn't failing to grow. It's actively being stolen."

**Step 6: Mechanism Tease**
"There is one asset where the math actually works. An asset your advisor won't tell you about. An asset that has historically outperformed everything else by orders of magnitude."
DO NOT name Bitcoin yet (awareness-stage traffic). For warm/hot traffic, name it here.

**Step 7: Revelation**
For warm/hot traffic: Introduce Bitcoin as the logical conclusion.
Reframe immediately: not gambling, not tech-bro stuff, just math.
"21 million is less than infinity. That's the entire argument."

**Step 8: The Method**
Introduce The Hero Investing Method / FREEDOM Framework.
Show the 6-week course structure. Module-by-module overview.
Position as education, not advice. "I'm showing you my system."

**Step 9: Social Proof**
Late Bloomer Heroes Vault stories. People 50-65 who made the math work.
Organize by avatar type so readers find "their" story.

**Step 10: The Offer (Value Stack)**
Present the complete offer stack from Value Proposition Stack:
- Core Training (Value: $2,997)
- Bonus #1: Hero's Numbers Calculator (Value: $497)
- Bonus #2: "They Lied to You" Money Printing Expose (Value: $297)
- Bonus #3: Hero's First Quest (Value: $397)
- Bonus #4: Late Bloomer Heroes Vault (Value: $297)
- Bonus #5: Hero's Safety Net (Value: $697)
- Total Stack Value: $7,682
- 11:1 value ratio

**Step 11: The Guarantee (Risk Elimination)**
The Hero's Clarity Guarantee:
1. Your Hero Number (the exact amount that means "enough")
2. Your Hero Path (whether it's mathematically possible)
3. Your First Action (confidence to make or decide against first investment)

Plus: No Stupid Questions guarantee, Anti-Sales guarantee, Honest Assessment guarantee.
Better Than Free: Keep $1,391 in bonuses even if you refund.

**Step 12: CTA + Urgency**
"Become a Hero Today" / "Start Your Hero Journey"
Urgency: Personal Attention Capacity (limited email access), compound growth runway shrinking.
AVOID: "Buy Now," "Purchase," "Add to Cart"

### Phase 4: Add Supporting Elements

1. **FAQ section:** Address top 8-10 objections
   - "Is this financial advice?" (No, education only)
   - "I'm not a tech person" (No tech required, just math)
   - "What if Bitcoin crashes?" (Volatility vs. real risk reframe)
   - "Can I do this in my 401k?" (Yes, via ETFs)
   - "Is $697 worth it?" (Compare to advisor fees, cost of inaction)
   - "What if this doesn't work for me?" (90-day guarantee)
2. **Price comparison section:** From Value Proposition Stack
3. **Final CTA:** Repeat offer summary + guarantee + button
4. **Disclaimer footer:** Educational content, not financial advice

### Phase 5: Quality Gates

1. Run `fl3-voice-check` on the complete page
2. Run `fl3-compliance-check` on the complete page
3. Verify all prices and bonus values match current offer structure
4. Verify Sarah's story details match course content
5. Save to `Projects/The-Great-Catch-Up/Sales-Page/`

## Integration with Copy Arsenal

For maximum conversion, delegate the sales page to the Copy Arsenal:

```
/arena sales-page 3
```

This runs the competitive arena with 4 copywriters + synthesis. Provide the brief with:
- All FL3 context documents listed in Phase 1
- The 12-step structure as the mandatory outline
- Voice DNA as the voice constraint
- Target avatar and traffic source

**Individual expert options:**
- `/deutsch` for sophisticated long-form (best for Awakened Skeptic)
- `/evaldo` for VSL script version (best for video-first approach)
- `/carlton` for maximum hook stopping power (best for cold traffic)
- `/clayton` for emotional trigger mastery (best for email-driven traffic)

## Quality Standards

**Maintain:**
- Scott's authentic voice throughout (calm authority, not hype)
- 85% toward language / 15% strategic away language
- Math-first, emotion-second approach
- "Education not advice" positioning at all times
- Sarah's story as the narrative anchor

**Avoid:**
- Generic sales page templates that lose Scott's voice
- Hype language ("incredible," "life-changing," "massive")
- Specific return promises without qualifiers
- Blaming the reader for being behind
- Em dashes anywhere on the page
- "Buy Now" or transactional CTA language

## Common Mistakes to Avoid

1. **Don't skip Sarah's story.** It IS the reader's story. Cutting it weakens identification.
2. **Don't lead with Bitcoin for cold traffic.** Follow the Reveal Sequence. Cold traffic pages tease "the one asset" without naming it.
3. **Don't inflate bonus values beyond what's documented.** The Value Proposition Stack has the approved values. Don't change them.
4. **Don't forget the "Better Than Free" element.** "Keep all bonuses even if you refund" is one of the strongest risk reversals. Make it prominent.
5. **Don't rush the price reveal.** Build the full value stack BEFORE revealing the price. The 11:1 ratio only works if the value is established first.
6. **Don't make the guarantee an afterthought.** The Hero's Clarity Guarantee is a major conversion driver for this risk-averse audience. Give it full treatment.

## Reference Documents

- `Main/FL3 ZenithPro Data/FREEDOM LIFE 3.0_ VALUE PROPOSITION STACK.md` (complete offer engineering)
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
- `Main/FL3 ZenithPro Data/FL3 Business Brief.md`
- `Main/The Great Catch Up Course.md` (module content)
- `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`
- `Main/Zenith Avatars/` (all avatar files)
- `Main/FL3 ZenithPro Data/HEADLINES.md`
- `Main/FL3 ZenithPro Data/IDEAL BUYING MINDSET ARCHITECTURE.md`
- `Main/FL3 ZenithPro Data/INVISIBLE INFLUENCE CONVERSION BLUEPRINT.md`

---

*FL3 Sales Page - The Core Conversion Asset v1.0.0*
*"The math finally works. In the time you have left."*
