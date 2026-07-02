<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# ROADMAP — coarse, wave-based

> Progressive JPEG: **Wave 0 is detailed, later waves are deliberately a sketch.** We re-detail the next wave only when the current one lands. Do not over-plan the far waves.

## Wave 0 — now (Opp Doc, first vertical slice)
Goal: one real signal goes through a thin Opp Doc diagnosis and a PM gets value.
- Opp Doc: M1 → M2 (build prompt-only skill) → M3 (tested on ≥3 real docs, false-ABSENT rate checked).
- Deliverable: the `pm-flow` opp-doc skill that maps → scores Q → reports grounded white spots → routes tasks.

## Wave 1 — next (sketch)
- Solution Doc: reuse the diagnosis prompt shape (new spec+rubric). Trigger = Opp Doc emits first ranked options.
- Context collection: detail once Opp Doc keeps hitting missing-context white spots.

## Wave 2 — later (sketch)
- Backlog manager: disk-state convention (opp-backlog.md, solution-backlog.md) once plain lists stop scaling.
- Planning: IKR desired-state → backward decomposition → vertical-slice waves + capacity/impact gate. Detailed LAST (consumes the others).

## Cross-cutting (every wave)
- Isolation/composability proven as an acceptance criterion (PM-B acts on PM-A's contract without PM-A present).
- Risks reviewed per wave.
