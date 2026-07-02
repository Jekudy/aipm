<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# STATE — where are we right now

_Last updated: 2026-07-02. This is the single source of truth for "what stage, which component, which tasks, which done-criteria." Update it every session._

## Stage
**Foundation complete → entering Wave 0.** Model locked, architecture drafted, tracking live, Opp Doc container ready to fill.

## Active component
**Opp Doc** (Wave W0 = now). Everything else is a coarse M0 stub (lazy fractal).

## Sessions (how we split work across windows)
Three roles, run in separate Claude Code windows. Ingest and Build are **independent → parallel**; they converge at the M2→M3 calibration.
| Session | Root | Owns | Brief | Status |
|---|---|---|---|---|
| **Orchestrator** (this) | `~/Vibe/products/aipm` | STATE.md, roadmap, GitHub Project, review | — | active |
| **Ingest** | `~/Vibe/products/aipm` | `components/opp-doc/examples/` (filled real docs) | `docs/sessions/ingest-brief.md` | ready to launch |
| **Opp Doc build** | `~/Vibe/products/aipm` | the `pm-flow` plugin (`~/.claude/local-plugins/pm-flow/`) | `docs/sessions/oppdoc-build-brief.md` | ready to launch |

No git worktrees: the three touch disjoint file trees (STATE vs examples vs the global plugin), so plain parallel windows suffice — worktrees of the whole Obsidian vault would be over-engineering. Non-orchestrator sessions never edit STATE.md; they hand results back and the orchestrator updates it.

## Component maturity (mirror of GitHub Project #5)
| Component | M | Wave | Note |
|---|---|---|---|
| Opp Doc | **M1** | W0 (now) | Hand-mapped: 12-section container + Q-rubric + white-spots. Next: build the prompt-only skill (M1→M2). |
| Context collection | M0 | later | Detail once Opp Doc ~M3 keeps asking for missing context. |
| Solution Doc | M0 | later | Detail right after Opp Doc emits its first ranked options. |
| Backlog manager | M0 | later | Detail once backlog files stop scaling as plain lists. |
| Planning | M0 | later | Detail LAST — consumes the other four. |

## Wave 0 deadline (from 2026-07-02 grill)
**First run of the user's own real signal through the opp-doc skill by 2026-07-16.** This is the existential done-criterion: the project's #1 risk is the user (sole engine) switching away; historically his projects survive only when living users wait. First living user = the user himself (dogfood). Plan for 1 week of work (x2 estimation rule).

## Current tasks & done-criteria
1. **Pour ChatGPT Opp-Doc work into `components/opp-doc/SPEC.md`.** Done = your existing material mapped onto the 12 sections; conflicts reconciled (map by the QUESTION each section answers). _Owner: user + Claude._
2. **Build prompt-only `pm-flow` opp-doc skill (M1→M2).** Done = a SKILL.md running the 6-step diagnosis loop against the frozen spec/rubric. _Not started._
3. **Collect ≥3 real Opp Docs for calibration (M2→M3 BLOCKING gate).** Done = false-ABSENT rate of the white-spot detector checked on real docs. The user's own dogfood docs count. _Blocked on: real docs._
4. **Set external anchors (anti-burnout).** Done = (a) public commitment posted in the Mattermost working group ("покажу первый прогон 16.07"), (b) a named co-owner from the group in the GH Project Owner field. _Owner: user._

## Blocked on
- User's ChatGPT Opp-Doc dump (for task 1).
- ≥3 real Opp Docs (for the M2→M3 calibration gate).

## Decisions locked
- M ⟂ Q (`docs/model-axes.md`). Lazy fractal. Container discipline.
- v1 = prompt-only (no Python/subagents/infra until a real doc demands it).
- State = plain Markdown at a PM-supplied path; git optional.
- Tracking = GitHub Project #5. Boardmix = render of the repo.
- Language: PM-facing output in Russian; machine/instruction layer in English (see CLAUDE.md).
- PRD.md waived: `docs/architecture.md#Interfaces` plays the cross-phase-contracts role (no hollow templates).
- Boardmix API check dropped (stays as deferred note in `docs/boardmix.md`); `Owner` field in GH Project filled when the second PM joins.

## Next move
Fill the Opp Doc container with your ChatGPT work → then build the prompt-only skill → then calibrate on real docs.
