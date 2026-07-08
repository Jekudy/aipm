<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# team-digest — SPEC (lvl1)

**Status note:** built BEFORE this spec (inverse of the usual flow) — the module was
developed and battle-tested in the TUT/avito project (3 live iterations, one published
post, one live-edit learning loop), then generalized into the plugin. This SPEC records
the as-built contract. M-state lives in the GitHub Project only.

## Purpose

Weekly team digest: the skill autonomously collects "what happened" from configured
sources, filters to real shifts, asks the PM 3-5 targeted questions, drafts in the PM's
distilled voice, and publishes to the team channel behind an explicit human gate.
Replaces the crowdsource-collection step of the manual ritual (team no longer has to
feed facts into comments); keeps the human where humans are irreplaceable: meaning and
go/no-go.

**Scope note (orchestrator attention):** this module sits OUTSIDE the three mega-scenarios
(opp doc / PRD / quarter) — it is a team-communication module. Added by owner decision
2026-07-06 («положим туда скилл для работы над дайджестом»). Router wiring: NOT wired
into router-lite (invoked directly); decide at next architecture pass whether it stays
a standalone entry.

## Engine ⟂ config (the module's core split)

- **Engine** = `pm-flow/skills/team-digest/SKILL.md` — generic, zero team hardcode.
- **Workspace** = PM-supplied directory (contract:
  `pm-flow/skills/team-digest/references/config-schema.md`): `source-config.yaml`
  (sources/boards/channels/roster/streams/exclusions), `voice-guide.md` (voice +
  anti-slop + editing lessons), `voice-examples.md` (few-shot).
- This mirrors the plugin-wide context-file contract (state = plain files at a
  PM-supplied path, re-read fresh, one command per pass). Reference instance: TUT at
  `~/Vibe/work/avito/.agents/skills/tut-weekly-digest/`.

## Pipeline (as built)

pre-flight probes → collect in subagents (Jira / MM channels / meeting-assist DM /
Confluence; raw payloads never enter the main context) → validator gates (ownership
check FIRST, then digest-worthiness, then stream/coverage) → evidence pack + clustering
(quarter-planning weeks lead with «Планирование Q{N}») → light grill (3-5 questions,
one message) → draft per voice-guide (delta/proof/so-what per bullet; team-accessible
links only; `display` naming «Имя П.») → health block + full-text preview + explicit
«ок» gate → publish → reply ritual + config-learning tail → **live-edit diff loop**
(PM edits the published post → skill diffs and appends lessons to voice-guide.md).

## Q — what a GOOD digest output means (runtime rubric, from live editing lessons)

- Events, not kitchen: decisions/artifacts/numbers-with-proof; NO process bullets, NO
  meta-Jira resolves, NO early futures, NO morals/interpretations.
- Political hygiene: no internal criticism of adjacent teams in a wide channel.
- Ownership-clean: zero facts belonging to other teams (the historically dominant
  failure mode).
- Voice-true: passes the workspace voice-guide checklist; people as «Имя П.»; honest
  «?» / deadline-dates; ≤6-8 streams, ≤4 bullets.
- Complete-honest: health block shows per-source counts and failures; a down source
  blocks silent publishing.

## Known limits / next

- meeting-assist DM is the richest decision source but is personal-scope; links must
  be re-pointed to team-accessible artifacts (enforced in the engine).
- Scheduling: pass is one-command; a standing Friday cron via `/schedule` is possible
  but the grill + publish gate remain human by design.
- Voice-guide bootstrap for a NEW team = style-distillation pass (documented in
  config-schema.md); not yet packaged as its own skill.
