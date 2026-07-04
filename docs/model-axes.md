<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Model axes — M / Q / decomposition (LOCKED)

> The three meanings of "level" kept strictly apart. Never merge M and Q.

## M — maturity / build-state of OUR tooling

M = MATURITY / build-state of OUR tooling (the plugin skill/component the building team is developing). It answers one question only: 'How far is this tool from concept to routine operational use?' M is a MONOTONIC lifecycle progression about the ARTIFACT'S EXISTENCE, INTEGRATION, and USAGE-COUNT — never about whether its output is correct. Modeled on TRL (NASA readiness ladder) and CMMI staged levels, which measure ONLY build/adoption and deliberately exclude fitness. M lives in the GitHub Project as external metadata ABOUT each component; it is NEVER encoded in skill frontmatter or files. Clean-separation test: if a descriptor could be true of a perfectly-built tool that produces a WRONG answer, it is an M descriptor.


| M | name | meaning |
|---|---|---|
| **M0** | Not-studied | Component exists only as a coarse box/stub. Real practice for it has not been studied; no hand-map, no prompt, no skill. Default state of the far components (progressive-JPEG). ~100-token description in context, nothing more. |
| **M1** | Mapped by hand | Real, citable practice has been studied and the component's structure (section schema + Q-rubric + white-spot triggers) has been mapped BY HAND, on paper/in a spec. Not yet wired into any skill. The 'we understand it' gate. |
| **M2** | Built into prompt/skill | The hand-map is embedded into a runnable skill/prompt: SKILL.md + references/ (spec, rubric). Exists as executable tooling but has not yet been run on real cases. |
| **M3** | Tested on real cases | The skill has been run on real PM material and the output inspected; rough edges found and fixed. Proven to function end-to-end at least once on non-toy input — but not yet part of anyone's routine. For the Opp Doc rubric, the M2->M3 gate specifically requires calibration against >=3 real docs with false-ABSENT rate checked. |
| **M4** | In daily use by 1 PM | One real PM uses the component as part of their normal from-signal-to-plan flow. It has survived repeated real use by a single operator; integration into one workflow is proven. |
| **M5** | Used by several PMs | Multiple PMs use the component in parallel. Isolation/composability (separate-folder separation, doc-contract interface) is proven in practice, not just in design. Routine operational use across operators — the top of the readiness ladder. |

## Q — quality / depth of the OUTPUT

Q = QUALITY / depth of elaboration of the OUTPUT. It answers one question only: 'How well does this actually solve the posed task?' Q is a NON-MONOTONIC content score (it can REGRESS if the output degrades) applied FRACTALLY at every scope. Grounded in the evidence-tier / levels-of-evidence ladder (asserted -> structured -> data-backed -> validated/falsifiable), mirroring GRADE's 4-tier confidence scale and analytic-rubric norms (3-5 levels, one construct per row, observable descriptors, no 'good/better/best'). Q lives as a RUBRIC inside the component spec (references/), authored once and applied at runtime; NEVER stored in the GitHub Project. Clean-separation test: if a descriptor could be true of a rough draft that nonetheless NAILS the task, it is a Q descriptor. Every rung states what is PRESENT and what is MISSING (the missing part = the white-spot trigger). M and Q are ORTHOGONAL and cannot be the same axis: M only ever advances (lifecycle, lives in GitHub Project), Q can regress (content can be deleted/degraded, lives in a runtime rubric) — see orthogonality_examples for the four proof cases.


**Applies fractally at:** section (each doc section carries its own Q from its per-section rubric row); doc (the whole Opp/Solution Doc's Q, rolled up from its sections); skill/workflow (how well the plugin's skeleton+rubric actually diagnoses and surfaces gaps on real cases)


| Q | name | meaning |
|---|---|---|
| **Q0** | Absent | The element does not exist or is a placeholder: empty section, TODO, unattempted, or evidence-dropped-as-unverifiable. Nothing to score. The primary white-spot. |
| **Q1** | Asserted | The claim/section exists and is stated clearly, but rests on opinion / gut / anecdote only — no evidence tier above 'assumption'. Present: a statement. Missing: any grounding. (GRADE 'very low'; base of the evidence pyramid.) |
| **Q2** | Structured | Mapped correctly onto the target structure, internally coherent, assumptions made EXPLICIT, open questions and counter-metrics named — but still not externally grounded. Present: no white spots in the REASONING. Missing: external evidence. The minimum to start downstream work on the section (cut score). |
| **Q3** | Data-backed | Key claims supported by real data/observation: analytics, surveys, cohort analysis, support tickets, prior cases = correlational evidence. Present: the claim is grounded in reality. Missing: a disprovable test. (GRADE 'low/moderate'.) |
| **Q4** | Validated / Falsifiable | The core claim is expressed as a falsifiable hypothesis with pass/fail criteria defined BEFORE testing, and is either experiment-validated (A/B, prototype trial) or carries acceptance criteria a downstream team can test. Present: causal evidence OR a pre-committed falsification condition. Merely 'having metrics' — or merely being instrumented/traceable — is Q3, NOT Q4. (GRADE 'high'; top of the pyramid.) |

### Roll-up rule (the anti-slop mechanism)

DUAL rollup, gate-primary. PRIMARY (headline Q, the anti-slop mechanism) = CONJUNCTIVE weakest-link gate: doc-Q = min(Q of all MANDATORY sections). A doc cannot claim level T unless EVERY required section reaches T, so one missing or merely-asserted section caps the whole doc — this surfaces white spots and stops a strong section masking a hole (the 'confident slop hiding a white spot' fear; HEQCO explicitly warns against averaging across constructs). Optional sections are marked and do NOT gate. A section must reach at least Q2 to count as 'attempted' (cut score; from Definition-of-Ready: never start downstream work below Q2). For the Opp Doc the mandatory-gating set is Sections 0,1,2,3,4,5,6,8,9,11 (Section 0 IS mandatory — a doc with no owner/status breaks parallel-PM isolation); optional 7,10 gate only if attempted. SECONDARY (progress only, never headline) = COMPENSATORY weighted average, reported solely as 'X% toward the next gate'. The report always names the single lowest gating section — the actionable white spot and source of the auto-generated tasks-for-PM vs tasks-for-analyst. Same rule applies fractally at every scope.


## Lazy decomposition rule

LAZY / progressive-JPEG decomposition: expand exactly ONE level down, and ONLY for the currently active component (Opp Doc). Never pre-design the whole fractal. (1) The active component gets a real, full set NOW — 12-section schema + locked per-section Q-rubric + white-spot triggers, wired into a prompt-only skill at M2. (2) The far four components (Context, Solution Doc, Backlog, Planning) stay ONE coarse box each at M0 — a SKILL.md with only frontmatter + a one-paragraph stub (~100 tokens), no full spec, no rubric rows. (3) The generic evidence-tier Q ladder (Q0-Q4) IS reusable across all components; but per-section CRITERIA are component-specific and stay coarse for the far four — author rubric rows only when a component becomes active. (4) Promotion of a far component from M0 requires no architectural change: flesh out its SKILL.md + references/, reuse the SAME diagnosis prompt shape for the two DOC components (Backlog/Planning get their own since they aren't diagnosis-shaped), advance M in the GitHub Project. Progressive-JPEG is enforced by FILE LAYOUT (coarse stubs cost ~100 tokens until invoked), not by discipline. Detail near, sketch far.


## Orthogonality (M and Q cannot be the same axis)

- M high / Q low: the Opp Doc skill is at M5 (several PMs use it daily) but on a specific messy input it produces a section that is only Q1 (asserted, no evidence). The tool is fully built and adopted; the OUTPUT still poorly solves the task. Maturity of the tool says nothing about the quality of any single doc it helps produce.
- M low / Q high: a PM hand-writes an Opportunity Doc entirely in ChatGPT with real analytics and a falsifiable hypothesis — that DOC is Q4 (validated). But our Planning component that would consume it is still M0 (not-studied, a coarse stub). A high-quality output can exist for a component our tooling hasn't even mapped yet.
- M high / Q regresses over time: the Solution Doc skill reaches M4 (daily use by 1 PM), and a doc that was Q3 (data-backed) is edited and its evidence section deleted, dropping it to Q1. M is monotonic and stays at M4; Q moved BACKWARD. This is why Q lives in a runtime rubric (content can degrade) and M lives in the GitHub Project (lifecycle only advances) — they cannot be the same axis.
- Clean-separation test in action: 'is in daily use by 1 PM' could be true of a tool giving wrong answers -> M descriptor (M4). 'core claim expressed as a falsifiable hypothesis with pre-committed pass/fail' could be true of a rough first draft -> Q descriptor (Q4). Neither can be swapped to the other axis without collapsing the two into one.

## r — work-item readiness (addendum, 2026-07-04; ADDITIVE — nothing above is modified)

r = READINESS of a WORK ITEM (an opportunity moving from raw signal to decision). It is NOT a fourth stored axis: r is a DERIVED PROJECTION of the doc-level Q profile + the decision state, computed through the locked Q-rubric. It answers one question only: 'Where does this ITEM stand in its decision lifecycle?' — which neither M (build-state of OUR tooling) nor Q (one output's content score) expresses. Naming rule: ALWAYS 'readiness (r)', NEVER 'maturity' — maturity stays reserved for M; derived phrases follow (readiness assessment, readiness milestones — never 'maturity engine').

| r | name | derivation over the 12-section Opp Doc container |
|---|---|---|
| **opp-r0** | raw signal | Pre-doc intake state: a backlog card exists with signal + source + rough domain; no doc required, no Q derivation. Variant `r0-solution-signal` carries a problem-unknown flag. |
| **opp-r1** | framed | Framing sections S1 Problem, S2 Strategic fit, S3 Segment, S4 Success metrics each ≥ Q2. |
| **opp-r2** | evidence-backed | r1 AND evidence sections S5 Evidence, S6 Sizing each ≥ Q3, alternative explanations addressed. |
| **opp-r3** | decision-ready | Doc-level conjunctive gate ≥ Q2 on the mandatory set (0,1,2,3,4,5,6,8,9,11) AND S11 carries an explicit decision from the closed set {kill / park / continue-discovery / generate-solutions} AND S8 holds 1–3 candidates. Identical to the existing promotion gate — the locked canon gate is NOT tightened. |

Non-nesting note: the ladder is a set of NAMED MILESTONES on one dial, not strictly nested by construction — an r3 doc may hold S5 at Q2 without ever earning the r2 label; the gap report always names the blocking sections, so nothing is hidden.

Properties: r is derived, dated, demotable — re-computed every pass from the doc via the locked Q-rubric; a later pass MAY demote it (Q is non-monotonic; a filled-but-garbage section stays Q1 and cannot fake r). Never stored as machine state. readiness ≠ priority ≠ workflow status — three separate card facets, never merged: an item can be r3-but-unimportant or r1-but-strategically-urgent.

Homes: the backlog card caches r as a DATED CLAIM (`readiness: r2 (assessed 2026-07-04)`); optionally the doc's Section 0 header mirrors it. NEVER in the GitHub Project (that home belongs to M); NEVER as a second rubric (that would be a shadow Q violating single-source-of-truth).

Clean-separation test for r: the descriptor is about the ITEM's position in its decision lifecycle; it could be true of a doc our tooling never touched (→ not an M descriptor); it is recomputed from the doc's Q profile and never scored independently (→ not a second quality score). sol-s0..s2 / prd-r1..r3 stay NAMED but UNDEFINED (lazy fractal) — reserved vocabulary in contracts only.
