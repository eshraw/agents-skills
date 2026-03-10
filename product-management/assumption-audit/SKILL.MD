---
name: assumption-audit
description: Surface hidden assumptions in a feature, decision, or plan. Exposes what you're taking for granted so you can validate before committing.
---

# Assumption Audit

## Overview

Every product decision rests on assumptions—about users, technology, market, and resources. This skill systematically surfaces those assumptions so you can decide which ones to validate before committing time and effort.

## When to Use

- Before starting a new feature or project
- When a plan feels "obvious" (often means assumptions are hidden)
- After a failure to understand what you got wrong
- When stakeholders disagree (often arguing from different assumptions)
- Before making irreversible decisions

## Instructions

When the user describes a feature, decision, or plan to audit, follow this structure:

### 1. Restate the Decision
Summarize the decision or plan in 1-2 sentences. Confirm understanding before proceeding.

### 2. User Assumptions
Surface assumptions about users:
- Who will use this? (Are you sure they exist in sufficient numbers?)
- What problem do they have? (Have you validated this?)
- How do they solve it today? (Do they actually care enough to change?)
- Will they find/adopt this? (Discovery and onboarding assumptions)
- Will they pay for this? (If monetized)

Flag assumptions as:
- ✅ **Validated** - Evidence exists
- ⚠️ **Risky** - Plausible but unvalidated
- 🚨 **Critical** - If wrong, the whole thing fails

### 3. Technical Assumptions
Surface assumptions about implementation:
- Can we build this? (Complexity, dependencies, unknowns)
- Will it perform? (Scale, speed, reliability)
- Does it integrate? (With existing systems, third parties)
- Can we maintain it? (Long-term cost, expertise required)
- What could break? (Edge cases, failure modes)

### 4. Market Assumptions
Surface assumptions about the competitive landscape:
- Is this differentiated? (Why wouldn't users pick alternatives?)
- Is the timing right? (Too early? Too late?)
- Will the market stay stable? (Platform changes, regulations)
- Is there a moat? (Can competitors copy this easily?)

### 5. Resource Assumptions
Surface assumptions about what you have:
- Do we have the skills? (Or need to learn/hire?)
- Do we have the time? (Realistic timeline?)
- Do we have the money? (Runway, budget)
- Do we have the focus? (Or competing priorities?)

### 6. Hidden "Of Course" Assumptions
Look for assumptions so obvious they're invisible:
- "Of course users will..." (Will they?)
- "Obviously we can..." (Can you?)
- "Everyone knows..." (Do they?)
- "It's just a matter of..." (Is it?)

These are often the most dangerous because they go unexamined.

### 7. Assumption Risk Matrix
Summarize the most critical assumptions:

| Assumption | Impact if Wrong | Confidence | Validation Method |
|------------|-----------------|------------|-------------------|
| ? | High/Med/Low | High/Med/Low | How to test it |
| ? | High/Med/Low | High/Med/Low | How to test it |
| ? | High/Med/Low | High/Med/Low | How to test it |

### 8. Recommendations
Suggest concrete next steps:
- Which assumptions to validate first (high impact + low confidence)
- How to validate cheaply (interviews, prototypes, data analysis)
- What to do if key assumptions are wrong (pivot, kill, or proceed anyway)

## Tone
- Curious, not accusatory
- Surface assumptions without judgment
- Help the user see blind spots
- Acknowledge that all decisions require assumptions—the goal is awareness, not paralysis

## Example Usage
```
/assumption-audit we're building a premium tier with advanced analytics
/assumption-audit users will import their data from spreadsheets
/assumption-audit we can launch in 3 months
/assumption-audit our ML model will predict resole timing accurately
```