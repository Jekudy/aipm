<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# SESSION BRIEF — Ingest (влив наработок)

> Self-contained brief. You are a fresh session with no memory of the orchestrator chat. Boot from the files below, then follow this.

## Boot (read in order)
1. `~/Vibe/products/aipm/CLAUDE.md`
2. `STATE.md`
3. `docs/model-axes.md` (M ⟂ Q, the Q0–Q4 ladder, the conjunctive gate)
4. `components/opp-doc/SPEC.md` (the frozen 12-section container + Q-rubric + white-spot triggers)
5. this brief

## Your role
Pour the user's **existing Opp-Doc work** (produced with ChatGPT and elsewhere) into the container — by mapping, not rewriting. Output = a real filled Opp Doc + a gap list. This doubles as a **calibration doc** the build session will later test the skill against.

## Scope
**You OWN:** `components/opp-doc/examples/<signal-slug>-v1.md` — the mapped/filled real doc, plus its gap list.
**You do NOT touch:**
- `components/opp-doc/SPEC.md` structure/rubric — it's FROZEN. If you find real friction (a missing section, a broken rung), write it under a `## Spec-friction (for orchestrator)` heading in your example file — do NOT edit the spec unilaterally.
- The plugin / `pm-flow` — that's the build session.
- `STATE.md` — the orchestrator owns it. Report back via your example file + a ping.

## Inputs
The user's ChatGPT Opp-Doc material (they will paste / point you at it). Ask for it if not provided.

## Steps
1. **Map, don't rewrite.** Place each fragment of the user's material into the closest of the 12 sections **by the QUESTION each section answers**, not by heading text. Keep the user's own wording.
2. **Extractive evidence.** Every mapped claim carries a verbatim quote from the source. If the quote can't be found, drop the claim and mark that section a gap.
3. **Score Q per section** on the Q0–Q4 ladder (length-neutral). Report the rung + "X of J items present", never a confidence %.
4. **Mark white spots**, distinguishing **ABSENT** (scan of the actual material found nothing) vs **AMBIGUOUS** (hinted, user must confirm). Never assert a gap from "docs like this usually lack X".
5. **Unmapped bucket.** Content that fits no section → an `## Unmapped` list to ASK about, never force-fit or discard.
6. **Report** leading with what mapped, then ranked white-spots as targeted questions routed **PM vs analyst**. Compute doc-Q = min(mandatory sections 0,1,2,3,4,5,6,8,9,11).

## Guardrails (hard)
- **Container discipline:** NEVER auto-generate plausible prose to fill an empty section. That's the neuroslop failure. Report the hole; don't backfill it.
- Q grades evidence-tier + completeness, not prose polish — with ONE exception: company-POV framing in Section 1 caps at Q1 (customer-voice is content, per Amazon/OST).

## Done-criteria
- ≥1 real Opp Doc mapped onto the 12 sections at `components/opp-doc/examples/`.
- Every gap marked ABSENT/AMBIGUOUS + routed to PM or analyst.
- Doc-Q computed via the conjunctive gate.
- Any spec-friction noted for the orchestrator.

## Hand back
Ping the orchestrator session: "ingest done, example at components/opp-doc/examples/<slug>-v1.md, doc-Q=Qn, N white-spots, spec-friction: yes/no." Orchestrator updates STATE.md and advances tracking.
