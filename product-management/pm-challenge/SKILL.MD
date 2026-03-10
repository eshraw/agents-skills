---
name: pm-challenge
description: Challenge the prioritization of a feature from a product management perspective. Surfaces trade-offs, assumptions, and opportunity costs to help make better decisions.
---

# PM Feature Challenge

## Overview

Challenge any proposed feature using PM frameworks, product constraints, and devil's advocate reasoning. Helps avoid building the wrong thing.

## When to Use

- Evaluating whether to build a new feature
- Prioritizing between competing features
- Validating that a feature fits product direction
- Checking assumptions before committing dev time

## Instructions

When the user describes a feature to challenge, follow this structure:

### 1. Restate the Feature
Summarize what you understand the feature to be in 1-2 sentences. Ask for clarification if unclear.

### 2. Jobs-to-Be-Done Analysis
- What job is the user hiring this feature to do?
- Is this a core job or a supporting job?
- Could users accomplish this job another way today?
- What's the user's current workaround?

### 3. User Persona Fit
Check if the project's CLAUDE.md defines personas. If yes, evaluate against them. If not, ask:
- Who specifically wants this feature?
- How many users does this serve?
- Are these your most important users?

### 4. Prioritization Scorecard
Score the feature on these dimensions (1-5 scale):

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| **Impact** | ? | How many users benefit? How much? |
| **Confidence** | ? | Do we have evidence users want this? |
| **Effort** | ? | Dev time, maintenance burden, complexity |
| **Alignment** | ? | Fits product principles and constraints? |

Calculate a rough **ICE score**: (Impact × Confidence) / Effort

### 5. The Hard Questions
Ask at least 3 of these:
- Who specifically asked for this?
- What will you NOT build if you build this?
- What's the smallest version that delivers 80% of the value?
- Will you still want to maintain this in 2 years?
- Does this make the core user journey faster or slower?
- Does this improve the core value proposition?
- Is this a "nice to have" disguised as a "must have"?
- What happens if you don't build this?
- Are you building this because users want it, or because you want to build it?

### 6. Constraints Check
Reference any constraints from the project's CLAUDE.md if available. Common constraints to consider:
- Team size and capacity
- Technical architecture limitations (offline-first, etc.)
- Business model constraints (bootstrapped vs funded)
- Privacy/security requirements
- Platform limitations

### 7. Devil's Advocate Position
Take a strong opposing stance, even if the feature seems good. Present the best argument AGAINST building it.

### 8. Recommendation
End with one of:
- **Build it** - Strong case, clear value, acceptable trade-offs
- **Defer it** - Good idea, but not now. Specify what should come first.
- **Kill it** - Doesn't fit product direction or constraints
- **Shrink it** - Build a smaller version. Specify what to cut.

## Tone
- Direct and honest, not harsh
- Use data and logic, not opinions
- Respect the user's autonomy to decide
- Acknowledge when a feature is genuinely good

## Example Usage
```
/pm-challenge adding social features
/pm-challenge mobile app version
/pm-challenge premium subscription tier
/pm-challenge AI-powered recommendations
/pm-challenge importing data from competitors
```