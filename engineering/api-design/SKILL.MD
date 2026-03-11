---
name: api-design
description: Design a well-structured API from a desired outcome. Produces OpenAPI specifications, usage examples, and a plain-language section for non-technical stakeholders.
---

# API Design

## Overview

Turn a desired product or business outcome into a fully designed API — including OpenAPI 3.1 specification, practical usage examples, and a plain-language explanation for non-technical stakeholders such as product managers.

## When to Use

- Starting a new API from a product requirement or user story
- Aligning engineering and product on what an API will do before building it
- Documenting an API design decision for broader review
- Quickly scaffolding a contract before implementation begins

## Instructions

### Phase 0 — Discovery questionnaire

Before designing anything, run this short questionnaire using the `AskUserQuestion` tool. Ask one question at a time and wait for the answer before proceeding to the next.

**Question 1 — The problem**

Use `AskUserQuestion` (free text):
- question: "What problem are you trying to solve? Describe it from the perspective of whoever (or whatever) will use this API — not the solution, just the problem or need."

**Question 2 — The consumer**

Use `AskUserQuestion` with choices:
- question: "Who or what will call this API?"
- choices:
  - "A) A web or mobile app we own"
  - "B) A third-party / external partner"
  - "C) An internal backend service or microservice"
  - "D) Multiple of the above (I'll specify)"
  - "E) Not sure yet"

If D, follow up with `AskUserQuestion` (free text): "Describe each consumer and what they need from the API."

**Question 3 — Core actions**

Use `AskUserQuestion` (free text):
- question: "What are the 3–5 things someone needs to be able to DO with this API? List them as actions (e.g. 'create an order', 'get the status of a shipment', 'cancel a subscription')."

**Question 4 — Data**

Use `AskUserQuestion` (free text):
- question: "What information does the API need to work with? Think about what goes IN (what the caller sends) and what comes OUT (what the API returns). Don't worry about technical field names — plain language is fine."

**Question 5 — Constraints**

Use `AskUserQuestion` with choices:
- question: "Are there any known constraints or requirements? (select all that apply)"
- choices:
  - "A) Authentication required (only known callers should access it)"
  - "B) Must integrate with an existing system or database"
  - "C) Performance-sensitive (high volume or low latency)"
  - "D) Must follow an existing API style or convention in our codebase"
  - "E) No specific constraints yet"
  - "F) Other — I'll describe"

If D or F, follow up with `AskUserQuestion` (free text): "Describe the constraint."

**Question 6 — Success**

Use `AskUserQuestion` (free text):
- question: "How will you know this API is successful? What does 'done' look like from a product or business perspective?"

After all answers are collected, summarize your understanding back to the user using `AskUserQuestion`:
- question: "Here's what I understood — does this look right before I start designing?"
  - Include a brief summary of: the problem, the consumers, the core actions, and any constraints.
- choices:
  - "Yes, go ahead and design it"
  - "No, let me correct something"

If the user says no, ask `AskUserQuestion` (free text): "What should I correct?" Then re-summarize and confirm before proceeding.

---

### 1. Restate the Goal
Summarize the desired outcome in 1-2 sentences. Confirm what the API is meant to achieve and for whom (internal system, mobile client, third-party partner, etc.). Ask for clarification if the scope is ambiguous.

### 2. Design Decisions
Before producing specifications, briefly document the key design choices and why they were made:
- **Resource modeling** — what are the core entities and why
- **REST vs other paradigms** — and why REST (or not) fits this use case
- **Auth approach** — API key, OAuth, JWT, none — and rationale
- **Pagination strategy** — cursor, offset, or none — and why
- **Error handling philosophy** — how errors are structured and why
- **Versioning strategy** — URL path, header, or none — and why

Keep this section concise. One sentence per decision is enough.

### 3. OpenAPI 3.1 Specification
Produce a complete, valid OpenAPI 3.1 YAML document covering:
- `info` block with title, version, and description
- `servers` with a realistic base URL
- All `paths` with:
  - HTTP method and summary
  - Request parameters (path, query, header) with descriptions and types
  - Request body schema where applicable
  - Response schemas for success (2xx) and common errors (4xx, 5xx)
  - Security requirements
- `components` section with reusable `schemas`, `securitySchemes`, and `responses`

Use realistic field names, types, and descriptions. Do not use placeholder values like `string` or `integer` without context.

```yaml
# Full OpenAPI 3.1 spec goes here
```

### 4. Usage Examples
Provide concrete, copy-pasteable examples for the most important endpoints:
- A `curl` request for each key operation
- The expected JSON response (success case)
- At least one error response example with the matching `curl` call

Format each example as:
```bash
# What this does
curl ...
```
```json
// Response
{ ... }
```

### 5. Plain-Language Stakeholder Brief
Write this section as if the reader has never read API documentation. Avoid jargon. Use analogies and everyday language.

#### What this API does
Explain the API's purpose in 2-3 sentences a product manager could repeat in a meeting.

#### What each endpoint does (in plain English)
For each endpoint, one short paragraph describing:
- What you send
- What happens
- What you get back
- A real-world analogy if helpful

#### Example walkthrough
Walk through the most important user journey end-to-end using plain language, not code. Example: "When a user places an order, the app calls the Orders API. The API checks if the item is in stock, reserves it, and sends back a confirmation with an order ID. The app shows that ID to the user."

#### Why it was designed this way
For each major design decision from section 2, explain the reasoning in one plain-English sentence. Focus on benefits to the product and users, not technical correctness.

## Tone
- Precise in the specification, plain in the stakeholder brief
- Design decisions should be justified, not just listed
- Examples should be realistic enough to be directly useful
- Avoid over-engineering — match complexity to the stated outcome

## Example Usage
```
/api-design users should be able to submit support tickets and track their status
/api-design a mobile app needs to browse a product catalog and add items to a cart
/api-design third-party partners need to pull daily sales reports for their accounts
/api-design an internal service needs to send transactional emails via a shared gateway
```
