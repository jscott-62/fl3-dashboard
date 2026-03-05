---
name: fl3-ad-copy
description: Facebook/Instagram ad copy generator for Freedom Life 3.0. Creates avatar-targeted ad sets with multiple variations, respects the Reveal Sequence, and flags compliance considerations.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-content-production
  framework_count: 6
  updated: 2026-02-13
---

# FL3 Ad Copy - Facebook/Instagram Ad Generator

Creates targeted ad copy for FL3's Facebook and Instagram campaigns. Produces multiple variations per avatar, respects the Reveal Sequence (no "Bitcoin" in cold traffic), and flags platform compliance considerations.

## When to Use This Skill

- Creating new Facebook/Instagram ad campaigns
- Testing new hooks or angles for existing campaigns
- Refreshing creative to combat ad fatigue
- Creating ads for different funnel destinations (lead magnet, webinar, sales page)
- When the Launch Director agent needs campaign assets

**For maximum hook stopping power:** Delegate hook creation to Copy Arsenal's `/carlton-hooks`.

## Core Principles

1. **The Reveal Sequence controls language.** Cold traffic ads NEVER say "Bitcoin" or "crypto." Use "the one asset," "alternative assets," or "the asset your advisor can't sell you."
2. **Each avatar needs different hooks.** Technophobe responds to simplicity ("no tech required"). Pursuer responds to urgency ("stop researching, start owning"). Skeptic responds to validation ("you were right").
3. **Short primary text wins.** Facebook's algorithm favors engagement. Short, punchy hooks (1-3 lines) often outperform long-form in cold traffic.
4. **Compliance is non-negotiable.** Facebook's financial services ad policy is strict. No guaranteed returns. No "get rich quick." No misleading before/after claims.
5. **Test in sets of 3-5.** Never create just one ad. Create 3-5 variations per avatar per hook angle.

## Complete Workflow

### Phase 1: Load Context

1. `Main/FL3 ZenithPro Data/Ads.md` (existing ad library)
2. `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/Wrong Asset Manifesto - Facebook Ads COMPLIANT.md` (compliant examples)
3. `Main/FL3 ZenithPro Data/Targeting Translator.md` (audience targeting)
4. `Main/FL3 ZenithPro Data/HEADLINES.md` (headline library)
5. `Main/Scott MacMillan Voice DNA/Voice DNA/01-VOICE-AND-TONE.md` (voice)
6. `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` (business context)

### Phase 2: Accept Campaign Parameters

1. **Campaign goal:** Lead magnet opt-in, webinar registration, direct to sales page
2. **Target avatar(s):** Technophobe, Pursuer, Skeptic, or All
3. **Traffic temperature:** Cold (never seen FL3), warm (on email list), hot (attended webinar)
4. **Budget tier:** Testing ($20-50/day) or scaling ($100+/day)
5. **Any constraints:** Specific hooks to test, existing winners to iterate on

### Phase 3: Generate Hook Angles

For each target avatar, select from these proven hook categories:

**Pain-First Hooks:**
- "You did everything right. And you're still behind."
- "50-something. Staring at a retirement account that won't get you there."
- "If 7% returns could save you, they would have by now."

**Curiosity Hooks:**
- "There's one asset class that could change the math entirely."
- "Why is nobody talking about the one investment that's averaged 100%+ returns?"
- "Your financial advisor doesn't want you to see this chart."

**Contrarian Hooks:**
- "What if playing it safe is the riskiest thing you can do?"
- "The financial advice that's keeping you poor."
- "Stop saving more. Start investing smarter."

**Math-Based Hooks:**
- "$100,000 at 7% for 15 years = $275,000. At 20% = $1.5 million. Same money. Different vehicle."
- "1.8 million. That's what you need. Here's why 7% won't get you there."
- "180 paychecks left. That's not too late. That's 180 opportunities."

**Identity Hooks:**
- "For the 55-year-old who's tired of being told to 'just save more.'"
- "Built for people who aren't tech people. Just math people."
- "You're not behind because you failed. You're behind because the system failed you."

### Phase 4: Write Ad Variations

For each hook, produce:

```markdown
## Ad Variation [#]: [Hook Name]
**Avatar Target:** [Technophobe/Pursuer/Skeptic]
**Traffic Temp:** [Cold/Warm/Hot]
**Destination:** [Lead Magnet/Webinar/Sales Page]

**Primary Text (Short - 1-3 lines):**
[Ad copy]

**Primary Text (Medium - 3-5 lines):**
[Ad copy]

**Primary Text (Long - Story format):**
[Ad copy]

**Headline:** [25-40 characters]
**Description:** [Under 30 characters]
**CTA Button:** [Learn More / Sign Up / Get Access / Watch Now]

**Compliance Notes:** [Any flags]
```

### Phase 5: Quality Gates

1. Run `fl3-compliance-check` on all ads (CRITICAL for paid media)
2. Verify Reveal Sequence compliance (no Bitcoin in cold traffic)
3. Verify no guaranteed return language
4. Check Facebook character limits (primary text: 125 chars visible, headline: 40 chars)
5. Save to `Projects/Wrong-Asset-Manifesto/Facebook-Ads/`

## Quality Standards

**Maintain:**
- Scott's calm authority voice (not hype)
- Reveal Sequence compliance
- Platform policy compliance
- Multiple variations for testing
- Avatar-specific targeting

**Avoid:**
- "To the moon," "massive gains," or any hype language
- Guaranteed return claims or specific dollar promises
- "Get rich quick" framing
- Screenshots of account balances
- Urgency tactics that feel manipulative
- Em dashes

## Common Mistakes to Avoid

1. **Don't say "Bitcoin" in cold traffic ads.** This is the #1 mistake. The Reveal Sequence exists for a reason.
2. **Don't promise specific returns.** "Could return 20%" is different from "WILL return 20%." Use historical framing with qualifiers.
3. **Don't ignore Facebook's special category requirements.** Crypto-related ads may require special authorization.
4. **Don't create only one ad variation.** Always create at least 3 for testing.
5. **Don't forget the landing page must match the ad.** If the ad says "free masterclass," the landing page must deliver a free masterclass.

## Reference Documents

- `Main/FL3 ZenithPro Data/Ads.md`
- `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/Wrong Asset Manifesto - Facebook Ads COMPLIANT.md`
- `Main/FL3 ZenithPro Data/Targeting Translator.md`
- `Main/FL3 ZenithPro Data/HEADLINES.md`

---

*FL3 Ad Copy - Targeted Hooks That Convert v1.0.0*
*"The vehicle matters more than the time."*
