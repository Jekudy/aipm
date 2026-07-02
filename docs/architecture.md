<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Plugin architecture — pm-flow (v1 = prompt-only)

## Overview

One Claude Code plugin, pm-flow/, packaged the standard way: only plugin.json in .claude-plugin/; skills/ at plugin root. V1 IS PROMPT-ONLY — no Python engine, no subagent forking, no runtime dependency, no structured-output requirement. The diagnosis logic lives as a prompt in opp-doc/SKILL.md that reads the doc, maps fragments to sections, scores Q, reports gaps. Only opp-doc is fleshed out (M2); the other four are ~100-token M0 stubs that cost nothing until activated. The 'engine' is a shared DIAGNOSIS reference (opp-doc/references/), reused only by the two doc components (Opp Doc, Solution Doc) — NOT by Backlog or Planning, which are different operation shapes. State is a plain Markdown file at a PM-supplied path; git is one possible carrier, not required. Isolation for parallel PMs is free: separate folders/repos, and the only interface between components is a committed doc-contract file (intent + invariants + acceptance criteria). Deferred-infra backlog (add only when the prompt-only path measurably fails on a REAL doc): (1) Python parse+score scripts — add when specific deterministic logic proves repeated; (2) deterministic V(quote,source) string-match + Pydantic-validate-retry — add when the judge actually fabricates quotes; (3) context:fork subagent scoring — add when a real doc measurably floods context. All three are M4+ scaling concerns; M3 (tested on real cases) comes first, and the smallest testable v1 is a prompt.


## Skill layout

### skills/opp-doc/ (M2, the ONE active component)
Lean SKILL.md body (~1500-2000 words), PROMPT-ONLY. Auto-invocable on triggers ('signal received', 'opportunity doc', 'map my discovery'). argument-hint '[doc-path]' — PM supplies the path to their plain-Markdown doc wherever they keep it. Body = the 6-step diagnosis loop run as a prompt (load doc -> map fragments to sections by the QUESTION each answers -> quote-check inline -> score Q per section -> detect grounded white-spots -> emit gap report leading with what mapped, then ranked questions routed PM/analyst -> write updated doc + task split back to the same path). Points at references/, inlines nothing. Mutations gated behind manual /name so Claude never auto-clobbers carried state.

### skills/opp-doc/references/opp-doc-spec.md (the CONTAINER)
Frozen 12-section schema the PM pours existing ChatGPT work into (Section 0 Header through 11 Recommendation). The Cagan/Amazon 12-section list is the TARGET SCHEMA; Torres OST 4 levels (Outcome/Opportunities/Solutions/Assumptions) is the SEPARATION DISCIPLINE nested inside it — specifically enforced at Sections 4/1/8/9 — NOT a competing spine. States explicitly which is schema and which is nested discipline so the diagnosis has one target structure.

### skills/opp-doc/references/opp-doc-rubric.md (the Q-RUBRIC + white-spot triggers)
One block per section: the Q0-Q4 rungs (Section 0 uses a plain presence checklist, not graded rungs) + white-spot triggers + a length-neutrality clause. Machine-facing note: multi-construct rungs (e.g. Section 8 Q2 'distinct+traced+compared+ranked') MUST be split into separate one-criterion-one-failure-mode checklist items when scored — SKILL prose can stay narrative. Hand-authored (M1), frozen, never regenerated at runtime. Editable without touching skill code.

### skills/opp-doc/references/gap-report.tmpl.md (output template)
Renders the diagnosis: present sections FIRST (what mapped successfully), then per-section Q badges (present/partial/absent/fabricated-removed), doc-level conjunctive gate Q, ranked white-spots each phrased as one targeted question routed PM-vs-analyst, and the tasks split. Anti-slop UX rule baked in: never a bare ABSENT badge-wall.

### skills/solution-doc/ (M0 stub)
SKILL.md = frontmatter + one-paragraph coarse stub only, ~100 tokens. Reuses the SAME diagnosis reference shape (new spec+rubric, no new logic) when activated. Ends in intent + invariants (EARS-ubiquitous) + acceptance criteria (EARS/Given-When-Then). Not designed now.

### skills/backlog-manager/ (M0 stub)
Coarse M0 stub. NOT a diagnosis component — a mutate/re-rank operation over the backlog stores (docs/opp-backlog.md, docs/solution-backlog.md). Likely mostly disk-state convention + manual-invocation-gated writes, may need no engine at all. Not designed now.

### skills/planning/ (M0 stub)
Coarse M0 stub. NOT a diagnosis component — a decompose/sequence operation over consumed inputs (IKR desired-state -> backward decomposition -> vertical-slice waves). Consumes Context + Solution-Backlog outputs. Not designed now.

### skills/context-collection/ (M0 stub)
Coarse M0 stub. Will fix a PM's context (backlog locations, channels, yearly goals, key metric + counter-metrics). Feeds the Opp Doc success-criteria section. Not designed now.

## Shared diagnosis engine (reference, not a running process)

Reused ONLY by the two doc components (Opp Doc, Solution Doc). Steps:

0. STEP 0 - LOAD FROZEN ARTIFACTS: read the 12-section schema + locked Q-rubric + white-spot triggers from opp-doc/references/ (hand-authored, never regenerated per call). Swapping only these three artifacts is what lets the SAME diagnosis prompt later serve Solution Doc.
1. STEP 1 - MAP: read the PM's plain-Markdown doc at the supplied path and place each fragment into the closest section BY THE QUESTION IT ANSWERS, not by heading text. Keep the PM's own wording. Content that fits no section goes to an 'unmapped' bucket to ask about, never discarded or force-fit. Never auto-generate prose to fill an empty section. (Prompt-only; no constrained decoding required — structured output is an optional optimization if the platform exposes it, with prompt-mapping as the default.)
2. STEP 2 - QUOTE-CHECK (inline, prompt instruction): every mapped claim must carry a verbatim quote from the PM's source; if the quote can't be found, drop the claim and mark the section a gap. (Deterministic V(quote,source) string-match enforcement is deferred backlog — add only if the judge actually fabricates in practice.)
3. STEP 3 - SCORE Q PER SECTION: score one criterion at a time on the Q0-Q4 evidence ladder, length-neutral. Report Q as the rung + 'X of J items present', never a raw model-confidence %. Do not mega-prompt all sections in one anchored pass.
4. STEP 4 - DETECT WHITE-SPOTS (grounded absence, GLOBAL rule): a gap = a required item whose scan over the PM's ACTUAL material returned nothing. Mark ABSENT (real white-spot, cited from the scan) vs AMBIGUOUS (hinted, needs PM confirmation) SEPARATELY — this ABSENT/AMBIGUOUS split applies to EVERY section's triggers, not just Section 5. Never assert a gap from 'docs like this usually lack X' (parametric belief is poorly calibrated; only scan-based absence is trustworthy).
5. STEP 5 - ELICIT (Socratic, minimum): turn the top white-spots into the smallest set of targeted questions, ranked by information gain, each routed to PM or analyst and doing exactly one job (fill slot / challenge framing / surface assumption). Cap the count; never dump the whole gap list as questions.
6. STEP 6 - REPORT + CARRY STATE: render gap-report.tmpl.md leading with what mapped, then Q badges + doc-level conjunctive gate Q (min of mandatory sections) + ranked questions + tasks split PM-vs-analyst. Write the updated doc + report back to the PM's supplied path. Stateless between invocations; re-reads the doc file each pass.

## State model

State is a PLAIN MARKDOWN FILE at a path the PM supplies as an argument — kept wherever the PM already works (a folder, a repo, a synced drive). Git is ONE possible carrier, NOT required; this is the resolved lazy default, not an open question, because the carry-out/carry-in loop is the core UX and can't rest on a 'PMs use git' assumption for a non-engineer population. Claude Code starts every session with a fresh context window and skills don't share context, so the doc-under-construction IS the between-invocation memory. Convention in whatever folder the PM uses: opp-current.md (the doc being built = carried state, edited offline, re-fed each pass), opp-report-<n>.md (each pass's gap report = audit trail), opp-backlog.md + solution-backlog.md (contracts other components read). The skill re-reads the doc at invocation start (path passed via argument). Nothing is written to CLAUDE.md; no memory of prior runs. Round-trip: PM invokes with path -> skill reads current doc -> emits report + updated doc to the same path -> PM edits offline -> re-invokes. Minimal invocation surface: ONE command runs the whole pass (read->map->score->report->write); resume is automatic from the doc path — the PM never reasons about which sub-skill to fire. All mutations gated behind manual /name.


## Parallelism (2 PMs)

Two levels, both cheap and buildable-with-nothing. (1) CROSS-PM isolation: each PM works in their own SEPARATE FOLDER/REPO — not git worktrees (a git-power-user feature that contradicts the non-engineer population). Parallel PMs never touch the same files and never share live context; the only exchange is a committed doc-contract file (intent + invariants + acceptance criteria). That file interface is what lets one PM's Opp Doc feed another PM's Solution Doc or planning wave without collision. Composability is an ACCEPTANCE CRITERION, not an assertion: PM-A's promoted Solution option must be readable and actionable by PM-B's Solution Doc skill WITHOUT PM-A present — the solution-backlog.md entry's exact three-slot shape is the demonstrated hand-off. (2) WITHIN-SESSION isolation: DEFERRED. v1 scores inline. Subagent context:fork scoring is added only once a real doc measurably floods context — it is not in the v1 spec. No shared database, no lock server, no running process — parallelism is a property of the file layout.


## Interfaces (the ONLY way components talk — committed files)

- **opp-doc → solution-doc**: docs/solution-backlog.md — top-ranked Solution options promoted out of the Opp Doc, each carrying the three-slot contract. INTENT: 'after this ships, [outcome/metric] holds for [segment]' (from Sections 1+3+4). INVARIANTS: seeded from Section 4 counter-metrics + Section 9 viability/legal constraints, expressed as EARS-ubiquitous 'The <system> shall <always-true property>' (Design-by-Contract class invariants — always hold, distinct from per-scenario postconditions). ACCEPTANCE-CRITERIA SEED: from the promoted option's riskiest assumption (Section 8 Q4) + success target (Section 4), stubbed as EARS unwanted-behaviour ('If <trigger> then the <system> shall <response>') + event-driven ('When <trigger> the <system> shall <response>') so the Solution Doc inherits the correct precondition/postcondition/invariant shape, not a vague 'falsification condition'. solution-doc reads the file; the two skills never share live context.

- **opp-doc → backlog-manager**: docs/opp-backlog.md (problems/outcomes, NOT committed features — that separation keeps it from collapsing into a roadmap) + docs/solution-backlog.md. backlog-manager reads/refreshes these files; opp-doc appends promoted options and updates opportunity status. File is the only interface.

- **solution-backlog → planning**: docs/solution-backlog.md = ranked Solution options each with per-item intent + invariants + acceptance criteria. planning consumes these as wave contents; each wave boundary is itself an intent+invariants+acceptance-criteria contract so two PMs own parallel waves without collision.

- **context-collection → opp-doc**: A context file (yearly goals + key metric + counter-metrics + backlog locations) that populates the Opp Doc success-criteria section. opp-doc reads it; if absent -> white-spot kicked back to context-collection. Same three-slot contract shape so it composes.

- **opp-doc / solution-doc → shared diagnosis reference**: Reference contract (NOT a running engine): INPUT = (PM's plain-Markdown material at a path, frozen section schema, locked Q-rubric, white-spot triggers). OUTPUT = per-section {mapped_content, status, evidence_quotes, Q-rung, gaps split ABSENT/AMBIGUOUS, targeted_questions}. Instantiated per doc-component by swapping ONLY the three frozen artifacts. Backlog and Planning do NOT use this contract — they are different operation shapes.

## Extensibility

The extensibility seam is trivial and requires NO architectural change: to promote a far component from M0 you (1) flesh out that component's skills/<comp>/SKILL.md body + write its references/ (schema + Q-rubric + white-spot triggers), (2) for the two DOC components reuse the SAME diagnosis prompt shape (new frozen artifacts, no new logic); Backlog and Planning get their OWN coarse mechanisms since they are not diagnosis-shaped, (3) advance its M in the external GitHub Project. The on-disk state convention and the doc-contract interface are already fixed. Two axes stay in separate homes and never mix: M (build-maturity of OUR tooling, M0..M5) lives ONLY in the GitHub Project — never in skill frontmatter (a skill has no native notion of its own maturity; encoding it re-introduces the fractal we keep lazy); Q (output quality) lives ONLY as the per-section rubric in references/, applied at runtime. The far four skills as ~100-token stubs is progressive-JPEG enforced by file layout, not discipline — there's no spec there to load, so nobody has to remember 'don't design them yet'.


## Open questions (empirical, resolve on real docs)

- Diagnosis prompt calibration is a BLOCKING M2->M3 gate, not a parked question: the opp-doc-rubric must be run against >=3 real ChatGPT Opp Docs and its false-ABSENT rate checked before the white-spot detector is trusted — an uncalibrated gap detector is itself the neuroslop risk. Who authors the first rubric and against which real docs.
- Doc file format: free-form Markdown (friendlier to pour existing work into) vs light front-matter + section headers (easier to map reliably). v1 defaults to free-form + map-by-question; revisit only if mapping proves unreliable on real messy pastes.
- Whether ANY of the three deferred-infra items (Python scripts, deterministic quote-verify, subagent fork) is ever actually needed — resolved empirically by the first real docs, not designed up front. Each stays in backlog until a real failure demands it.
