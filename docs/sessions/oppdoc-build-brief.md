<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# SESSION BRIEF — Opp Doc build (v0 → v1, M1 → M2)

> Self-contained brief. You are a fresh session with no memory of the orchestrator chat. Boot from the files below, then follow this.

## Boot (read in order)
1. `~/Vibe/products/aipm/CLAUDE.md`
2. `STATE.md`
3. `docs/model-axes.md` (M ⟂ Q, Q0–Q4, conjunctive gate)
4. `docs/architecture.md` (pm-flow, **v1 = prompt-only**, the 6-step diagnosis loop, state model)
5. `components/opp-doc/SPEC.md` (the frozen container you implement against)
6. this brief

## Your role
Implement the **prompt-only** `pm-flow` Opp Doc skill that runs the diagnosis loop from `docs/architecture.md` against the frozen spec. This moves Opp Doc **M1 → M2** (built into a runnable skill, not yet tested on real cases).

## Plugin home (recommended default)
Build at **`~/.claude/local-plugins/pm-flow/`** (global — immediately dogfoodable via Claude Code, per the vault's global-plugin policy). Distribution/packaging for Avito is a **later** decision; do not solve it now. If you disagree, raise it with the orchestrator before building — don't silently pick product-local.

## Scope
**You OWN:** the plugin tree — `plugin.json` (in `.claude-plugin/`), `skills/opp-doc/SKILL.md` + `skills/opp-doc/references/` (frozen spec, rubric, gap-report template), and ~100-token M0 stubs for the far four skills.
**You do NOT touch:**
- `STATE.md` (orchestrator owns).
- The spec STRUCTURE/rubric — implement against it. Propose changes via a `## Spec-friction` note to the orchestrator, don't edit unilaterally.
- The ingest examples.

## Steps
1. Scaffold the plugin per `docs/architecture.md` (one plugin, `plugin.json` only in `.claude-plugin/`, `skills/` at root).
2. Write `skills/opp-doc/SKILL.md` (~1500–2000 words): frontmatter + argument-hint `[doc-path]` + the **6-step loop** (load frozen artifacts → map by question → quote-check → score Q per section → detect ABSENT/AMBIGUOUS white-spots → emit gap report + updated doc). Points at `references/`, inlines nothing. Mutations gated behind a manual `/name`.
3. Put the frozen artifacts in `references/`: `opp-doc-spec.md` (12 sections), `opp-doc-rubric.md` (Q0–Q4 per section + white-spot triggers, multi-construct rungs split into one-criterion items), `gap-report.tmpl.md` (leads with what mapped, then Q badges + doc-Q gate + ranked routed questions).
4. Far-four skills = frontmatter + one-paragraph stub only (~100 tokens each). Do NOT design them.

## Guardrails (hard)
- **v1 is PROMPT-ONLY.** No Python engine, no subagent forking, no runtime dependency, no structured-output requirement. All three deferred-infra items live in `docs/architecture.md`'s backlog — add ONLY when a real doc measurably breaks the prompt.
- **Container discipline + anti-slop report UX:** map, never backfill; report leads with what mapped, never a bare ABSENT badge-wall.
- State = plain Markdown at a PM-supplied path; re-read each invocation; nothing written to CLAUDE.md/memory.

## Done-criteria (M2)
- The skill runs the whole pass end-to-end (read → map → score → report → write) against the frozen artifacts on a sample doc, prompt-only, invocable via one command.
- Far-four stubs present at ~100 tokens.

## Next gate (NOT this session)
**M2 → M3** = calibrate on **≥3 real docs** (from the ingest session) and check the white-spot detector's false-ABSENT rate. Blocking before the detector is trusted.

## Hand back
Ping the orchestrator: "opp-doc skill at M2, plugin at <path>, ran on <sample>, spec-friction: yes/no." Orchestrator updates STATE.md + GitHub Project (Opp Doc → M2).
