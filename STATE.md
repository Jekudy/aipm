<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# STATE — where are we right now

_Last updated: 2026-07-04. This is the single source of truth for "what stage, which component, which tasks, which done-criteria." Update it every session._

## Stage
**Этап 1 (Wave 0): Architecture lvl1 ∥ Opp Doc lvl1 — DESIGN DONE, build pending.** The 2026-07-04 reconciliation merged the ChatGPT design line (docs/architecture/*, docs/opportunity-doc-plugin/* — now SUPERSEDED source material) with the repo canon. Reviewed target solution + build handoffs exist. **Этап 2 = Opp Backlog lvl1** (SPEC designed now, build after stage 1).

## Canon reading order (new sessions)
1. `docs/target-solution.md` — reviewed North-Star frame (куда идём).
2. `docs/model-axes.md` — M ⟂ Q ⟂ lvl + the r (work-item readiness) addendum.
3. `docs/architecture.md` — plugin architecture: router-lite, interfaces (incl. context-file contract), state model.
4. `docs/design-log/2026-07-04-reconciliation.md` — locked decisions D-1…D-6 + conflict register C1…C20.

## Mega-scenarios (North Star, from 2026-07-02 inter-module session)
The plugin exists to close three PM pains:
1. Нет достаточно качественного **Opportunity Doc** → хочет его получить.
2. Нет достаточно качественного **PRD** → хочет его получить. (**PRD = зрелый Solution Doc** — one module, its target output is called PRD.)
3. Нет поспринтово корректно спланированного **квартала** для диско → хочет его получить.

~10 entry scenarios reduce to ONE pattern: **diagnose where the PM is in the cycle → route to a module**. The router (router-lite lvl1) is part of the Architecture module — normative description in `docs/architecture.md#Skill layout`.

## Active tracks
- **Track A — Architecture lvl1**: reconciliation DONE (2026-07-04): router-lite specced, interfaces expanded (router→opp-backlog READ, context-file contract single home, transition gates c1–c5), r addendum in model-axes.md. Remaining: router-lite gets BUILT inside the stage-1 skill.
- **Track B — Opp Doc lvl1**: build handoff ready → `docs/handoffs/stage-1-opp-doc-lvl1.md` (supersedes the old brief). Ingest of ≥3 real example docs still pending (M2→M3 gate).
- **Track C — Opp Backlog lvl1 (Этап 2)**: lvl1 SPEC designed (`components/opp-backlog/SPEC.md`, card schema = single owner). Build handoff ready → `docs/handoffs/stage-2-opp-backlog-lvl1.md`. Build starts after stage 1 hand-back.

## Sessions (how we split work across windows)
| Session | Root | Owns | Brief | Status |
|---|---|---|---|---|
| **Orchestrator** (this) | `~/Vibe/products/aipm` | STATE.md, canon docs, design-log, GitHub Project, review | — | active |
| **Ingest** | `~/Vibe/products/aipm` | `components/opp-doc/examples/` (filled real docs) | `docs/sessions/ingest-brief.md` | ready to launch |
| **Stage 1 build** | `~/.claude/local-plugins/pm-flow/` | the pm-flow plugin (opp-doc lvl1 + stubs) | `docs/handoffs/stage-1-opp-doc-lvl1.md` | ready to launch |
| **Stage 2 build** | `~/.claude/local-plugins/pm-flow/` | skills/opp-backlog lvl1 | `docs/handoffs/stage-2-opp-backlog-lvl1.md` | blocked on stage 1 hand-back |

Non-orchestrator sessions never edit STATE.md; they hand results back and the orchestrator updates it (stage handoffs define the hand-back protocol).

## Module maturity (mirror of GitHub Project #5 — authoritative M lives THERE)
| Module | M | Wave | Note |
|---|---|---|---|
| Architecture & contracts | **M1** | W0 (now) | Router-lite + interfaces + gates hand-mapped in `docs/architecture.md`. M2 when embedded in the built skill. |
| Opp Doc | **M1** | W0 (now) | Container + rubric frozen; build spec = stage-1 handoff. M1→M2 = execute the handoff. |
| Opp Backlog | **M1** | Этап 2 | lvl1 SPEC hand-designed (2026-07-04): card schema, match keys, admission rules. M1→M2 = execute stage-2 handoff. GH Project: advance M0→M1. |
| Context collection | M0 | later | Module stays M0, but the context-FILE contract is FIXED (single home: `docs/architecture.md#Interfaces`) — no refactor when the module activates. |
| Solution Doc (→ PRD) | M0 | later | Reserved vocabulary: sol-s0..s2 / prd-r1..r3. Detail after Opp Doc emits first ranked options. |
| Solution Backlog | M0 | later | `docs/solution-backlog.md` is already a WRITE-ONLY contract target in Этап 1 (admission invariant live). |
| Planning | M0 | later | Reserved vocabulary: bet types, delivery_mode, 5 intent types. Detail LAST. |

## Wave 0 deadline (from 2026-07-02 grill)
**First run of the user's own real signal through the opp-doc skill by 2026-07-16.** Existential done-criterion (dogfood; anti-burnout anchors in task 4).

## Current tasks & done-criteria
0. ~~Track A: reconcile ChatGPT architecture/levels findings.~~ **DONE 2026-07-04** (target-solution.md + canon edits + design-log).
1. **Execute stage-1 handoff** (`docs/handoffs/stage-1-opp-doc-lvl1.md`): build the prompt-only pm-flow opp-doc lvl1 skill (M1→M2). Done = handoff's done-criteria + smoke tests pass, hand-back recorded next to the handoff. _Owner: stage-1 build session (Fable)._
2. **Ingest ≥3 real Opp Docs** into `components/opp-doc/examples/` (M2→M3 BLOCKING gate: false-ABSENT rate of the white-spot detector). _Owner: user + ingest session._
3. **Execute stage-2 handoff** (`docs/handoffs/stage-2-opp-backlog-lvl1.md`): build opp-backlog lvl1 (M1→M2). Blocked on task 1 hand-back. _Owner: stage-2 build session (Fable)._
4. **Set external anchors (anti-burnout).** Done = (a) public commitment in the Mattermost working group («покажу первый прогон 16.07»), (b) named co-owner in the GH Project Owner field. _Owner: user._
5. **GitHub Project #5**: advance Opp Backlog M0→M1; add Этап-2 wave column/label. _Owner: orchestrator._

## Blocked on
- ≥3 real Opp Docs (for the M2→M3 calibration gate).
- Stage-1 hand-back (for stage 2 start).

## Decisions locked
- M ⟂ Q ⟂ lvl (`docs/model-axes.md`) **+ r = work-item readiness as a DERIVED projection** (r addendum, 2026-07-04): r0–r3 computed from the Q profile + decision state; dated, demotable; never "maturity", never in GH Project.
- Orchestrator decisions D-1…D-6 + conflict resolutions C1…C20: `docs/design-log/2026-07-04-reconciliation.md`. Highlights: r3 ≡ promotion gate (canon NOT tightened); solution-backlog.md = write-only target in Этап 1; dedupe = router executes / opp-backlog owns match keys; candidate generation only on explicit PM request post-r3, cap 1–3; card status enum authoritative, frozen S0 enum untouched.
- v1 = prompt-only. Container discipline. Lazy fractal. State = plain Markdown at a PM-supplied path.
- Tracking = GitHub Project #5. Boardmix = render of the repo.
- Language: PM-facing output Russian; machine/instruction layer English.
- Этап 1 = Architecture lvl1 + Opp Doc lvl1; **Этап 2 = Opp Backlog lvl1** (re-scoped 2026-07-04 by user, overrides "detail at Opp Doc M3+").
- PRD.md waived: `docs/architecture.md#Interfaces` plays the cross-phase-contracts role.

## Next move
Launch the stage-1 build session against `docs/handoffs/stage-1-opp-doc-lvl1.md` → dogfood the user's own signal through it (deadline 16.07) → ingest real docs for M3 calibration → stage-2 build.
