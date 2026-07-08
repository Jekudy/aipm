<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Hand-back: team-digest module added to pm-flow (2026-07-06)

Non-orchestrator session (avito working dir, owner-directed). STATE.md intentionally
NOT edited — orchestrator to fold this in.

## What was done
- **New skill `pm-flow/skills/team-digest`** (engine, generic) + `references/config-schema.md`
  (workspace contract). Plugin version bumped 0.1.2 → **0.2.0** in both manifests.
- **`components/team-digest/SPEC.md`** written (as-built; module was developed and
  live-tested in avito/TUT first, then generalized — inverse flow, flagged inside).
- TUT workspace stays at `~/Vibe/work/avito/.agents/skills/tut-weekly-digest/`
  (source-config.yaml + voice-guide.md + voice-examples.md); its old SKILL.md replaced
  with a thin redirect to `/pm-flow:team-digest`.

## Evidence of maturity
Three live iterations on real weeks (W26 test → owner corrections → W27 published to
tut-team + live-edit learning loop appended to voice-guide). Suggested M for GH Project:
**M2** (built + used on the owner's real data; no second-team instance yet).

## Orchestrator decisions needed
1. **Scope**: module is outside the 3 mega-scenarios (team communication). Accept as
   standalone entry or park? (Owner already decided to include; question is only
   router wiring + wave placement.)
2. **Module table**: add team-digest row to STATE.md + GH Project (suggested M2).
3. **Router**: not wired into router-lite; decide at next architecture pass.
4. **Prompt-only deviation**: collection uses subagent fan-out (documented in SKILL.md;
   trigger = 190KB single-source payloads, matching the architecture's "once a real doc
   measurably floods context" clause). Ratify or constrain.
5. **Markdown-only deviation**: workspace core config is YAML (`source-config.yaml`),
   while the context-file contract says "Markdown ONLY in v1". Battle-tested as-is;
   ratify YAML for this module or schedule a convergence.
6. **aipm/CLAUDE.md**: Structure block lists components/ without team-digest — update
   on fold-in.

## Verify
`/reload-plugins` (or `claude plugin update "pm-flow@pm-flow-marketplace"`) →
`/pm-flow:team-digest ~/Vibe/work/avito/.agents/skills/tut-weekly-digest` on a fresh week.
