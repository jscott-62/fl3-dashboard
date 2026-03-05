---
name: fl3-launch-sequence
description: Complete launch orchestrator for The Great Catch-Up course. Plans and produces all content for a launch window including email sequences, social posts, webinar promotion, and cart-open/close messaging.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-launch-infrastructure
  framework_count: 6
  updated: 2026-02-13
---

# FL3 Launch Sequence - Course Launch Content Orchestrator

Plans and produces all content needed for a complete course launch window. Creates the pre-launch warmup, webinar promotion, cart-open sequence, urgency sequence, and cart-close content across all channels.

## When to Use This Skill

- Planning a full course launch for The Great Catch-Up
- Re-launching with new positioning, pricing, or bonuses
- Planning a mini-launch or flash enrollment window
- When the Launch Director agent needs all launch assets produced

**This skill orchestrates.** It calls other FL3 skills to produce individual assets.

## Core Principles

1. **A launch is a coordinated campaign, not a collection of emails.** Every piece of content across every channel must tell the same story at the same time.
2. **Pre-launch builds desire. Launch fulfills it.** Don't pitch during pre-launch. Don't educate during cart-close.
3. **Urgency must be authentic.** FL3's urgency comes from compound growth runway (every year waited = less multiplier) and personal attention capacity (limited email access). Not fake deadlines.
4. **The webinar is the primary conversion event.** All other launch content points toward the webinar. Post-webinar, all content points toward the sales page.
5. **Cart-close is the highest-converting period.** 40-60% of sales happen in the last 48 hours. Don't underproduce the close.

## Complete Workflow

### Phase 1: Accept Launch Parameters

1. **Launch type:** Full launch, re-launch, mini-launch, or flash sale
2. **Key dates:**
   - Pre-launch start date
   - Webinar date(s)
   - Cart open date
   - Cart close date
3. **Pricing for this launch:** Standard ($697), Founding Hero ($497), or special
4. **Special elements:** Early bird bonuses, limited spots, founding hero pricing
5. **Channels active:** Email, Facebook ads, Instagram, LinkedIn, YouTube, blog

### Phase 2: Generate Launch Timeline

Create a day-by-day timeline:

```markdown
## LAUNCH TIMELINE: The Great Catch-Up [Launch Date]

### PRE-LAUNCH (Days -14 to -1)
| Day | Email | Social | Ads | Other |
|-----|-------|--------|-----|-------|
| -14 | Story hook email | IG: Teaser post | - | Blog post: pillar content |
| -10 | Problem deeper | LI: Authority post | - | - |
| -7 | Social proof email | FB: Student story | Start webinar ads | YouTube: pillar video |
| -5 | Announcement tease | IG: Countdown | Webinar ads running | - |
| -3 | Webinar invite #1 | All: Webinar promo | Ramp webinar ads | - |
| -1 | Webinar invite #2 | All: Tomorrow! | Peak ad spend | - |

### WEBINAR DAY (Day 0)
| Time | Action |
|------|--------|
| Morning | Reminder email + social posts |
| 1 hr before | Final reminder email |
| Live | Webinar runs |
| Post-webinar | Replay email + cart open email |

### CART OPEN (Days +1 to +5)
| Day | Email | Social | Ads |
|-----|-------|--------|-----|
| +1 | The Math email | All: Cart is open | Retarget webinar attendees |
| +2 | FAQ/Objections email | IG: FAQ carousel | Retarget + lookalike |
| +3 | Social proof email | FB: Student stories | Continue retargeting |
| +4 | Guarantee deep-dive | LI: Thought leadership | - |
| +5 | 48-hour warning | All: Closing soon | Urgency ads |

### CART CLOSE (Days +6 to +7)
| Day | Email | Social | Ads |
|-----|-------|--------|-----|
| +6 | Last chance AM | All: Final day tomorrow | Final push |
| +7 AM | Final call | All: Doors closing tonight | Last spend |
| +7 PM | Cart closing NOW | All: Last chance | Ads off |
| +7 11pm | Closed email | - | - |
```

### Phase 3: Produce Launch Assets

Delegate to specific FL3 skills:

1. **Pre-launch emails (5):** Call `/fl3-email-sequence` with type "pre-launch"
2. **Launch emails (8):** Call `/fl3-email-sequence` with type "launch"
3. **Webinar promotion:** Call `/fl3-webinar-brief` for arena submission
4. **Social posts (20-30):** Call `/fl3-social-batch` for each launch phase
5. **Ad copy (10-15 variations):** Call `/fl3-ad-copy` for webinar + cart campaigns
6. **Post-purchase onboarding (5):** Call `/fl3-email-sequence` with type "post-purchase"

### Phase 4: Cross-Channel Consistency Check

Verify that all assets tell the same story:
- Same language and framing across email, social, and ads
- Reveal Sequence maintained (no premature Bitcoin mentions)
- Pricing and bonus details consistent everywhere
- Dates and deadlines match across all channels
- CTAs point to correct destinations at each stage

### Phase 5: Save and Report

1. Save all assets to `Projects/The-Great-Catch-Up/` organized by channel
2. Save launch timeline to `calendar/`
3. Produce Launch Readiness Report:

```markdown
## LAUNCH READINESS REPORT

**Launch:** The Great Catch-Up [Date]
**Cart Open:** [Date] | **Cart Close:** [Date]

### ASSETS PRODUCED
| Asset | Count | Location | Status |
|-------|-------|----------|--------|
| Pre-launch emails | 5 | Projects/The-Great-Catch-Up/Email-Sequences/pre-launch/ | Ready |
| Launch emails | 8 | Projects/The-Great-Catch-Up/Email-Sequences/launch/ | Ready |
| Post-purchase emails | 5 | Projects/The-Great-Catch-Up/Email-Sequences/post-purchase/ | Ready |
| Social posts | [N] | Projects/Weekly-Content/Social Media/ | Ready |
| Ad variations | [N] | Projects/Wrong-Asset-Manifesto/Facebook-Ads/ | Ready |
| Webinar brief | 1 | Projects/Webinar/ | Ready for arena |

### STILL NEEDED
- [ ] Sales page (run /fl3-sales-page or /arena)
- [ ] Webinar (run /webinar-arena with brief)
- [ ] Ad creative (images/video, produced separately)
- [ ] Email platform setup (Beehiiv sequences)
- [ ] Facebook ad campaign setup

### QUALITY STATUS
- Voice check: [PASSED/PENDING]
- Compliance check: [PASSED/PENDING]
- Cross-channel consistency: [VERIFIED/PENDING]
```

## Quality Standards

**Maintain:**
- Consistent messaging across all channels and dates
- Authentic urgency (compound growth, capacity limits)
- Pre-launch warmth before launch pitch
- Heavy cart-close content (40-60% of sales happen here)

**Avoid:**
- Pitching during pre-launch
- Fake scarcity or manufactured deadlines
- Inconsistent pricing or bonus mentions
- Under-producing cart-close content
- Missing post-purchase onboarding

## Common Mistakes to Avoid

1. **Don't under-invest in pre-launch.** The warmup period builds the desire that the launch fulfills. Skip it and conversion drops.
2. **Don't send only 2 cart-close emails.** The last 48 hours need at least 3 emails (48-hour warning, final call, closing tonight).
3. **Don't forget the post-purchase sequence.** Buyer's remorse is real. Reassurance in the first 14 days prevents refunds.
4. **Don't let social and email tell different stories.** Cross-channel consistency is critical. Same offer, same deadlines, same framing.

## Reference Documents

- All documents referenced by `/fl3-email-sequence`, `/fl3-ad-copy`, `/fl3-social-batch`, and `/fl3-webinar-brief`
- `Main/FL3 ZenithPro Data/FREEDOM LIFE 3.0_ VALUE PROPOSITION STACK.md` (offer architecture)

---

*FL3 Launch Sequence - Coordinated Campaign Orchestrator v1.0.0*
*"A launch is a story told across every channel, every day, building to one moment."*
