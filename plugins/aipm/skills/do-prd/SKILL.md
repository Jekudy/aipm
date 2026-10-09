---
name: do-prd
description: Audit an existing PRD for concrete gaps and contradictions, or help write and revise a PRD from an agreed product direction. Use when the task concerns the PRD itself; earlier problem and solution decisions belong to their owning workflow.
---

# do-PRD

Help the PM leave with a usable PRD or a precise list of changes to one. Work in the document they chose. Preserve its language, structure, and the PM's intent; do not replace an existing page with a local draft unless requested.

## Establish the source

- Read the owning project's document rules, current PRD, linked decisions, relevant flows, and sources needed for the request. Treat old drafts and unverified claims as historical, not current product behavior.
- Keep each document's canonical URL exactly as supplied by the user or returned in the source's `url` field. Do not reconstruct it from a page ID, truncate its title, or substitute an unverified `short_url`. Correct stale links in current navigation; preserve historical snapshots.
- When review comments matter, fetch the full thread, including replies and resolved comments. Compare reply IDs as well as top-level comment IDs when identifying changes. Keep quoted anchors and exact requests in working notes. Distinguish a deletion request, an editorial suggestion, a changed decision, and a reopened question. A later explicit decision supersedes an older one; a discussion does not settle a value.
- Ask only about a material gap that cannot be resolved from the documents or the user's direction. Continue work that does not depend on the answer. Never invent product scope, priorities, metric values, or a decision owner.

## Audit a PRD

- Read the whole relevant document before judging it. Check that its goal, chosen solution, user stories, flows, requirements, acceptance examples, risks, and next steps describe the same scope and mechanism. Apply the story and flow checks below; trace a changed flow through every affected section.
- Report only concrete contradictions, missing information that prevents an identified reader from using the PRD, and stale claims supported by current evidence. For each finding, cite the exact passage or location, explain the consequence, and propose the smallest repair. Mark source uncertainty explicitly.
- Distinguish a question the PM must decide from an edit the document already supports. Judge completion at the requested level: an explicitly open choice limits that branch's readiness, not automatically the usefulness of every high-level flow. A target flow may include lower-priority branches; do not infer a first-release commitment from their presence. Do not award readiness scores or create a new approval gate. An audit request produces findings and suggested edits; it does not publish changes to the source.
- If the requested material is inaccessible, identify what could not be checked. Do not infer it from a summary or claim the audit is complete.

## Write or revise a PRD

- Use `text-simple` as the writing layer for new Russian PRD prose. Invoke the installed skill and read its required reference; if no invocation tool exists, read its `SKILL.md` and apply it directly. Use the user's current-text instruction first, then the explicit conversation setting (including off); otherwise apply 100% locally to this PRD task. The local default does not change the conversation setting. Do not copy the language rules here or claim the skill was applied if it could not be loaded.
- Start from the agreed product direction and existing document. Establish the reader and intended level of detail from the request and source. For new or substantially changed flows, produce a compact, reviewable story/flow draft before expanding requirement tables. Interview only for missing decisions or facts; follow the PM's requested cadence, group related questions when useful, and do not re-ask answered ones. Draft supported parts while questions remain open, marking unresolved choices as questions rather than answers.
- A user story names an actor, a goal and its value. Cover materially affected perspectives, including the other party or operator when relevant; do not invent a separate story for an unchanged role. Use INVEST as a quality lens at the requested level: a high-level PRD need not contain sprint-sized stories. Preserve the PM's stated intent rather than inventing motives to fill a template.
- A flow shows observable actions in order, relevant initial state, branches and outcome. Include agreed exclusions and exception paths, including behavior when a required check fails; an undecided exception stays an open question. Apply MECE to alternatives at the same decision and to final outcomes of the same event; perspectives of different roles may overlap. Check absolute promises against accepted exceptions before handing off the first draft.
- Requirements state expected behavior, not guessed architecture; acceptance examples make that behavior testable.
- Before simplifying a requirement table, identify each row's intended acceptance result at the requested level of detail. Propose splitting distinct workflow steps only to resolve a concrete reading or acceptance problem. Separate pass/fail checks alone do not justify separate rows. Keep conditions and exceptions with their behavior. Preserve PM-approved bundles.
- Keep the selected solution, stories, flows, requirements, and risks synchronized. Reuse requirement IDs when behavior remains; retire obsolete branches. A function's priority and the conditions required whenever it ships are separate. Mark new priorities as proposals when the PM has not chosen them.
- Follow the document's existing tables, labels, order, and density. Where useful, put requirement, criterion, priority, and open status together in one table. Merge overlapping risks in the existing risk table and update mitigations when the mechanism changes. Retain units, dates, and sources for metrics; do not present projected impact as measured impact.
- If the PM authorized changes to the working document, re-read it immediately before each edit batch and preserve concurrent changes. For Confluence, use the current storage XHTML, check unique edit anchors and XML validity, compare body as well as version, then re-read the published page to verify tables, links, and consistency. Keep edit tokens and response headers out of Git and snapshots.
- Reconcile each requested comment as implemented, already satisfied, superseded by a newer instruction, or still awaiting a named decision. Resolving or replying to comments is a separate action and requires its own authorization.
- When replies are authorized, answer in the original thread with the concrete document change and its section or requirement ID. Distinguish an implemented edit from a decision that remains open. Read back the replies; leave comment status unchanged unless closing it was also requested.

## Finish

State what changed or what the audit found, cite the document evidence, and name only decisions that remain open. Verify claims against the final document. Keep case-specific channels, timings, values, and scope decisions in that PRD, not in this reusable skill.

Before posting a handoff with Confluence links, save its exact text to a temporary file. For each Confluence page referenced, take its canonical URL from the source. If it has a `/spaces/.../pages/{id}/{title}` path, run `python3 scripts/check_document_links.py '<canonical-url>' '<text-file>'` from this skill's directory. Fix every failure before posting. The check compares links with the source URL; it does not test network access. Run `python3 scripts/check_document_links.py --self-test` when changing the checker.
