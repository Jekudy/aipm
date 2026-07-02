<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# aipm — AI-for-PM working system

Helping Avito product managers use AI tools (Claude Code, Codex, ChatGPT Pro) across the flow **from "signal received" to "quarter planned"**. This folder is the **project-management + design layer** (specs, model, tracking). The runnable plugin (`pm-flow`) is built downstream from these specs.

## Read order
1. `~/.claude/CLAUDE.md` → 2. `~/Vibe/CLAUDE.md` → 3. this file → 4. **`STATE.md`** (where are we right now).

## Purpose
Build a plugin that: takes a PM's signal + messy material → maps it onto a known doc structure → scores quality → surfaces white spots → routes tasks (PM vs analyst) → iterates until ready → promotes to backlog → plans the quarter. Prototyping and the AI-analyst are built by **other teams** (we may consume them) — out of our scope.

## Non-negotiable model (read `docs/model-axes.md`)
- **M** = maturity/build-state of OUR tooling (M0–M5). Lives ONLY in the GitHub Project. Never in files/frontmatter.
- **Q** = quality/depth of the OUTPUT ("how well it solves the task", Q0–Q4). Lives ONLY as a runtime rubric in `components/*/SPEC.md`.
- **M ⟂ Q.** Never merge them.
- **Lazy fractal:** detail exactly one level down, only for the active component. Far components stay coarse M0 stubs.
- **Container discipline:** component SPECs are containers to pour real work into — never auto-generate prose to fill a gap (that's the neuroslop failure).

## Structure
```
STATE.md                     ← single source of "where are we now"
VISION.md                    ← what/why, scope, non-goals
docs/
  model-axes.md              ← M / Q / decomposition (LOCKED)
  architecture.md            ← pm-flow plugin architecture (v1 = prompt-only)
  ROADMAP.md                 ← coarse, wave-based (near detailed, far sketched)
  github-project.md          ← tracking = GitHub Project #5 (axis M)
  boardmix.md                ← workflow visualization (repo → board render)
  reference-digest.md        ← cited real-practice grounding + critique changelog
components/
  opp-doc/SPEC.md            ← ACTIVE (M1): 12-section container + Q-rubric + white-spots
  context-collection/SPEC.md ← coarse M0 stub
  solution-doc/SPEC.md       ← coarse M0 stub
  backlog-manager/SPEC.md    ← coarse M0 stub
  planning/SPEC.md           ← coarse M0 stub
```

## Language policy
- **PM-facing output = Russian**: gap reports, targeted questions, Q-rubric descriptors the PM reads, gap-report template. End users are Russian-speaking Avito PMs.
- **Machine/instruction layer = English**: SKILL.md bodies, architecture, specs' structural skeleton, CLAUDE.md, STATE.md, briefs.
- **PRD.md consciously waived**: the cross-phase-contracts role of the playbook's PRD.md is fulfilled by `docs/architecture.md#Interfaces` (doc contracts: intent + invariants + acceptance criteria). Don't create a hollow PRD template — that's container-discipline violation.

## Tracking & visualization
- **What/status:** GitHub Project #5 → https://github.com/users/Jekudy/projects/5 (component × M-status × Wave).
- **How/workflow:** Boardmix (see `docs/boardmix.md`). Source of truth = this repo; board = a render.

## Control command center
- AI for PM working group (Mattermost) + ИИпродакт channel (Telegram).
