# opportunity doc plugin — next steps

> цель: превратить discovery-контекст в прототип, который можно вайбкодить и показывать.

## 0. главный следующий артефакт

следующий артефакт — не prd и не ещё одна методология.

нужен:

```text
mvp result screen spec
```

почему: главный экран результата — это центр продукта. именно там pm должен почувствовать, что плагин не просто reviewer, а рабочий помощник.

## 1. result screen v0

### 1.1 layout

гибридный экран:

```text
верхний summary:
  readiness
  workflow status
  scenario
  main diagnosis
  next step
  priority data

ниже:
  improved opp doc
  gaps
  tasks
  claim warnings
  backlog card
```

### 1.2 обязательные ответы экрана

экран должен отвечать:

- что у меня сейчас есть?
- какой readiness?
- почему именно такой readiness?
- что блокирует следующий transition?
- какие tasks нужно сделать?
- какой улучшенный opp doc получился?
- можно ли это положить в backlog?
- какой next step?

### 1.3 primary cta

cta зависит от состояния:

```text
r0 + unclear problem → answer grillme questions
r1 + critical gaps → create tasks
waiting for task result → add task result
after task result → update opp doc
r2/r3 → package backlog card
```

но для demo главный cta:

```text
create tasks
```

потому что он превращает reviewer в workflow.

## 2. connected demo scenario

делаем один connected case вокруг ценовой неопределённости продавцов.

```text
step 1: solution idea
“нужно сделать рекомендованную цену”

step 2: detox to raw signal
“похоже, продавцы не понимают, какую цену поставить”

step 3: weak opp doc
pm написал solution-first doc без sizing/decomposition

step 4: plugin result
improved opp doc + gaps + tasks + backlog card

step 5: task result intake
pm/evidence приносит данные

step 6: doc update + gap analysis again
readiness пересчитывается
```

## 3. screen states to design

### state 1. input classified as solution idea

показывать:

- detected type: solution idea;
- warning: not an opportunity yet;
- detox questions;
- save as r0 solution-signal;
- next step: frame underlying problem.

### state 2. input classified as raw signal

показывать:

- detected type: raw signal;
- r0/r1 candidate;
- minimal grillme questions;
- skeleton opp doc;
- unknowns;
- first tasks.

### state 3. input classified as existing weak opp doc

показывать:

- current readiness;
- rewritten opportunity statement;
- gaps;
- tasks;
- claim warnings;
- backlog card.

### state 4. task result added

показывать:

- what changed;
- updated evidence / sizing / decomposition;
- closed gaps;
- new gaps;
- recalculated readiness;
- updated backlog card.

## 4. transition criteria table

создать таблицу:

| level | meaning | required | critical gaps | allowed outputs | next step |
|---|---|---|---|---|---|
| r0 | signal | signal/source/domain | no user/scenario/problem | backlog r0 | frame |
| r1 | framed opportunity | user/scenario/problem | no evidence/sizing/decomposition | opp skeleton/card | size/decompose |
| r2 | sized/decomposed | evidence/sizing/components | no solution-component link if moving to r3 | backlog-ready opp | prepare solutions only if requested |
| r3 | ranked existing solution hypotheses | hypotheses linked to components | no expected mechanism | solution backlog candidate | before-prd tasks |

## 5. task templates

### pm task

```text
task:
role: pm
why needed:
acceptance criteria:
linked gap:
```

пример:

```text
task: разложить проблему на компоненты
role: pm
why needed: без decomposition opportunity слишком широкая и не может перейти r1 → r2
acceptance criteria: есть 3–5 components, для каждого указан affected segment/scenario
linked gap: no problem decomposition
```

### evidence task

```text
task: оценить affected volume
role: evidence
why needed: без rough sizing нельзя перейти r1 → r2
acceptance criteria: есть диапазон affected volume, источник, period, confidence
linked gap: no sizing
```

### rewrite/edit task

```text
task: переписать opp doc problem-first
role: rewrite/edit
why needed: сейчас документ solution-first и скрывает unknowns
acceptance criteria: есть concise opportunity statement, claims marked as fact/assumption/unknown, no delivery language
linked gap: ai-slop / solution-first doc
```

## 6. non-slop writing rubric

проверки:

- конкретный пользователь;
- конкретный сценарий;
- конкретная проблема;
- нет “improve experience” без поведения;
- нет claims без fact/assumption/unknown;
- нет delivery language;
- нет prd language;
- короткий tl;dr;
- gaps не спрятаны.

## 7. backlog card contract

```text
signal:
problem:
potential solutions:
priority data:
readiness/status:
next step:
```

для r0/r1 card тоже создаётся, но с явным next step.

## 8. prototype changes

обновить/держать в html-прототипе:

- journey strip;
- connected scenarios;
- hybrid result screen;
- clear readiness/status/priority separation;
- tasks with why + acceptance criteria;
- task result intake;
- gap analysis again;
- no proactive solution generation.

## 9. engineering-ish breakdown for vibe coding

### milestone 1. static prototype

- static connected flow;
- three input examples;
- result screen tabs;
- hardcoded gaps/tasks/readiness;
- task result step.

### milestone 2. local interactive prototype

- textarea input;
- simple classifier;
- scenario switch;
- editable opp doc sections;
- add task result;
- recalculate hardcoded readiness.

### milestone 3. llm-backed prototype

- classifier prompt;
- detox prompt;
- gap detection prompt;
- rewrite prompt;
- task generation prompt;
- claim warning summary;
- output schema.

### milestone 4. config mock

- domain profile json;
- metrics dictionary;
- task templates;
- readiness preferences.

### milestone 5. repo/demo polish

- README as navigation;
- full context pack;
- prototype html;
- examples folder;
- screenshot/gif later.

## 10. suggested folder structure

```text
docs/opportunity-doc-plugin/
  README.md
  full-context.md
  next-steps.md
  prototype-flow.html
  examples/
    solution-idea-input.md
    raw-signal-input.md
    weak-opp-doc-input.md
    improved-opp-doc-output.md
  schemas/
    opportunity-doc.schema.md
    task.schema.md
    backlog-card.schema.md
```

## 11. immediate next action

1. finish `mvp-result-screen-spec.md`.
2. create `examples/` with one connected case.
3. create `schemas/` for opp doc, task, backlog card.
4. make html prototype consume those examples later.
5. only after this: design prompts/contracts.

## 12. reminder

do not start with 25 workflows or 17 agents.

start with:

```text
3 connected scenarios
2 skills/loops
1 quality pass
1 living opp doc
1 backlog card
```
