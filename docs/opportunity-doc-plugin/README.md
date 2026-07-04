# opportunity doc plugin

> working discovery pack for aipm / avito pm tooling  
> цель: спроектировать плагин, который помогает продакту довести сигнал / идею решения / слабый opportunity doc до living opp doc, readiness diagnosis, gaps, tasks и compact backlog card.

## что это

это не “генератор opportunity doc”.

правильная модель:

```text
плагин ведёт opportunity через состояния понимания,
а opportunity doc является living artifact этого процесса.
```

ядро:

```text
solution idea / raw signal / weak opp doc
  → intake & framing
  → living opportunity doc
  → gap analysis
  → tasks
  → task results
  → doc update
  → gap analysis again
  → readiness recalculation
  → backlog card / next step
```

## где что лежит

- [`full-context.md`](./full-context.md) — полный контекст discovery: решения, модели, readiness, workflows/skills, gaps, tasks, риски, open questions. читать, если нужно понять всё.
- [`next-steps.md`](./next-steps.md) — практический план: что делать дальше, как вайбкодить, какие артефакты собрать следующими.
- [`prototype-flow.html`](./prototype-flow.html) — статический connected-flow прототип: solution idea → raw signal → weak opp doc → tasks → task result → updated card.

## главный mental model

```text
input can be anything:
  solution idea / signal / weak opp doc / fragment

plugin classifies it:
  what is this?

plugin frames it:
  who, scenario, problem?

plugin refuses bullshit:
  fact / assumption / unknown

plugin identifies gaps:
  critical / major / minor

plugin creates tasks:
  pm / evidence / rewrite-edit

user brings results:
  task result intake

plugin updates living opp doc:
  doc update + gap analysis again

plugin outputs:
  improved opp doc + readiness + tasks + backlog card + next step
```

## ключевые решения

### 1. readiness ≠ priority

readiness — степень проработки. priority — отдельный процесс выбора.

```text
r0 — signal
r1 — framed opportunity
r2 — sized / decomposed opportunity
r3 — opportunity with ranked existing solution hypotheses
```

r0 тоже лежит в opportunity backlog.

### 2. opp doc — не prd

opp doc не должен содержать delivery roadmap, acceptance criteria, ux-макеты, архитектуру и детальное описание решения.

### 3. solution без opportunity заворачивается назад

если на входе “нужно сделать рекомендованную цену”, плагин не принимает это как opportunity. он ищет underlying problem.

### 4. loops = plugin skills

для mvp достаточно:

```text
skill 1: intake & framing
skill 2: gap resolution
quality pass: human doc quality / anti-bullshit
```

### 5. pлагин не должен быть занудным reviewer

он должен снимать работу:

- переписать слабый doc;
- найти gaps;
- превратить gaps в tasks;
- показать next step;
- собрать compact backlog card.

## mvp scope

делаем:

- один textarea input;
- classifier + confirmation;
- три connected сценария;
- readiness r0–r3;
- gap analysis;
- task generation;
- human rewrite;
- claim warnings summary;
- compact backlog card;
- task result intake loop;
- static connected-flow prototype.

не делаем:

- quarterly planning;
- automatic jira task creation;
- full solution backlog workflow;
- prd generation;
- delivery decomposition;
- architecture / acceptance criteria / ux mockups;
- full product context config workflow;
- final opportunity score formula.

## следующий артефакт

сначала делать:

```text
mvp result screen spec
```

подробности — в [`next-steps.md`](./next-steps.md).

> **SUPERSEDED (2026-07-04):** source material only. Reconciled canon = `docs/target-solution.md` + `docs/design-log/2026-07-04-reconciliation.md`; on any conflict those win.
