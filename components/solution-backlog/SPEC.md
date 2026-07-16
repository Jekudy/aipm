<!-- Root: ~/Vibe/CLAUDE.md — ALWAYS read it first for vault-wide rules and structure -->

# Solution Backlog — module SPEC (lvl1 scope contract)

> **Status: lvl1 RATIFIED & FROZEN — Phase-A gate approved by the user 2026-07-16.** M0 → M1 achieved; M advances ONLY in GitHub Project #5 — never in this file, never in skill frontmatter. This spec replaces the former M0 coarse stub and is the frozen contract for the stage-4 Phase-B build.
>
> **Schema ownership:** this SPEC is the SINGLE OWNER of the solution-backlog entry schema and its serialization. The two live writers — opp-doc (promotion append at its r3 gate) and solution-doc (`status`/`readiness`/`decision` write-back) — WRITE conforming entries; they never own or redefine the layout (solution-doc SPEC §Format-ownership rule 8 already says so). The normative three-slot interface text lives in `docs/architecture.md#Interfaces` (opp-doc → solution-doc); on any divergence about the SLOTS' meaning, the architecture interface wins; on any divergence about SERIALIZATION (field names, order, form), THIS file wins — that is exactly the layer canon leaves unowned.
>
> **Provenance:** this lvl1 is a REVERSE-RATIFICATION (stage-4 Phase A, 2026-07-16): the schema below was derived from what the two live writers actually produce on disk + the canon interface — not invented fresh. The writer-vs-writer-vs-canon drift register lives in `docs/handoffs/stage-4-phase-a-gate.md`; unreconciled writer drift is spec-friction, never silently patched (both writers are frozen for this stage).

## One-line intent

`docs/solution-backlog.md` is the DECISION QUEUE answering "which solutions/hypotheses deserve PRD / delivery / test" (distinct from the opportunity queue) — a store of promoted solution candidates, each carrying the three-slot contract, realized in v1 entirely as ONE committed plain-Markdown file plus prompt-driven, manually-gated mutations.

## lvl1 scope contract

### Intent

Hold promoted solution candidates across the full sol-r0–sol-r3 readiness range — freshly promoted, in-design, PRD-ready, held, dropped, archived — so that (a) nothing promoted gets lost, (b) the PM can view / manage / re-rank the queue, (c) the dated sol-r readiness claim + status + decision that the solution-doc pass produces are RECORDED here, and (d) Planning (M0, later) can consume `prd_ready` entries as wave contents. NOT diagnosis-shaped: no Q-rubric, no readiness derivation — this module records given claims.

### Invariants (EARS-ubiquitous)

1. The solution backlog shall be a single committed plain-Markdown file (`docs/solution-backlog.md` at a PM-supplied path) — no JSON store, no table store, no database. Entries live INSIDE the file as fenced YAML blocks (the block is content of the .md file; the store MEDIUM is unchanged — canon invariant kept).
2. The solution backlog shall accept no entry without a parent opportunity AND a product hypothesis (if-then-because shape) — «не помойка идей»; a bare «сделать ai-помощника» may not enter (canon admission invariant, `docs/architecture.md#Interfaces`).
3. There shall be exactly ONE canonical entry serialization (§Entry schema below); every writer — the opp-doc promotion append, the solution-doc write-back, and this module's own ops — shall write it; any divergence found in live writes is spec-friction to record, never a second admitted form (the opp-backlog "two serializations" defect is the named failure this guards against).
4. All mutations of the backlog file shall be gated behind manual invocation with a full-inventory confirmation (S-1) — no auto-mutations, ever.
5. The `readiness` field shall be a DATED, DEMOTABLE claim from the single ladder `sol-r0..sol-r3`, produced by the solution-doc diagnosis pass (`sol-rN (assessed <date>)`) or assigned as the floor at promotion (`sol-r0 (promoted <date>)`); this module RECORDS the claim and shall never derive, re-score, or negotiate it — in either direction; NEVER called "maturity".
6. Entry facets shall never merge: `status` ⟂ `decision` ⟂ `readiness` ⟂ priority data (`rank`/`pm_priority`). In particular `hold`/`drop` are DECISION values legitimate at any rung and shall never auto-map to `status: archived`.
7. Priority data shall carry NO computed or aggregate score (false-precision guard, mirror opp-backlog invariant 6): `rank` is written only from an explicit PM ordering; a PM's own prioritization model (MoSCoW, RICE, anything) shall be stored VERBATIM in `pm_priority` — never converted, never aggregated, never silently dropped (foreign-prioritization passthrough, stage-2 real-wave R2).
8. No entry field shall be auto-defaulted or synthesized: a missing value is elicited from the PM or stays an explicit gap; a PM-declared lifecycle outcome shall never be silently overwritten by a default-alive state (stage-2 real-wave S2/S3 lessons, day-one).
9. Two-tier enforcement shall hold at the Planning boundary: a below-gate entry MAY live in the backlog, but `status: prd_ready` shall be written ONLY by the solution-doc pass at its sol-r3 gate — never by this module, never by PM assertion.

### Acceptance criteria (lvl1)

- A candidate promoted by opp-doc lands as ONE conforming entry (all mandatory keys, §Entry schema) appended to the file.
- A solution-doc write-back (dated `readiness` + `status` + `decision`) lands conformingly on the existing entry — including a DEMOTE (e.g. sol-r3 → sol-r2 with a fresh date and `status` dropping from `prd_ready`); a build where the claim can only go up is a failed build.
- A manual PM entry (out-of-promotion) passes the admission invariant or is REFUSED with the verbatim Russian guard that also ROUTES (§Admission rules) — spoken once per block, never a wall of repeats.
- An already-decided legacy row (e.g. «сделали»/«отказались») is honestly admissible: parent + hypothesis elicited, `status`/`decision` elicited from the closed sets — never a silent `draft`/`—` default, never a synthesized parent.
- The PM can re-rank (updating `rank` values; file order untouched) and record their own prioritization verbatim in `pm_priority`.
- Composability (canon AC): PM-B reads PM-A's entry and can act on it WITHOUT PM-A present — the three slots + folded sub-fields are complete from the entry alone.
- Integration check (Phase B gate): the real on-disk entries of BOTH live writers diff against this schema; every mismatch is recorded as spec-friction (per invariant 3), not silently patched.

## Entry schema (OWNED HERE — the ONE canonical serialization)

File layout: a single H1 preamble, then one fenced YAML block PER ENTRY, each holding exactly one single-item list. Append = add a new block at the end of the file; update = edit in place inside the entry's block. An HTML comment above a block (provenance/date) is allowed and non-normative.

```markdown
# Solution Backlog — <owner>

```yaml
- candidate_id: sol-cand-NNN-<slug>
  title: "<one-line human title>"
  parent_opportunity: opp-NNN
  status: draft            # draft | assessed | prd_ready | archived
  decision: —              # ship | experiment-first | hold | drop | — (undecided)
  readiness: sol-r0 (promoted YYYY-MM-DD)   # or sol-rN (assessed YYYY-MM-DD); dated, demotable
  rank: <positive integer>              # OPTIONAL — PM-set ordinal; omit when unset
  pm_priority: "<verbatim>"             # OPTIONAL — the PM's own model, stored verbatim
  updated_at: YYYY-MM-DD
  intent: >
    after this ships, [outcome/metric] holds for [segment] …
  invariants:
    - "The <system> shall <always-true property> (EARS-ubiquitous)."
  acceptance_criteria:
    - "If/When <trigger>, the <system> shall <response> (EARS-stubbed seed; matures in place)."
  problem: "<one line>"
  segment: "<one line>"
  solution_hypothesis: >
    if <мы сделаем X>, then <метрика/поведение Y>, because <механизм Z>.
  target_behavior: "<one line>"
  target_outcome_metric: "<name + target>"
  why_it_might_work: "<one line>"
  key_assumptions:
    - "<assumption>"
  guardrails:
    - "<human-readable guardrail (Russian), mirrors an invariant>"
  doc: "<path>"            # OPTIONAL — the solution doc grown from this entry
  note: "<free text>"      # OPTIONAL — reasons (demote/decision/decline), provenance
  bet_type: <discovery|delivery>                    # RESERVED, UNREAD in v1
  delivery_mode: <experiment|mvp|rollout|full_launch|test>   # RESERVED, UNREAD in v1
  intent_type: <metric|strategic_learning|capability_platform|risk_quality_compliance|business_stakeholder>  # RESERVED, UNREAD in v1
```
```

**Mandatory keys** (always present): `candidate_id, title, parent_opportunity, status, decision, readiness, updated_at, intent, invariants, acceptance_criteria, problem, segment, solution_hypothesis, target_behavior, target_outcome_metric, why_it_might_work, key_assumptions, guardrails`. **Optional keys** (`rank, pm_priority, doc, note` + the three reserved) are OMITTED when empty — never written with a blank/invented value (container discipline).

**Serialization discipline (byte-compatibility rules — the two-serializations guard):**
- **Quoting:** every free-text scalar value (`title, problem, segment, target_behavior, target_outcome_metric, why_it_might_work, pm_priority, doc, note`) is DOUBLE-QUOTED (internal `"` escaped); list items are quoted strings; the two long narrative fields (`intent`, `solution_hypothesis`) use block scalars (`>`). Rationale: Russian PM prose routinely contains `: ` and leading `-`, which break bare YAML plain scalars — an unquoted writer emits unparseable files on realistic input. Enum/structured values (`candidate_id, parent_opportunity, status, decision, readiness, rank, updated_at`, reserved enums) stay unquoted.
- **Dates:** ISO 8601 `YYYY-MM-DD` everywhere a date appears (`updated_at`, the readiness annotation).
- **Key order:** the order above is the canonical WRITE order (new writes follow it; it is the lvl2 Sheets column order). lvl1 CONFORMANCE is judged on keys + values — YAML mappings are unordered, so order deviation in an existing entry is a hygiene note, not drift.

Schema notes:

- **Why the YAML-block form:** a backlog is structured, tabular data; the loose Markdown-prose form (opp-doc's `## sol-A` + `###` subsections) under-constrains the write shape — the exact root cause of the opp-backlog two-serializations defect. The sol-doc YAML form already carries the store fields (`status`/`readiness`/`decision`) the Markdown form lacks. No third form is introduced.
- **Forward-compat with the lvl2 target (base TABLE + Google Sheets adapter via `gws`):** every key above = one column, one entry = one row, mandatory-key order = column order; list values render as newline-joined cell text. v1 stays file-based only because of prompt-only + the gws proxy block; the schema must survive that migration without change.
- **`candidate_id` scheme:** `sol-cand-NNN-<slug>`; NNN = max existing NNN in THIS file + 1, zero-padded to 3 digits, NEVER reused; slug = short latin kebab from the title. Unique per PM folder only (isolation model — same accepted limitation as opp-NNN). The letters opp-doc uses in-doc (sol-A/B/C in S8) are doc-internal working labels, not ids: the file id is assigned at the promotion append; the opp-backlog card's `potential_solutions` at r3 references these `sol-cand` ids.
- **`parent_opportunity` value** = the opp-backlog card id (`opp-NNN` heading form, per `components/opp-backlog/SPEC.md`), from the SAME PM folder.
- **Promotion-time shape (the fields-absent-vs-seeded decision, ratified):** the opp-doc append writes ALL mandatory keys, seeding the lifecycle four as `status: draft`, `decision: —`, `readiness: sol-r0 (promoted <date>)`, `updated_at: <date>`. Rationale: sol-r0 is definitionally true the moment the entry exists (floor rung, no Q derivation — mirror of opp-r0 at card creation, D-1); absent lifecycle keys would break every mechanical reader and force per-reader defaults (the exact no-fallbacks violation). `(promoted <date>)` — not "assessed" — because no diagnosis pass has run (resolves the sister SPEC's r0-dated-annotation friction day-one).
- **`status` enum** = solution-doc's S0 enum `{draft | assessed | prd_ready | archived}` — the entry lifecycle. DIFFERENT from opp-backlog's 6-value card enum; never conflate, never borrow values across modules. `prd_ready` per invariant 9. `archived` is a PM-set terminal shelf state (superseded / acted-on / retired); it is NOT the automatic rendering of `hold`/`drop`.
- **`decision`** = the S9 closed set `{ship | experiment-first | hold | drop}` or `—` when undecided — a SEPARATE axis from status (a held candidate may sit `assessed`+`hold`; a shipped one `prd_ready`+`ship`). `hold`/`drop` are legitimate BELOW sol-r3 (solution-doc SPEC §Decision-at-any-rung). A delivered/shipped OUTCOME has no lvl1 axis (deliberate): record `decision: ship` + a `note`; the delivery-outcome terminal axis is lvl2 (real-wave R3) — the gap is surfaced to the PM, never papered over with `archived`.
- **`readiness` rendering** is always the compact dated claim (`sol-r2 (assessed 2026-07-07)`) — never the full definition clause per entry (sister friction #8 resolved day-one); demote reasons go to `note`. Naming: a `(promoted <date>)` floor still standing is a **stay-low** (rung never assessed — no `note` reason expected); an `(assessed <date>)` rung replaced by a LOWER `(assessed <date>)` is a **demote** (dated, reason in `note`). Both are honest; this module records either as given.
- **Reserved `sol_state` is RETIRED:** the 2026-07-07 collapse made `readiness: sol-r0..sol-r3` the single dial; `sol_state` is never written again (a live `sol_state: sol-s0` in an old entry is recorded drift, not a schema key). `bet_type` / `delivery_mode` / `intent_type` stay named, optional, UNREAD in v1.
- **`owner` is file-level, not entry-level:** the H1 preamble `# Solution Backlog — <owner>` names the owner (one PM per file, isolation model); an existing PM H1 is accepted as-is, never rewritten. Entry-level owner/role slots are lvl2 (real-wave R5).
- **`note`** is the ratified slot for the sister wave's C4 friction ("a reason with no place to live"): demote reasons, decline reasons, provenance remarks. Free text, PM- or writer-supplied only.
- **Forward-compatibility:** later-lvl features (Sheets adapter, batch intake, delivery axis, owner roles, institutional fields quarter/type/theme, dedupe views, planning shortlists) operate on THESE keys or add optional columns; none requires changing an existing key.

## Admission rules

- **Hard invariant (canon, invariant 2):** no entry without `parent_opportunity` + if-then-because `solution_hypothesis`. This applies to EVERY entry path — promotion append (opp-doc already withholds on this), manual create, and migration/legacy rows.
- **C3 ratified (parent as blocker vs flag):** `parent_opportunity` is a HARD blocker — but the refusal must ROUTE, not dead-end (the sister's source-as-blocker ambiguity caused the 59→0 migration zero-write; here the invariant is canon-frozen, so the fix is a first-class route): the PM may name an existing `opp-NNN` conversationally (counts — S4 lesson), or the one legal path is creating the opp card first (`/pm-flow:opp-backlog` create-card, minimum r0 content), then admitting the entry. A bare idea with no hypothesis routes to the opp side as an early signal (`r0-solution-signal` in opp-backlog terms) — that is its designed home, not this file.
- **Parent EXISTENCE is accepted on assertion in lvl1 (ratified, explicit):** the gate checks presence + well-formedness of `opp-NNN`; it does NOT verify the card exists — this module reads and writes ONLY its own file (no cross-file read, no router hook), and an existence gate would re-create the sister's over-block trap on migration. A dangling parent id is possible by design and PM-owned; existence validation (a read of the opp-backlog file) is a declared lvl2 extension, not a silent lvl1 behavior.
- **C1 ratified (park/kill at intake):** an already-decided row IS honestly admissible — admission gates parent+hypothesis ONLY, never aliveness. On a PM-declared outcome, elicit `status` from the enum and `decision` from the closed set (e.g. «отказались» → typically `archived` + `drop`, PM confirms); never write a silent default-alive `draft`/`—` (invariant 8); never fake a readiness above sol-r0 for a row no diagnosis pass ever saw.
- **Verbatim admission guard (Russian, refuses AND routes; spoken once per block, then acknowledge + name the one legal path; de-jargoned per the sister's C7 lesson — no internal field lists, no state labels):**
  > «в solution-backlog не заходит запись без родительской opportunity и продуктовой гипотезы if-then-because (беклог решений — не помойка идей). варианты: (a) назови id карточки opp-NNN из opp-backlog — запишу её как родителя; (b) карточки нет — сначала заведи её через /pm-flow:opp-backlog, потом вернёмся сюда; (c) гипотезы нет — идея едет в opp-backlog как ранний сигнал, не сюда.»
- Missing non-core values (title wording, why_it_might_work for a legacy row, …) are elicited or left as explicit gaps — never synthesized (invariant 8).

## Ranking (the lvl1 decision, ratified with its argument)

**lvl1 includes a PM-set ordinal rank and nothing more.** Argument: (a) the module's own intent is a DECISION QUEUE — a queue that cannot express order cannot answer "what deserves PRD next", and the canon interface (`solution-backlog → planning`: "ranked Solution options") already promises order to Planning, so deferring ranking entirely (as opp-backlog did) would breach the module's canon contract; (b) anything MORE than an ordinal violates the no-aggregate-score precedent (invariant 7) and lazy-fractal — full prioritization surfacing stays a later phase. Mechanics: optional `rank` integer, written ONLY from an explicit PM ordering statement; re-rank op updates rank values and never re-sorts the file; ties/gaps allowed; no score is ever computed from `pm_priority`, `readiness`, or anything else. **Foreign-prioritization passthrough is mandatory behavior:** if the PM's material carries MoSCoW/RICE/any model, it goes VERBATIM into `pm_priority` with a one-line transparency notice — never converted into `rank`, never aggregated, never silently dropped (real-wave R2; the empty RICE columns in the user's real sheet are field evidence that imposed scoring dies). Deferred, forward-compatible: prioritization surfacing, shortlists, readiness views (all operate on `rank`/`pm_priority`/existing keys).

## Write operations (lvl1 — ALL manually gated; ownership split explicit)

Prompt-only land: each skill edits the shared file directly, so ownership is a doc convention enforced by the Phase-B integration check, not by code. No op below is double-owned; none is orphaned.

| # | Operation | Owner | Notes |
|---|---|---|---|
| W1 | **append-entry at PROMOTION** | **opp-doc** (its c5 gate) | The only promotion path; writes ALL mandatory keys incl. the seeded lifecycle four. NOT an op of this module. |
| W2 | **pass write-back** (dated `readiness`, `status`, `decision`, matured slots S1/S7/S8) | **solution-doc** (its pass step 2) | Incl. `prd_ready` at sol-r3 ONLY; incl. demotes. NOT an op of this module. |
| O1 | **create-entry** (manual, out-of-promotion) | this module | Admission rules in full; legacy/batch rows: shared provenance stated once per batch counts (S4); per-row `status`/`decision` elicited (C1). |
| O2 | **update-status** | this module | PM-dictated, from the enum; NEVER `prd_ready` (route to `/pm-flow:solution-doc` — invariant 9). |
| O3 | **record-readiness-claim** | this module | GIVEN dated claim (from a sol-doc pass the PM relays); demotion works; never re-derived, never negotiated «ни вверх, ни вниз». |
| O4 | **update-decision** | this module | Closed set + `—`; legitimate at any rung; never auto-maps status (invariant 6). |
| O5 | **re-rank / record-pm_priority** | this module | Per §Ranking; explicit PM input only. |
| O6 | **update-links/fields** | this module | Set `doc:` when a solution doc appears; set/append `note:`; PM-dictated corrections to folded sub-fields. |

Every operation refreshes `updated_at`. Status/decision double-write is resolved by CONTEXT: solution-doc writes them only as part of its own pass write-back (W2); this module records PM-dictated changes outside a pass (O2/O4); both write the same closed sets, neither derives the other's values. **Decision precedence across writers:** a W2 pass write-back records what the doc's S9 currently carries and MAY clear a stale decision to `—` — but clearing a decision the PM set out-of-pass (O4) is SURFACED (one line + reason in `note`), never silent; a PM O4 decision made after the last pass stands until a newer pass supersedes it.

## Link model

Links are FIELDS on entries only — no graph store: `parent_opportunity` (singular, admission-bearing) → the opp-backlog card; the opp card's `potential_solutions` at r3 references `sol-cand` ids back (owned by the opp side); `doc:` → the solution doc grown from the entry. One candidate closing SEVERAL opportunities stays a RESERVED edge (not realizable in v1; activating it later is a declared extension, per the sister SPEC's link model) — at lvl1 the same solution promoted from two opportunities is simply two entries, each with its own parent (legal, see stress archetypes).

## Dedupe (decided: DEFERRED, with the argument)

No dedupe scan over solution-backlog at lvl1. Argument: entries arrive only through a hard, PM-confirmed promotion gate at a cap of 1–3 per opportunity (D-5) or through a manually-gated create — they are rare and pre-curated, unlike the raw-signal firehose that justified the router's opp-backlog scan; the promotion confirmation dialogue is already the human moment where a duplicate would surface. A same-hypothesis-two-parents pair is legal data (reserved many-to-one edge), not noise. If a writer NOTICES an apparent duplicate it may say so in one line (recommend-only, no op fires). A real scan (match keys, router involvement) would be a router change — flagged as spec-friction for the orchestrator if ever wanted, never added unilaterally.

## Acceptance-test seeds (M2 smoke; explicitly NOT the M3 gate)

1. **Promotion conformance:** a fresh opp-doc-style promotion lands as one conforming entry (all mandatory keys, seeded lifecycle four).
2. **Write-back + demote:** a sol-doc-style write-back demotes `prd_ready`/sol-r3 → `assessed`/sol-r2 with a fresh date; header==entry value; reason in `note`.
3. **Admission guard:** a bare idea is refused with the verbatim guard (once, then acknowledge+route); a legacy decided row admits with elicited status/decision.
4. **Ranking:** PM re-ranks three entries; `rank` values update, file order untouched; a MoSCoW label is stored verbatim in `pm_priority`, no conversion.
5. **Composability (canon AC):** PM-B acts on PM-A's entry without PM-A present.
6. **Integration check:** both live writers' real fixtures diffed against this schema; drift recorded as friction (the stage's highest-value test).

These are mock/smoke checks. The M2→M3 gate is separate: real promoted candidates + real PRD write-backs through the LIVE skill.

## Explicit non-goals (lvl1)

- No Q-rubric, no readiness derivation or re-scoring (records given claims only).
- No computed/aggregate priority score; no prioritization surfacing beyond the PM-set ordinal.
- No dedupe scan; no merge execution; no cross-PM anything (isolation model).
- No Sheets/Confluence adapter (lvl2 target; schema is ready for it); no non-Markdown store; no JSON/DB.
- No automatic mutations; no writes to opp docs, solution docs, opp-backlog, or any file but the solution-backlog file itself.
- No delivery-outcome axis (lvl2 R3); no entry-level owner slots (lvl2 R5); no institutional fields (lvl2 R6).
- No router hook — the module is reached by explicit PM invocation; writers connect through the shared FILE.

## Deferred to later lvl (forward-compatible in this schema)

Base-TABLE format + Google Sheets adapter via `gws` (lvl2 reference target; blocked today by the gws proxy issue) · batch/bulk-intake op with per-batch defaults (R1) · delivery-outcome terminal axis (R3) · owner as role-tag vs named person (R5) · institutional adaptive-periphery fields: quarter, type, theme/epic, decline-reason (R6) · dedupe scan / merge · prioritization surfacing, shortlists, readiness views · activating the many-to-one candidate↔opportunity edge.

## Day-one build notes (non-normative; Phase B bakes these as skill rules — sister lessons, paid for in blood)

- **S-1 full-inventory mutation gate** inline; append-only ops need ONE confirmation, not an inventory ceremony re-run (sister S9).
- **Anti-loop refusal UX (S1):** every verbatim guard once per block; on pushback — acknowledge, name the one legal path, offer to run it; the gate never softens.
- **Never auto-default a field (S2); no silent lifecycle lie (S3); conversational/batch provenance counts (S4).** Marked-verbatim strings are reproduced byte-exactly; improvised Russian carries no jargon (no "S-1"/"lvl1"/section codes at the PM).
- **Separate-artifact transparency (sister S12b):** on first write in a session, one plain-Russian line that this is a separate committed Markdown file, not the PM's existing sheet/tool (Sheets adapter = lvl2).
- **Demotion path must demonstrably work** (readiness AND status down-moves).
- **Registration:** read the ACTUAL current plugin version live from BOTH manifests, bump minor, sync, refresh cache; fixtures named by the probe that produced them.
