# opportunity doc plugin — discovery notes and mvp spec

> status: working product discovery snapshot  
> audience: aipm / avito pm tooling  
> purpose: зафиксировать ключевые решения, контекст и продуктовую модель, которые мы наработали в диалоге

## 0. коротко

мы проектируем не “генератор opportunity doc”, а плагин, который помогает продакту двигать opportunity через состояния понимания.

opportunity doc — это живой контейнер процесса: сигнал, проблема, данные, gaps, задачи, обновления, потенциальные решения, readiness и compact backlog card.

ключевая формула:

```text
signal / solution idea / weak opp doc
  → intake & framing
  → living opp doc
  → gap analysis
  → tasks
  → task results
  → doc update
  → gap analysis again
  → backlog card / next step
```

главный mvp-wow:

```text
“я пришёл с кашей → получил понятную opportunity”
+
“я загрузил плохой doc → понял, чего не хватает и что делать дальше”
```

## 1. базовые принципы

### 1.1 opp doc — не prd

opportunity doc не должен содержать:

- детальное описание решения;
- ux-макеты;
- acceptance criteria;
- архитектурные детали;
- детальную экономику эксперимента;
- delivery roadmap;
- sprint plan;
- полноценные success metrics конкретного решения.

в opp doc допустимы high-level outcomes и affected metrics, но не commitment на delivery.

### 1.2 readiness — это степень понимания, а не приоритет

железное разделение:

```text
readiness ≠ priority
workflow status ≠ priority
priority ≠ readiness
```

opportunity может быть:

- r3, но низкий приоритет;
- r1, но стратегически срочная;
- r0, но важный сигнал, который стоит держать в backlog.

### 1.3 r0 тоже лежит в opportunity backlog

opportunity backlog хранит не только зрелые opportunities, но и сигналы.

```text
r0 signal → opportunity backlog
r1 framed opportunity → opportunity backlog
r2 sized/decomposed opportunity → opportunity backlog
r3 opportunity with ranked existing solution hypotheses → opportunity backlog + optional solution backlog candidate
```

critical gaps не блокируют хранение в backlog. они блокируют переходы readiness.

### 1.4 solution без opportunity заворачивается назад

solution hypothesis или feature idea без parent opportunity не должна напрямую становиться solution backlog item.

если на входе:

```text
“нужно сделать рекомендованную цену”
```

плагин должен спросить:

```text
какую проблему это решает?
у кого?
в каком сценарии?
как мы знаем, что проблема есть?
какие ещё решения могли бы решить ту же проблему?
```

если проблема не ясна, это r0 solution-signal, а не opportunity doc.

### 1.5 no unsupported claims

любой важный claim должен быть одним из трёх типов:

```text
fact — подтверждено источником
assumption — предположение команды
unknown — неизвестно, нужно проверить
```

плагин не должен писать уверенный красивый текст, если данных нет. если факта нет — маркируем assumption/unknown или создаём task.

### 1.6 не ai-slop

важный reusable стандарт качества текста:

- конкретные пользователи вместо “users”;
- конкретный сценарий вместо “experience”;
- короткие предложения;
- claims помечены как fact / assumption / unknown;
- нет корпоративной воды;
- нет преждевременной уверенности;
- gaps не замазаны красивыми формулировками;
- есть честный next step.

плохо:

```text
пользователи могут испытывать трудности в процессе взаимодействия с функциональностью размещения, что потенциально оказывает влияние на общий пользовательский опыт.
```

лучше:

```text
новые продавцы в категории x часто не понимают, какую цену поставить при первом размещении. мы видим это в интервью и косвенно в редактировании цены в первые 7 дней после публикации.
```

## 2. три оси системы

### 2.1 readiness / maturity

отвечает на вопрос: насколько хорошо мы понимаем opportunity?

```text
r0 — signal
r1 — framed opportunity
r2 — sized / decomposed opportunity
r3 — opportunity with ranked existing solution hypotheses
```

### 2.2 workflow status

отвечает на вопрос: что сейчас происходит с opportunity?

человеку показываем только простые статусы:

```text
new
in progress
needs input
ready for next step
parked
```

детальные machine statuses оркестратор может вести сам:

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

люди не должны вручную вести 15 статусов. это должна делать система.

### 2.3 priority / selection

отвечает на вопрос: насколько это важно брать в работу относительно других opportunities?

это отдельный процесс, не readiness.

в mvp не делаем квартальное планирование и не делаем финальную формулу приоритизации. собираем только данные для будущей приоритизации.

## 3. readiness уровни

### r0 — signal

достаточно:

- есть сигнал;
- есть источник или автор;
- есть примерный домен / тема.

можно:

- сохранить в opportunity backlog как r0;
- начать intake & framing.

нельзя:

- считать opportunity понятой;
- создавать solution backlog candidate;
- писать prd.

### r1 — framed opportunity

нужно:

- пользователь / сегмент;
- сценарий;
- проблема;
- источник сигнала;
- problem-first statement.

пример:

```text
новые продавцы в категории x не понимают, какую цену поставить при первом размещении, из-за чего ставят цену наугад, чаще редактируют объявление и дольше ждут первых откликов.
```

### r2 — sized / decomposed opportunity

нужно:

- problem decomposition;
- rough sizing хотя бы диапазоном;
- evidence inventory;
- confidence;
- critical unknowns / gaps;
- tasks/workplan, если gaps ещё не закрыты.

### r3 — opportunity with ranked existing solution hypotheses

нужно:

- 1–3 solution hypotheses, если они есть или prodakt попросил их проработать;
- привязка каждой hypothesis к problem component;
- fast ranking / recommendation;
- before-prd unknowns/tasks.

важно:

```text
r3 ≠ высокий приоритет
r3 ≠ prd
r3 ≠ delivery commitment
r3 ≠ acceptance criteria
```

## 4. три mvp-сценария

мы делаем сразу три сценария, но они не отдельные демо. они протекают друг в друга.

### scenario c — solution idea → detox → r0/r1

вход:

```text
“нужно сделать рекомендованную цену”
```

плагин:

- не принимает это как opportunity;
- запускает detox;
- ищет underlying problem;
- если проблема не ясна, сохраняет r0 solution-signal;
- если проблема ясна, формирует r1 opportunity.

### scenario b — raw signal → r0/r1 skeleton

вход:

```text
“продавцы спрашивают, какую цену поставить”
```

плагин:

- сохраняет r0 signal;
- задаёт минимальные grill-me вопросы;
- если хватает ответов, формирует r1;
- если не хватает, оставляет r0 + unknowns + tasks.

минимальные вопросы для r0 → r1:

```text
1. кто затронут?
2. в каком сценарии это происходит?
3. что именно идёт не так?
4. как мы это заметили?
5. почему это может быть важно?
```

### scenario a — existing weak opp doc → improved doc + gaps + tasks

вход:

- существующий opp doc;
- слабый или solution-first документ;
- много текста без ясной проблемы;
- нет sizing / evidence / decomposition.

плагин:

- определяет текущий r-level;
- находит solution-first подмены;
- разделяет fact / assumption / unknown;
- находит gaps;
- генерирует tasks;
- переписывает документ problem-first человеческим языком;
- собирает compact backlog card;
- показывает next step.

## 5. skills / loops

в терминах плагина лупы можно считать skills.

### skill 1. intake & framing

цель: довести вход до r0/r1.

запускается для:

- raw signal;
- solution idea;
- fragment;
- existing doc, где проблема не ясна.

контракт:

```text
input: raw signal / solution idea / doc fragment
output: r0/r1 opp doc skeleton, problem-first statement, unknowns, first gaps, next questions/tasks
```

петля возвращается назад, если:

- problem statement слишком общий;
- solution притворяется problem;
- непонятен пользователь;
- непонятен сценарий;
- pm не может ответить.

### skill 2. gap resolution

сердце продукта.

```text
gap analysis
  → tasks
  → user brings task results
  → living opp doc update
  → gap analysis again
  → readiness recalculation
```

важно: после выполнения задач всегда возвращаемся в gap analysis, а не идём вслепую дальше.

контракт:

```text
input: current opp doc, current readiness, known gaps, new task results
output: updated opp doc, updated readiness, gap list, tasks, next step, compact backlog card
```

### quality pass

не отдельный большой workflow, а обязательный санитарный проход перед результатом.

проверяет:

- claims разделены на fact / assumption / unknown;
- нет solution-first подмены;
- нет delivery language;
- нет ai-slop;
- tl;dr можно понять за 30 секунд;
- gaps не замазаны красивым текстом.

## 6. living opportunity doc

opp doc — основной контейнер.

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

важно: это один документ, но не всё должно быть одинаково видимо. сверху должна жить compact card и readiness/next step. операционные детали могут быть ниже.

## 7. compact backlog card

самая компактная карточка для opportunity backlog:

```text
signal
problem
potential solutions
priority data
readiness / status
next step
```

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

карточка генерируется даже для r0/r1, но с явным readiness и next step.

## 8. priority data для opportunity backlog

для mvp не делаем финальный score числом. показываем dimensions low/medium/high.

5 компонентов:

```text
1. volume
2. severity
3. addressability
4. strategic fit
5. urgency
```

confidence не включаем в priority, чтобы не смешивать приоритет и readiness. confidence живёт рядом в readiness / claim quality.

позже возможная формула:

```text
opportunity potential = volume × severity × addressability
opportunity timing = strategic fit × urgency
opportunity score = opportunity potential × opportunity timing
```

но не для mvp: слишком высок риск ложной точности.

## 9. gaps

gap severity:

```text
critical — блокирует readiness transition или solution backlog candidate
major — снижает confidence, но не блокирует
minor — улучшает качество, но можно жить
```

пример critical gaps:

- неясно, кто пользователь;
- неясен сценарий;
- неясна проблема;
- solution без opportunity;
- нет evidence вообще;
- нет rough sizing для r2;
- нет decomposition для широкой opportunity;
- нет понимания addressability;
- нет parent component для solution hypothesis.

## 10. tasks

задачи — способ двигать opportunity по readiness.

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

после выполнения task:

```text
user приносит результат
→ плагин обновляет opp doc
→ закрывает или обновляет linked gap
→ запускает gap analysis again
→ пересчитывает readiness
→ может создать новые gaps/tasks
```

## 11. solution hypotheses

в mvp плагин не предлагает новые решения проактивно.

правило:

```text
если solution hypotheses уже есть в исходном документе — проверяем и приводим в порядок.
если их нет — не генерируем без просьбы pm.
```

если решение есть, оно должно быть привязано к:

- parent opportunity;
- target problem component;
- expected mechanism.

r3 может содержать ranked existing solutions, но top hypothesis не является delivery commitment.

## 12. главный экран результата

решение: hybrid result screen.

сверху:

```text
readiness
workflow status
scenario
главный вывод
next step
priority data
```

ниже вкладки / секции:

```text
improved opp doc
gaps
tasks
claim warnings
backlog card
```

первый экран должен дать pm ответ:

```text
где я сейчас?
чего не хватает?
что делать дальше?
какой обновлённый opp doc получился?
можно ли это положить в backlog?
```

главный wow первого демо:

```text
плохой док стал хорошим
+
pm понял, чего не хватает
```

## 13. mvp scope

### делаем

- один textarea на вход;
- classifier сам определяет: signal / solution idea / existing opp doc / unclear fragment;
- подтверждение классификации;
- три connected сценария;
- readiness r0–r3;
- gap analysis;
- task generation;
- human rewrite;
- claim warnings summary;
- compact backlog card;
- task result intake loop;
- connected-flow prototype.

### не делаем в mvp

- quarterly planning;
- автоматическое создание задач в jira;
- полноценный solution backlog workflow;
- prd generation;
- детальную delivery-декомпозицию;
- architecture / acceptance criteria / ux-макеты;
- сложный product context config workflow;
- финальную opportunity score formula.

## 14. product context config

конфиг нужен, но в mvp только mock config.

позже в конфиге должны жить:

- product domain;
- team;
- pm / owners;
- основные сегменты;
- основные сценарии;
- north-star / guardrail metrics;
- доменные метрики;
- dashboards;
- event taxonomy;
- typical evidence sources;
- typical decomposition axes;
- strategic goals;
- stakeholders;
- task templates;
- readiness preferences;
- scoring preferences.

opp doc workflow должен использовать конфиг, но создание/обновление конфига — отдельная большая проработка.

## 15. риски и self-roast

### риск 1. аэропорт вместо терминала

мы легко можем переусложнить систему: 25 workflows, 17 blocks, агенты, статусы. для mvp нужно держать фокус:

```text
3 scenarios
2 skills/loops
1 quality pass
1 living opp doc
1 compact backlog card
```

### риск 2. reviewer вместо продукта

если плагин только говорит “не хватает sizing”, это занудный reviewer.

он должен снимать работу:

- переписать;
- сжать;
- найти gaps;
- превратить gaps в tasks;
- показать next step;
- собрать backlog card.

### риск 3. opp doc как помойка

если всё хранить в одном документе, он может стать нечитаемым. решение: два слоя.

```text
human-readable doc — короткий, problem-first
operational metadata — gaps, tasks, claim map, служебное
```

### риск 4. false precision в scoring

не считать score числом в mvp. показывать dimensions.

### риск 5. r3 тянет в prd

top solution hypothesis нужно явно маркировать как next exploration direction, а не commitment.

### риск 6. config может съесть проект

config нужен, но его большой workflow не делать в mvp.

## 16. следующий шаг

следующий продуктовый артефакт:

```text
mvp result screen spec
```

нужно подробно спроектировать:

- layout;
- основные блоки;
- primary cta;
- empty states;
- weak input states;
- how gaps are shown;
- how tasks are shown;
- how rewritten opp doc is shown;
- how backlog card is shown;
- how pm brings task result;
- how readiness recalculation happens.

## 17. прототип

connected-flow html prototype лежит рядом:

```text
docs/opportunity-doc-plugin/prototype-flow.html
```

он показывает, как три сценария протекают друг в друга:

```text
solution idea
  → raw signal
  → weak opp doc
  → gap tasks
  → task result
  → doc update / gap analysis again
```
