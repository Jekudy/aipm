---
name: do-prd
description: Audit an existing PRD for concrete gaps and contradictions, or help write and revise a PRD from an agreed product direction. Use when the task concerns the PRD itself; earlier problem and solution decisions belong to their owning workflow.
---

# do-PRD

Help the PM leave with a usable PRD or a precise list of changes to one. Work in the document they chose. Preserve its language, structure, and the PM's intent; do not replace an existing page with a local draft unless requested.

## Establish the source

- Read the owning project's document rules, current PRD, linked decisions, relevant flows, and sources needed for the request. Treat old drafts and unverified claims as historical, not current product behavior.
- When review comments matter, fetch the full thread, including replies and resolved comments. Compare reply IDs as well as top-level comment IDs when identifying changes. Keep quoted anchors and exact requests in working notes. Distinguish a deletion request, an editorial suggestion, a changed decision, and a reopened question. A later explicit decision supersedes an older one; a discussion does not settle a value.
- Ask only about a material gap that cannot be resolved from the documents or the user's direction. Continue work that does not depend on the answer. Never invent product scope, priorities, metric values, or a decision owner.

## Audit a PRD

- Read the whole relevant document before judging it. Check that its goal, chosen solution, user stories, flows, requirements, acceptance examples, risks, and next steps describe the same scope and mechanism. Trace a changed flow through every affected section.
- Report only concrete contradictions, missing information that prevents an identified reader from using the PRD, and stale claims supported by current evidence. For each finding, cite the exact passage or location, explain the consequence, and propose the smallest repair. Mark source uncertainty explicitly.
- Distinguish a question the PM must decide from an edit the document already supports. Do not award readiness scores or create a new approval gate. An audit request produces findings and suggested edits; it does not publish changes to the source.
- If the requested material is inaccessible, identify what could not be checked. Do not infer it from a summary or claim the audit is complete.

## Write or revise a PRD

- Start from the agreed product direction and existing document. Interview the PM only for decisions or facts that are genuinely missing. Draft supported parts while questions remain open, and mark unresolved choices as questions rather than answers.
- A user story names actor and goal. A flow shows observable actions in order, relevant initial state, branches, and outcome. Keep distinct user perspectives distinct. Requirements state expected behavior, not guessed architecture; acceptance examples make that behavior testable.
- Keep the selected solution, stories, flows, requirements, and risks synchronized. Reuse requirement IDs when behavior remains; retire obsolete branches. A function's priority and the conditions required whenever it ships are separate. Mark new priorities as proposals when the PM has not chosen them.
- Follow the document's existing tables, labels, order, and density. Where useful, put requirement, criterion, priority, and open status together in one table. Merge overlapping risks in the existing risk table and update mitigations when the mechanism changes. Retain units, dates, and sources for metrics; do not present projected impact as measured impact.
- If the PM authorized changes to the working document, re-read it immediately before each edit batch and preserve concurrent changes. For Confluence, use the current storage XHTML, check unique edit anchors and XML validity, compare body as well as version, then re-read the published page to verify tables, links, and consistency. Keep edit tokens and response headers out of Git and snapshots.
- Reconcile each requested comment as implemented, already satisfied, superseded by a newer instruction, or still awaiting a named decision. Resolving or replying to comments is a separate action and requires its own authorization.

## Finish

State what changed or what the audit found, cite the document evidence, and name only decisions that remain open. Verify claims against the final document. Keep case-specific channels, timings, values, and scope decisions in that PRD, not in this reusable skill.
