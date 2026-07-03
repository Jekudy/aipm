# opportunity doc plugin — full context pack

> snapshot: 2026-07-03  
> repo area: `docs/opportunity-doc-plugin/`  
> purpose: сохранить весь набранный контекст по opportunity doc plugin: решения, развилки, модели, риски, открытые вопросы и следующие шаги.

## 0. исходная задача

нужно сформулировать критерии readiness для opportunity doc для продактов авито и по этапам, чтобы понять, какой документ достаточно хорош, чтобы его результат можно было компактно положить в backlog, а дальше взять из него гипотезу решения, которую можно развивать в prd.

первичный запрос был не “дай шаблон”, а “проинтервьюируй меня relentlessly, пройди по веткам design tree, разрешая зависимости между решениями”. это важно: методология должна быть не чеклистом, а системой принятия решений и движения opportunity.

## 1. главный разворот понимания

мы ушли от идеи “плагин пишет opportunity doc” к более сильной модели:

```text
плагин ведёт opportunity через состояния понимания,
а opportunity doc является living artifact этого процесса.
```

opportunity doc — это не финальный файл. это контейнер, который живёт по мере проработки:

```text
signal
→ framing
→ evidence
→ decomposition
→ sizing
→ gaps
→ tasks
→ task results
→ doc update
→ gap analysis again
→ readiness recalculation
→ backlog card
```

## 2. что такое хороший opportunity doc

хороший opp doc должен показывать:

- объём проблемы;
- компоненты проблемы и их объём;
- ключевые возможности внутри проблемы;
- evidence, assumptions и unknowns;
- gaps и что нужно сделать, чтобы их закрыть;
- 0–3 потенциальных направления решения, если они уже есть;
- compact backlog output;
- next step.

важно: хороший opp doc не обязан доказывать конкретное решение. он должен дать достаточно понимания, чтобы opportunity можно было положить в backlog без потери смысла.

## 3. границы opp doc

opp doc не является prd и не должен содержать:

- детальное описание решения;
- ux-макеты;
- acceptance criteria;
- архитектурные детали;
- детальную экономику эксперимента;
- delivery roadmap;
- sprint plan реализации;
- полноценные success metrics конкретного решения.

можно держать high-level affected metrics и product/business relevance, но нельзя превращать opp doc в delivery artifact.

## 4. главная архитектура backlog

принято решение:

```text
есть opportunity backlog
есть solution backlog
```

opportunity backlog хранит всё от r0 до r3:

```text
r0 signal
r1 framed opportunity
r2 sized/decomposed opportunity
r3 opportunity with ranked existing solution hypotheses
```

solution backlog получает только лучший / выбранный solution backlog candidate, когда opportunity достаточно зрелая.

ключевая мысль:

```text
r0–r3 — это maturity/readiness, не priority.
```

opportunity может быть r3, но неважной; или r1, но стратегически срочной.

## 5. три независимые оси

### 5.1 readiness / maturity

отвечает на вопрос:

```text
насколько хорошо мы понимаем opportunity?
```

уровни:

```text
r0 — signal
r1 — framed opportunity
r2 — sized / decomposed opportunity
r3 — opportunity with ranked existing solution hypotheses
```

### 5.2 workflow status

отвечает на вопрос:

```text
что сейчас происходит с этой opportunity?
```

человеку показываем очень простые статусы:

```text
new
in progress
needs input
ready for next step
parked
```

машинные статусы оркестратор может вести сам:

```text
needs_problem_framing
needs_sizing
needs_decomposition
needs_evidence
needs_task_result
needs_rewrite
needs_solution_ranking
needs_backlog_packaging
```

люди не должны руками вести много статусов. это дохуя и никто не будет.

### 5.3 priority / selection

отвечает на вопрос:

```text
насколько это важно брать в работу относительно других opportunities?
```

это отдельный процесс, не readiness. quarterly planning пока не mvp.

## 6. readiness levels

### r0 — signal

есть:

- сырой сигнал;
- источник или автор;
- примерный домен / тема.

можно:

- сохранить в opportunity backlog;
- начать intake & framing.

нельзя:

- считать problem/opportunity понятой;
- создавать solution backlog candidate;
- идти в prd.

пример:

```text
signal: продавцы спрашивают, какую цену поставить.
source: support / интервью / наблюдение pm.
readiness: r0.
```

### r1 — framed opportunity

нужно:

- пользователь / сегмент;
- сценарий;
- problem statement;
- почему это проблема;
- источник сигнала;
- отделение problem от solution.

пример:

```text
новые продавцы в категории x не понимают, какую цену поставить при первом размещении, из-за чего ставят цену наугад, чаще редактируют объявление и дольше ждут первых откликов.
```

### r2 — sized / decomposed opportunity

нужно:

- problem decomposition;
- rough sizing диапазоном;
- evidence inventory;
- confidence;
- known unknowns;
- gap list;
- workplan/tasks, если gaps ещё не закрыты.

### r3 — opportunity with ranked existing solution hypotheses

нужно:

- 1–3 solution hypotheses, если они уже есть или pm попросил их проработать;
- привязка каждой hypothesis к problem component;
- fast ranking / recommendation;
- before-prd unknowns/tasks.

важное предупреждение:

```text
r3 ≠ high priority
r3 ≠ prd
r3 ≠ delivery commitment
r3 ≠ acceptance criteria
```

## 7. transition contracts

### r0 → r1

нужно понять:

- кто пользователь / сегмент;
- в каком сценарии возникает проблема;
- какая проблема;
- почему это не просто feature idea;
- откуда пришёл сигнал.

если пришло решение без проблемы — остаётся r0 solution-signal.

### r1 → r2

нужно:

- разложить проблему на компоненты;
- дать rough sizing хотя бы диапазоном;
- собрать evidence inventory;
- указать confidence;
- зафиксировать gaps/unknowns;
- создать workplan/tasks для закрытия gaps.

### r2 → r3

нужно:

- иметь 1–3 solution hypotheses, если они есть/запрошены;
- привязать каждую hypothesis к problem component;
- сделать fast ranking;
- указать recommended top hypothesis;
- оставить только non-critical gaps для перехода к solution backlog candidate.

### r3 → solution backlog candidate

нужно:

- parent opportunity;
- target problem component;
- chosen/top-ranked solution hypothesis;
- expected mechanism;
- before-prd tasks.

## 8. problem-vs-solution detox

принцип:

```text
solution hypothesis без opportunity заворачивается назад до opp doc или r0 signal.
```

пример входа:

```text
нужно сделать рекомендованную цену.
```

плагин должен спросить:

- какую проблему это решает?
- для кого?
- в каком сценарии?
- как мы знаем, что проблема есть?
- какие ещё решения могли бы решить ту же проблему?

исходы:

1. проблема не ясна → r0 solution-signal;
2. проблема ясна → r1 framed opportunity;
3. проблема + evidence + sizing → r2 candidate.

## 9. opp doc как living container

решение: opp doc — основной контейнер всего процесса.

структура mvp:

```text
1. compact opportunity card
2. opportunity statement
3. evidence / assumptions / unknowns
4. problem decomposition
5. priority data
6. gaps
7. tasks / workplan
8. solution hypotheses, only if provided or requested
9. backlog packaging
```

важно: это один документ, но в нём два слоя:

```text
human-readable doc — короткий, problem-first, readable
operational metadata — gaps, tasks, claim map, служебные штуки
```

иначе opp doc станет помойкой.

## 10. compact opportunity backlog card

самая компактная карточка:

```text
signal
problem
potential solutions
priority data
readiness / status
next step
```

карточка генерируется даже для r0/r1, но с явным readiness и next step.

пример:

```text
signal:
support и интервью показывают, что новые продавцы не уверены в цене.

problem:
новые продавцы в категории x не понимают, какую цену поставить при первом размещении.

potential solutions:
1. диапазон рыночной цены
2. рекомендованная цена
3. объяснение влияния цены на спрос

priority data:
volume: high
severity: medium
addressability: medium
strategic fit: high
urgency: low

readiness:
r2, needs solution hypothesis ranking

next step:
закрыть sizing/decomposition gaps или привести существующие solution hypotheses в порядок.
```

## 11. priority data для opportunity backlog

в mvp не считаем итоговый score числом.

5 компонентов:

```text
volume
severity
addressability
strategic fit
urgency
```

confidence не включаем в priority, чтобы не смешивать priority и readiness.

confidence живёт отдельно:

```text
confidence / evidence strength / claim quality
```

возможная будущая формула:

```text
opportunity potential = volume × severity × addressability
opportunity timing = strategic fit × urgency
opportunity score = opportunity potential × opportunity timing
```

но не в mvp, потому что будет ложная точность.

## 12. gaps

severity:

```text
critical — блокирует readiness transition или solution backlog candidate
major — снижает confidence, но не блокирует
minor — улучшает качество, но можно жить
```

critical gaps:

- неясно, кто пользователь;
- неясен сценарий;
- неясна проблема;
- solution без opportunity;
- нет evidence вообще;
- нет rough sizing для r2;
- нет decomposition для широкой opportunity;
- нет понимания addressability;
- нет parent component для solution hypothesis.

важно:

```text
critical gap не блокирует хранение в opportunity backlog.
critical gap блокирует переход readiness.
```

## 13. tasks

плагин не просто говорит “чего не хватает”, а превращает gaps в задачи.

в mvp роли:

```text
pm
evidence
rewrite/edit
```

analytics и research пока объединяем в evidence task.

минимальный task contract:

```text
task
role
why needed
acceptance criteria
linked gap
```

пример:

```text
task:
оценить rough affected volume по проблеме ценовой неопределённости.

role:
evidence

why needed:
без rough sizing opportunity не может перейти r1 → r2.

acceptance criteria:
есть диапазон affected volume за месяц, источник данных и confidence: low/medium/high.

linked gap:
нет sizing.
```

после выполнения:

```text
user приносит result
→ plugin updates opp doc
→ linked gap закрывается или меняется
→ gap analysis again
→ readiness recalculation
→ new gaps/tasks if needed
```

## 14. gap resolution loop

сердце продукта:

```text
gap analysis
  → gap tasks
  → pm/evidence/rewrite work
  → task result intake
  → living doc update
  → gap analysis again
  → readiness recalculation
```

после task result нельзя сразу идти дальше. нужно снова анализировать gaps.

эта петля может повторяться несколько раз.

## 15. loops as skills

решение: в плагине loops можно считать skills.

### skill 1. intake & framing

цель: довести вход до r0/r1.

входы:

- raw signal;
- solution idea;
- doc fragment;
- existing doc, где проблема не ясна.

output:

- r0/r1 opp doc skeleton;
- problem-first statement;
- unknowns;
- first gaps;
- next questions/tasks.

### skill 2. gap resolution

цель: двигать opportunity по readiness.

output:

- updated opp doc;
- updated readiness;
- gap list;
- tasks;
- next step;
- compact backlog card.

### quality pass

не отдельный skill для пользователя, а санитарный проход.

проверяет:

- fact / assumption / unknown;
- solution-first подмены;
- no ai-slop;
- no delivery language;
- clear tl;dr;
- honest gaps.

## 16. grillme

grillme — переиспользуемый механизм внутри skills.

оригинальный принцип:

```text
interview me relentlessly about every aspect of this plan until we reach a shared understanding.
walk down each branch of the design tree, resolving dependencies between decisions one-by-one.
use askuserquestion to get feedback.
```

адаптация:

- идём по веткам design tree;
- не принимаем общие слова;
- просим конкретный сегмент, сценарий, поведение, источник;
- если pm не знает — маркируем unknown;
- если unknown критичный — создаём task;
- если есть assumption — просим подтвердить;
- если найден новый независимый компонент — предлагаем linked r0.

## 17. claim quality / anti-bullshit

любой claim должен быть:

```text
fact
assumption
unknown
```

плагин не должен:

- выдумывать facts;
- писать уверенно без evidence;
- превращать weak evidence в strong claim;
- замазывать unknowns красивым текстом.

claim map в mvp показываем как summary + warnings, не огромной таблицей.

## 18. human writing / non-slop

принцип качества текста:

- problem-first;
- коротко;
- конкретно;
- честно;
- без корпоративного тумана;
- без delivery language;
- без “улучшения пользовательского опыта” без конкретики;
- gaps и assumptions явно видны.

критерий:

```text
документ читается как рабочая записка pm, а не как ai-generated corporate soup.
```

## 19. solution hypotheses

mvp-правило:

```text
если solution hypotheses уже есть в исходном документе — проверяем и приводим в порядок.
если их нет — не генерируем без просьбы pm.
```

причина: мы не хотим, чтобы плагин преждевременно тащил продакта в solution mode.

если solution есть, она должна иметь:

- parent opportunity;
- target problem component;
- expected mechanism;
- confidence / unknowns;
- before-prd tasks.

r3 может включать ranked existing solutions, но top hypothesis = next exploration direction, не commitment.

## 20. product context config

конфиг нужен, но это отдельный большой workflow.

в mvp:

```text
mock config / ручной контекст
```

позже в конфиге должны жить:

- product domain;
- team;
- pm / owners;
- user segments;
- key scenarios;
- north-star / guardrail metrics;
- domain metrics;
- dashboards;
- event taxonomy;
- evidence sources;
- decomposition axes;
- strategic goals;
- stakeholders;
- task templates;
- readiness preferences;
- scoring preferences.

opp doc flow должен использовать конфиг, но не обязан уметь его создавать в mvp.

## 21. domain invariants

важны не одинаковые метрики, а одинаковые вопросы:

```text
1. кто затронут?
2. в каком сценарии?
3. что идёт не так?
4. как мы это видим?
5. какой объём?
6. какая часть объёма addressable?
7. почему это важно?
8. что мы пока не знаем?
9. что можно попробовать сделать?
```

доменные примеры:

### marketplace

- listings affected;
- sellers affected;
- buyers affected;
- conversion to contact;
- conversion to deal;
- time to first response;
- gmv / revenue;
- paid conversion;
- listing quality.

### jobs

- vacancies affected;
- employers affected;
- candidates affected;
- applications per vacancy;
- conversion to application;
- employer response rate;
- time to hire;
- vacancy fill rate;
- candidate quality.

### automated support

- contact rate;
- ticket volume;
- automation coverage;
- deflection rate;
- resolution rate;
- reopen rate;
- csat;
- cost per contact;
- sla breaches;
- manual support load.

### antifraud

- fraud attempts;
- fraud losses;
- users harmed;
- false positives;
- false negatives;
- manual review volume;
- time to resolution;
- appeal rate;
- blocked good users;
- trust impact.

## 22. three connected mvp scenarios

решение: делаем все три сценария, но connected, не отдельными демо.

flow:

```text
c · solution idea
“нужно сделать рекомендованную цену”
  ↓
b · raw signal
“похоже, продавцы не понимают, какую цену поставить”
  ↓
a · weak opp doc
pm уже начал писать opp doc, но он solution-first и без sizing/decomposition
  ↓
loop · task result
pm/evidence tasks выполнены, результат возвращается в opp doc
  ↓
gap analysis again / readiness recalculation
```

### scenario c — solution idea

цель: detox.

output:

- r0 solution-signal или r1 opportunity;
- questions to frame problem;
- no direct solution backlog.

### scenario b — raw signal

цель: r0/r1 skeleton.

output:

- signal card;
- opportunity draft;
- unknowns;
- first gaps;
- tasks.

### scenario a — weak opp doc

цель: improved doc + gaps + tasks.

output:

- improved opp doc;
- readiness diagnosis;
- gaps;
- tasks;
- claim warnings;
- compact backlog card.

## 23. result screen

решение: hybrid result screen.

сверху:

```text
readiness
workflow status
scenario
main diagnosis
next step
priority data
```

ниже tabs/sections:

```text
improved opp doc
gaps
tasks
claim warnings
backlog card
```

первый экран должен дать ответы:

- где я сейчас?
- чего не хватает?
- что делать дальше?
- какой обновлённый opp doc получился?
- можно ли это положить в backlog?

главный wow:

```text
плохой док стал понятным
+
pm понял, чего не хватает
```

## 24. first screen input

решение:

```text
one textarea + classifier + confirmation
```

pm вставляет что угодно:

- raw signal;
- solution idea;
- existing opp doc;
- fragment.

плагин сам классифицирует и просит мягкое подтверждение.

## 25. mvp scope

делаем:

- one textarea input;
- classifier;
- confirmation of classification;
- three connected scenarios;
- readiness r0–r3;
- gap analysis;
- task generation;
- human rewrite;
- claim warnings summary;
- compact backlog card;
- task result intake loop;
- connected-flow prototype.

не делаем:

- quarterly planning;
- automatic jira task creation;
- full solution backlog workflow;
- prd generation;
- delivery decomposition;
- architecture;
- acceptance criteria;
- ux mockups;
- full product context config workflow;
- final opportunity score formula.

## 26. risks / self-roast

### риск 1. airport instead of terminal

мы легко можем построить аэропорт вместо первого терминала: 25 workflows, 17 blocks, агенты, статусы. для mvp фокус:

```text
3 scenarios
2 skills/loops
1 quality pass
1 living opp doc
1 backlog card
```

### риск 2. reviewer вместо продукта

если плагин только критикует, это занудный reviewer. он должен снимать работу:

- rewrite;
- compression;
- gap detection;
- task generation;
- next step;
- backlog card.

### риск 3. opp doc как помойка

решение: human-readable layer + operational metadata layer.

### риск 4. false precision

не считать score в mvp. показывать dimensions.

### риск 5. r3 pulls into prd

top solution hypothesis нужно маркировать как exploration direction.

### риск 6. config eats the project

config нужен, но workflow config creation выносим отдельно.

### риск 7. слишком много статусов

человек видит простые статусы. оркестратор ведёт machine statuses.

### риск 8. tasks as full task manager слишком рано

в mvp tasks живут внутри opp doc/workplan. jira потом.

## 27. open questions

1. какие конкретные поля должны быть в operational metadata vs visible doc?
2. насколько aggressively показывать claim warnings?
3. должен ли pлагин уметь сравнивать opportunities между собой в mvp или только готовить data?
4. где граница между r2 и r3, если pm не хочет обсуждать solutions?
5. когда solution hypothesis из opp doc становится solution backlog candidate?
6. как показывать linked r0 suggestions без захламления?
7. как versioning/changelog должен выглядеть в mvp?
8. что считается “достаточно хорошим” mvp human rewrite?
9. как конфиг под команду будет подмешиваться в рантайме?
10. какие examples нужны для demo на avito domains: marketplace, jobs, support, antifraud?

## 28. recommended next steps

### next 1. result screen spec

спроектировать главный экран результата:

- layout;
- header;
- readiness summary;
- next step;
- tabs;
- gaps;
- tasks;
- claim warnings;
- backlog card;
- empty states;
- weak input states;
- task result intake.

### next 2. scenario scripts

написать 3 demo scripts:

- solution idea → detox;
- raw signal → skeleton;
- weak opp doc → improved doc + gaps + tasks.

они должны быть connected вокруг одного кейса.

### next 3. transition criteria table

сделать таблицу r0/r1/r2/r3:

- criteria;
- critical gaps;
- allowed outputs;
- next step;
- examples.

### next 4. task templates

сделать шаблоны:

- pm task;
- evidence task;
- rewrite/edit task.

### next 5. quality rubric

сделать критерии non-slop rewrite:

- problem-first;
- no unsupported claims;
- no delivery language;
- concise;
- concrete;
- unknowns visible.

### next 6. prototype iteration

обновить html-прототип:

- connected journey strip;
- hybrid result screen;
- task result intake step;
- no proactive solution generation;
- clear difference between readiness and priority.

## 29. final mental model

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

это и есть ядро opportunity doc plugin mvp.
