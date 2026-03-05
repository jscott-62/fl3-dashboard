---
name: fl3-compliance-check
description: Financial compliance checker for Freedom Life 3.0 content. Scans for guaranteed return claims, specific financial advice, missing disclaimers, FTC disclosure requirements, and platform ad policy violations.
license: Private
metadata:
  version: 1.0.0
  author: J. Scott MacMillan
  category: fl3-quality-control
  framework_count: 5
  updated: 2026-02-13
---

# FL3 Compliance Check - Financial Content Compliance Validator

Scans FL3 content for potential regulatory and platform policy issues before publishing. FL3 is an educational business, NOT a financial advisory service. Every piece of content must maintain that distinction clearly.

## When to Use This Skill

- Before publishing any content that discusses investment returns, Bitcoin, or financial outcomes
- Before submitting Facebook/Instagram ads (financial services ad policies are strict)
- Before publishing testimonials or success stories
- When the Brand Guardian agent runs its quality check pipeline
- When creating sales pages, webinars, or email sequences that reference returns

**This skill does NOT create content.** It only evaluates existing content for compliance risks.

## Core Principles

1. **FL3 is education, not advice.** Every piece of content must frame the business as educational. "I'm showing you what I did" is education. "You should invest in Bitcoin" is advice.
2. **Past performance language is critical.** Historical returns must be framed as past performance, not promises. "Bitcoin has historically averaged 100% annual returns" needs the qualifier that past performance doesn't guarantee future results.
3. **The Reveal Sequence has compliance implications.** Withholding Bitcoin's name in early marketing is a strategic choice, but the moment it's revealed, all crypto-specific compliance rules apply.
4. **Platform policies differ from legal compliance.** Facebook's financial services ad policies are more restrictive than general FTC guidelines. Content may be legally fine but still violate platform terms.
5. **Disclaimers must be present, not buried.** "Not financial advice" in tiny print at the bottom doesn't count. Disclaimers should be visible and contextually placed.

## Complete Workflow

### Phase 1: Load Compliance References

1. Review FL3's positioning as educational business (from Business Summary)
2. Load existing compliant content examples:
   - `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/Wrong Asset Manifesto - Facebook Ads COMPLIANT.md`
   - `Main/The Great Catch Up Course.md` (Slide 2 disclaimer language)

### Phase 2: Accept and Classify Content

1. Accept content to review
2. Identify content type and distribution channel
3. Determine if this is paid advertising (stricter rules apply)
4. Determine funnel stage and whether Bitcoin has been revealed

### Phase 3: Scan Against 5 Compliance Frameworks

**Framework 1: Guaranteed Returns Language**
Scan for and flag:
- "You WILL earn X%"
- "Guaranteed returns"
- "Make $X in Y months"
- "Turn $X into $Y"
- Any specific dollar amounts framed as promises rather than examples
- Projected returns without qualifiers ("at 20% returns" needs "if historical trends continue" or similar)

**Severity:** CRITICAL. These can trigger regulatory action.

**Compliant alternatives:**
- "If Bitcoin continues its historical trajectory..."
- "At a hypothetical 20% annual return..."
- "In my experience, the math looks like this..."
- "Here's what the numbers show historically..."

**Framework 2: Financial Advice Boundary**
Scan for and flag:
- "You should invest in X"
- "Buy X now"
- "Sell your Y and put it in Z"
- "The best investment is..."
- Any imperative language directing specific investment actions
- Personalized advice ("based on your situation, you should...")

**Severity:** CRITICAL. This crosses the education/advice boundary.

**Compliant alternatives:**
- "Here's what I chose to do..."
- "The approach I teach involves..."
- "Students who've taken this path have..."
- "Education about how to evaluate..."

**Framework 3: Disclaimer Requirements**
Check for presence and placement of:
- "Not financial advice" / "For educational purposes only" disclaimer
- "Past performance does not guarantee future results" when citing historical returns
- "Consult a qualified financial advisor for personal advice"
- FTC disclosure for testimonials/endorsements ("Results not typical" or similar)
- Affiliate disclosure if any affiliate links present

**Severity:** WARNING if missing. CRITICAL if discussing specific returns without any disclaimer.

**Placement rules:**
- YouTube: verbal disclaimer early in video + written in description
- Blog: disclaimer at top and/or bottom
- Social: disclaimer in post or bio link
- Email: footer disclaimer
- Ads: disclaimer visible in ad (not just landing page)
- Sales page: multiple disclaimer placements

**Framework 4: Platform Ad Policies**
For paid advertising content, check:
- Facebook/Meta financial services policies:
  - No "get rich quick" implications
  - No guaranteed outcomes
  - No misleading before/after claims
  - No targeting based on financial status
  - Crypto-related ads may require special authorization
- No "too good to be true" framing
- No urgent/scarcity tactics that feel manipulative
- No screenshots of account balances or P&L

**Severity:** WARNING to CRITICAL depending on platform.

**Framework 5: Reveal Sequence Compliance**
Check content against its funnel stage:
- **Awareness stage (cold traffic):** Bitcoin/crypto should NOT be mentioned by name. Use "the one asset," "alternative assets," "the asset your advisor can't sell you"
- **Education stage:** Bitcoin can be named but must be immediately reframed (not scary, logical conclusion)
- **Implementation/Conversion stage:** Bitcoin discussed openly, full compliance language applies

**Severity:** WARNING. Not a legal issue but a strategic one.

### Phase 4: Produce Compliance Report

Output format:

```markdown
## FL3 COMPLIANCE REPORT

**Content:** [Title or first 20 words]
**Type:** [YouTube/Blog/Social/Email/Ad/Sales Page]
**Channel:** [Platform]
**Is Paid Advertising:** [Yes/No]
**Funnel Stage:** [Awareness/Education/Implementation/Conversion]

### FINDINGS

| # | Issue | Framework | Severity | Line/Location | Suggested Fix |
|---|-------|-----------|----------|---------------|---------------|
| 1 | [Description] | [1-5] | [CRITICAL/WARNING/NOTE] | [Where] | [How to fix] |

### SUMMARY
- **CRITICAL issues:** [count] (must fix before publishing)
- **WARNING issues:** [count] (should fix)
- **NOTES:** [count] (optional improvements)

### DISCLAIMER CHECK
- [ ] Educational disclaimer present
- [ ] Past performance disclaimer present (if returns cited)
- [ ] Personal advice disclaimer present
- [ ] FTC testimonial disclosure present (if testimonials used)
- [ ] Platform-specific requirements met (if paid ad)

### CLEARANCE STATUS
- **CLEARED:** No critical issues, safe to publish
- **CONDITIONAL:** Fix critical issues, then cleared
- **BLOCKED:** Major compliance concerns, needs significant revision
```

### Phase 5: Suggest Compliant Rewrites

For each CRITICAL and WARNING finding, provide a specific compliant rewrite that preserves the persuasive intent while removing the compliance risk.

## Quality Standards

**Maintain:**
- Conservative flagging (better to over-flag than under-flag)
- Specific, actionable fixes that preserve persuasive power
- Clear severity levels (don't cry wolf on minor issues)
- Respect for FL3's educational positioning

**Avoid:**
- Stripping all persuasion out of the content (compliance doesn't mean boring)
- Missing platform-specific requirements for paid ads
- Ignoring the Reveal Sequence stage
- Treating the disclaimer as a magic shield (the content itself must be compliant)

## Common Mistakes to Avoid

1. **Don't over-flag educational examples.** "If you invested $1,000 in 2015, it would be worth $250,000 today" is a factual historical statement, not a guaranteed return claim. But it DOES need the past performance qualifier.
2. **Don't miss the "I" vs. "you" distinction.** "I invested in Bitcoin" is fine. "You should invest in Bitcoin" crosses the line.
3. **Don't ignore compound claims.** A single sentence might be fine, but when multiple return claims stack up without disclaimers, the cumulative effect can be problematic.
4. **Don't assume the landing page disclaimer covers the ad.** Each piece of content needs its own appropriate disclaimer.
5. **Don't forget crypto-specific ad restrictions.** Facebook has special authorization requirements for crypto-related advertising. Flag if the content might trigger this.

## Reference Documents

- `Main/FL3 ZenithPro Data/The Wrong Asset Manifesto/Wrong Asset Manifesto - Facebook Ads COMPLIANT.md`
- `Main/The Great Catch Up Course.md` (disclaimer language on Slide 2)
- `Main/FL3 ZenithPro Data/Freedom Life 3.0 - Complete Business Summary.md` (positioning as education)

---

*FL3 Compliance Check - Protecting the Business v1.0.0*
*Education, not advice. Always.*
