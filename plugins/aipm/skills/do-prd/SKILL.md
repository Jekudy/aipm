---
name: do-prd
description: Audit Avito PRDs and help write or update them from product decisions, user flows and review comments. Use to find concrete gaps or contradictions in a PRD, draft missing sections, or maintain the working document. Product discovery is a separate workflow when the problem itself is still unclear.
---

# do-PRD

The output is a current product document the PM and team can use. Work in the user's chosen document. A local Markdown draft is a review aid when requested, not a replacement for the working Confluence page.

## Choose the requested mode

- **Audit:** read the current document and comments; report concrete contradictions, missing decisions and unsupported claims with a short quote or section location, their consequence and the smallest proposed fix. Audit alone does not authorize publishing edits. Do not add a readiness gate or invent answers to make the document complete.
- **Writing assistance:** draft or edit the requested sections in the user's chosen artifact. Interview only for decisions that materially change the result; continue independent work while awaiting answers. Implement already authorized comments without asking for approval again.
- Keep a broad product goal distinct from the coverage of the selected mechanism. In analytics, separate users, periods, attempts and pairs; an attempt has one final outcome, while playback or delivery states are separate attributes.

## Establish the current source

- Read the owning project's document rules, current PRD, and relevant flows. Follow the project’s source-of-truth and snapshot rules.
- Fetch all review comments and replies, with pagination. When checking what changed, compare reply IDs as well as top-level comment IDs. Include resolved comments when they contain decisions. Keep IDs, quoted anchors, and exact requests in working notes; do not guess authors absent from the tool response.
- Distinguish an instruction to delete, an editorial request, a changed product decision, and a reopened question. A later explicit decision supersedes an older one; “discussable” reopens a value rather than approving a new value.
- Ask only about material ambiguity. Continue edits that do not depend on the answer. Existing authorization to implement the comments remains valid; do not add another approval ceremony.

## Keep the main PRD useful

- Match the existing language and density. Preserve the PM’s words where they express intent clearly. Do not replace a concrete product goal with an invented desire to understand the system's behaviour.
- A user story states actor and goal. Its flow shows observable actions in order, the relevant initial state, branches, and outcome. Keep buyer and seller perspectives distinct.
- Put a short comparison of real alternatives before the selected solution. Fold the reasons for choosing or rejecting a variant into its table row; avoid a second narrative repeating that table.
- The selected solution, stories, and requirements must describe the same mechanism and scope. Put stories before the requirements when that is the document’s agreed layout.
- Keep superseded plans and visions in source history or snapshots, not in the main narrative when the PM asks to remove them. Do not introduce process notes about who generated the text, what editing pass ran, or whether a paragraph is historical unless that information helps the reader make a current decision.

## Reconcile the requirements

- For each changed flow, update the affected requirement, scope, priority, and acceptance example. Check all occurrences: summary, alternatives, selected solution, stories, requirements, risks, and next steps.
- A requirement describes the expected result, not an architecture guess. Keep technical uncertainty in an actionable open question where needed; do not append a disclaimer to every product paragraph.
- Reuse requirement IDs where the behaviour still exists. Retire obsolete branches instead of leaving them looking selectable. Keep new priorities identifiable as proposals when the PM has not assigned them; choosing a function is not automatically a development-priority decision.
- Separate the priority of a function from mandatory conditions within it. A low-priority notification may still require deduplication and eligibility checks whenever it ships. Do not copy rules between different notifications without a source.
- Represent requirements and acceptance in one table with ID, area, criterion, MoSCoW, and status/open questions, adapting column labels to the existing document. Make branches separate rows when that helps comparison; do not repeat the priority list in story prose.

## Update risks without inventing progress

- Use one risk table. Put prevention, trigger, response, and owner in the relevant row; avoid a separate “plan for top risks” duplicating it.
- A changed mechanism changes risks and mitigations. Remove obsolete dependencies and fallback choices, merge overlapping risks where useful, and preserve genuinely different risks.
- Update stale dates and statuses from evidence. A decision about the mechanism does not prove that research, estimates, staffing, or integration are finished. Reuse established risk scores only for the same assessed risk and mechanism; mark changed risks for reassessment rather than carrying their old scores into a new mechanism. An unscored risk stays unscored.
- Domain metrics, counter-metrics, and related entities follow the owning project rules and available domain skills. Keep units and source dates intact; do not turn historical potential into measured impact.

## Publish and verify

- Use current Confluence storage XHTML for edits. Markdown rendering may flatten tables, macros, and links. Patch the current body with unique-match assertions and validate XML; preserve unrelated structure and links.
- Before writing, re-read the page. Comments can change inline anchors without incrementing the page version, so compare the body as well as its version. Merge concurrent changes; upload with the version read. Keep response headers and edit tokens outside snapshots and Git.
- Re-read the published document. Check section order, tables, links, remaining old branches, and consistency between flows and requirements. Record publication version and verification evidence in the existing worklog.
- Account for every requested comment: implemented, already satisfied, superseded by a newer instruction, or a specific unresolved decision. A reopened question is implemented by marking it open, not by inventing its answer.
- Do not claim all comments are addressed until the reconciliation is complete. Resolving comments or replying to people is a separate external action; do it only when authorized and supported by the tools.

## Improve this skill from use

Extract reusable editing rules from actual PM feedback. Keep feature-specific channels, timings, metric values, and scope decisions in their PRD. Do not generalize a one-off product decision into a rule for all documents. Apply a new rule to the current PRD before claiming it works.
