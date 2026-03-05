---
name: fl3-webinar-brief
description: Creates complete webinar briefs for The Great Catch-Up, formatted for the ZenithPro Webinar Arena. Produces the brief document, avatar context, and supporting materials the arena experts need.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-launch-infrastructure
  framework_count: 4
  updated: 2026-02-13
---

# FL3 Webinar Brief - Webinar Arena Brief Generator

Creates a complete, arena-ready webinar brief for The Great Catch-Up course. The output is formatted for direct submission to the ZenithPro Webinar Arena (`/webinar-arena`), where 6 competing experts will draft the webinar.

## When to Use This Skill

- Creating a new webinar for the course launch
- Refreshing the existing webinar with new data or angles
- Creating webinar variants for different avatars or traffic sources
- When the Launch Director agent needs a webinar asset

**This skill produces the brief only.** To create the actual webinar, run `/webinar-arena` with the brief this skill produces.

## Core Principles

1. **The brief is the blueprint.** The quality of the arena output depends entirely on the quality of the brief. Include everything the experts need.
2. **One primary avatar per webinar.** While the webinar should work for all three avatars, optimize the brief for one primary avatar.
3. **The Reveal Sequence happens DURING the webinar.** The webinar is where Bitcoin gets named for many audience members. The brief must instruct the experts to manage this transition.
4. **Constraints protect the brand.** Include Scott's voice rules, compliance requirements, and anti-patterns as mandatory constraints.

## Complete Workflow

### Phase 1: Load FL3 Context

1. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
2. `Main/FL3 ZenithPro Data/FREEDOM LIFE 3.0_ VALUE PROPOSITION STACK.md`
3. `Main/The Great Catch Up Course.md` (course content for teaching section)
4. `Main/Zenith Avatars/` (avatar profiles)
5. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md`
6. `Main/FL3 ZenithPro Data/FL3 Business Brief.md` (4 Pillars, messaging)
7. `Main/FL3 ZenithPro Data/SILENT TECHNOPHOBE - Content Ecosystem Architecture v2.0.md` (epiphany units)

### Phase 2: Accept Webinar Parameters

1. **Webinar objective:** Lead generation, direct sale, or hybrid
2. **Primary avatar:** Technophobe, Pursuer, or Skeptic
3. **Traffic source:** Facebook ads, email list, organic social, mixed
4. **Pricing for this webinar:** $697 full, $497 Founding Hero, or $297x3 plan
5. **Special elements:** Any bonuses, limited-time offers, or events to include
6. **Duration target:** 60 min, 90 min, or 120 min

### Phase 3: Generate Arena Brief

Produce the brief in the Webinar Arena's required format:

```markdown
# WEBINAR ARENA BRIEF: [Webinar Title]

## PRODUCT/OFFER
- **Product:** The Great Catch-Up: The Hero Investing Method
- **Price:** [As specified]
- **Payment Plan:** [If applicable]
- **Guarantee:** The Hero's Clarity Guarantee (90-day, 3 specific outcomes)
- **Bonuses:** [List from Value Proposition Stack]

## TARGET MARKET
- **Primary Avatar:** [Name, age, core fear, barrier, key message]
- **Secondary Avatars:** [Brief descriptions]
- **Current State:** "I did everything right, I'm still behind, and I don't know if the math can ever work for me"
- **Desired State:** "I understand exactly why I fell behind (it wasn't my fault), I've discovered the assets where the math actually works, and I have a clear path to execute"

## KEY CONSTRAINTS
- **Voice:** Must sound like J. Scott MacMillan (calm authority, empathetic challenger, no hype)
- **No em dashes** in any output
- **Reveal Sequence:** Bitcoin is NOT named in the first half. Revealed mid-webinar with immediate reframe.
- **Compliance:** This is education, not financial advice. No guaranteed returns. Include disclaimers.
- **85% toward language / 15% strategic away language**
- **No blame.** Validate the reader. The system failed them, not the other way around.

## CORE MESSAGES (The 4 Pillars)
1. The math doesn't work at 7% returns
2. Traditional advice fails for catch-up
3. Better vehicles exist (the one asset)
4. The real risk is staying in low-return assets

## EPIPHANY SEQUENCE
The webinar must deliver these belief shifts in order:
1. "My savings are being stolen by invisible inflation" (The Invisible Theft)
2. "My asset choice, not my effort, determines outcomes" (The Wrong Asset)
3. "There IS an asset where the math works" (The Reveal)
4. "I am capable of doing this" (The Identity Permission)
5. "Starting now gives me the best chance" (The Urgency)

## TEACHING CONTENT
Draw from The Great Catch-Up course modules:
- Module 01: Sarah's story, the math wake-up call, personal responsibility
- Module 02: Money printing, inflation, the invisible theft
- Additional module content as relevant to the teaching section

## OFFER STACK (present in this order)
1. Core Training (Value: $2,997)
2. Hero's Numbers Calculator (Value: $497)
3. "They Lied to You" Money Printing Expose (Value: $297)
4. Hero's First Quest (Value: $397)
5. Late Bloomer Heroes Vault (Value: $297)
6. Hero's Safety Net (Value: $697)
- Total Value: $7,682
- Price: [As specified]
- Better Than Free: Keep $1,391 in bonuses even with refund

## CTA LANGUAGE
Use: "Become a Hero Today" / "Start Your Hero Journey" / "Get the Hero Method Now"
Avoid: "Buy Now" / "Purchase" / "Add to Cart" / "Submit Payment"

## ADDITIONAL CONTEXT
[Any webinar-specific notes, events, market conditions, etc.]
```

### Phase 4: Package Supporting Materials

Include with the brief:
1. **Avatar Dossier:** Full avatar profiles from `Zenith Avatars/`
2. **Voice Reference:** Key excerpts from Voice DNA
3. **Existing Webinar (if any):** Reference to `FL3 ZenithPro Data/Webinar Arena Outputs/`
4. **Compliance Checklist:** Key compliance rules for the arena experts

### Phase 5: Save and Instruct

1. Save brief to `Projects/Webinar/`
2. Output instructions for running the arena:
   ```
   To run this webinar through the arena:
   /webinar-arena [brief-file-path] [number-of-rounds]
   ```

## Quality Standards

**Maintain:**
- Complete information for arena experts (they shouldn't need to search for context)
- Clear constraints that protect the FL3 brand
- Realistic duration and structure expectations
- Proper Reveal Sequence instructions

**Avoid:**
- Incomplete briefs that force experts to guess
- Missing voice constraints (the arena experts don't know Scott's voice without explicit instructions)
- Overly rigid structure (let the experts do their work within the constraints)

## Common Mistakes to Avoid

1. **Don't skip the voice constraints.** Arena experts default to their own style. Scott's voice must be explicitly required.
2. **Don't forget the Reveal Sequence instructions.** The experts need to know when and how Bitcoin gets named.
3. **Don't provide too little teaching content.** The content section of the webinar needs real substance from the course. Give the experts enough material.
4. **Don't omit the existing webinar reference.** If a previous webinar exists, reference it so experts can build on what worked.

## Reference Documents

- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md`
- `Main/FL3 ZenithPro Data/FREEDOM LIFE 3.0_ VALUE PROPOSITION STACK.md`
- `Main/The Great Catch Up Course.md`
- `Main/Zenith Avatars/`
- `Main/FL3 ZenithPro Data/SILENT TECHNOPHOBE - Content Ecosystem Architecture v2.0.md`
- `Main/FL3 ZenithPro Data/Webinar Arena Outputs/` (existing webinar if available)
- `Main/ZenithPro-Webinar-Arena-v1.0/sample-briefs/` (brief format reference)

---

*FL3 Webinar Brief - Arena-Ready Briefs v1.0.0*
*"The brief is the blueprint. Give the experts everything they need."*
