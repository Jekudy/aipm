# ai pm plugin architecture handoff v0.3

дата: 2026-07-03  
статус: внутренний архитектурный контекст проекта  
репозиторий: `Jekudy/aipm`

## 0. зачем этот документ

этот документ фиксирует полный контекст архитектурной проработки ai-плагина для продуктовой работы. это не презентация для продактов и не финальный prd. это handoff для продолжения проектирования и разработки.

мы много обсуждали, как помочь продактам авито быстрее и качественнее проходить базовые задачи:

- интерпретировать сигнал;
- доводить сигнал до opportunity doc;
- генерировать и отбирать решения-кандидаты;
- вести решение до prd;
- управлять двумя backlog-ами;
- планировать квартал через discovery / delivery bets;
- возвращать продакта к продуктовой дисциплине.

---

## 1. главный вывод

мы строим не генератор opportunity doc / prd / квартального плана.

мы строим ai-систему, которая помогает продакту двигать продуктовую работу по зрелости:

```text
signal
→ opportunity
→ solution candidates
→ prd
→ backlog / prioritization
→ quarterly planning
```

ключевая идея:

```text
документ — не главная сущность.
документ — это представление состояния сущности.
```

то есть:

```text
opportunity doc = представление состояния opportunity item
prd = представление состояния solution item
quarter plan = представление набора bets / commitments
```

плагин должен помогать не просто “писать текст”, а:

- понять, что принес пользователь;
- определить стадию работы;
- найти похожие сущности в backlog;
- понять, чего не хватает;
- провести по правильному flow;
- проверить готовность к следующему шагу;
- создать / обновить артефакт;
- положить результат в нужный backlog;
- вернуть продакта к дисциплине.

самая важная формула:

```text
плагин не начинает с генерации документа.
плагин начинает с диагностики состояния работы.
```

---

## 2. главный продуктовый принцип

плагин должен быть:

- product buddy;
- исследовательным критиком мышления;
- помощником в структурировании;
- навигатором по maturity;
- охранником продуктовой дисциплины.

но он не должен превращаться в микроменеджера.

важная поправка: не надо опускаться до чрезмерной детализации и управлять каждой микросекцией как маленьким бюрократическим светофором. сильные модели могут работать хуже, если задавить их слишком жесткими правилами, чеклистами и микроконтролем.

правильный подход:

```text
структурировать ai-специалиста через:
- что мы хотим получить;
- чего мы не хотим получить;
- какие ошибки он должен ловить;
- какой уровень свободы у модели;
- где нужно решение человека.
```

неправильный подход:

```text
сделай шаг 1.1.1;
потом шаг 1.1.2;
потом обязательно спроси поле 37;
потом поставь статус каждому блоку;
потом инвалидируй все downstream-блоки.
```

контракты и maturity нужны как рамка поведения, а не как корпоративный excel-ад.

---

## 3. что мы не строим

anti-goals:

- не строим генератор красивой воды;
- не строим систему, которая ускоряет хаос;
- не делаем tech decomposition за разработчиков;
- не пытаемся сразу построить идеальный planning module;
- не делаем слишком тяжелый context module на первом этапе;
- не описываем контракты как обязательные страницы в stash;
- не микроменеджим каждый блок документа;
- не заставляем все квартальные ставки притворяться metric bets;
- не строим тяжелый revision / invalidation log на старте.

отдельно зафиксировано:

```text
модуль декомпозиции пока не лезет в техническую декомпозицию.
```

он может помогать понять:

- продуктовые компоненты;
- этапы работы;
- зависимости;
- последовательность;
- параллельность;
- maturity milestones;
- что может не поместиться;
- что можно порезать.

но не должен делать:

- api;
- backend/frontend tasks;
- архитектуру сервисов;
- таблицы;
- технические таски.

это пока остается за инженерной командой.

---

## 4. правильный путь + разные точки входа

мы пришли к сильной модели:

```text
есть canonical flow — правильный путь взросления сущности;
пользователь может войти в этот flow с любого места;
система должна понять, где он вошел;
помочь добрать недостающее;
и продолжить движение дальше.
```

пример для opportunity:

```text
raw signal
→ framed opportunity
→ evidence-backed opportunity
→ decision-ready opportunity
→ 1–3 solution candidates
→ solution backlog
```

пример для solution / prd:

```text
solution candidate
→ framed solution
→ prd-ready solution
→ prd-r1
→ prd-r2
→ prd-r3
```

пример для planning:

```text
intent / goal
→ candidate bets
→ discovery / delivery classification
→ shortlist
→ rough fit
→ weekly / sprint plan
→ committed quarter plan
```

важная мысль:

> если мы пишем док с нуля, в идеальном мире мы пишем его последовательно, не переписывая старые части. если приходится постоянно переписывать старые части — возможно, проблема в структуре.

это принимается как дизайн-принцип, но без тяжелой механики “инвалидировать downstream-блоки”. эту механику сейчас не берем: она переусложняет систему.

рабочая позиция:

```text
плагин помогает двигаться последовательно;
если пользователь пришел в середину — диагностирует, чего не хватает;
если ранняя часть слабая — мягко возвращает к ней;
но не строит бюрократическую систему инвалидирования всего ниже по цепочке.
```

---

## 5. зрелость: важное уточнение

зрелость не равна “заполнены блоки документа”.

зрелость — это готовность сущности к следующему meaningful decision.

она зависит от:

- есть ли нужные элементы;
- достаточно ли они качественные;
- подтверждены ли важные claims;
- нет ли противоречий;
- можно ли принять следующее решение;
- понятны ли риски и неизвестные.

пример:

```text
блок “сегмент” заполнен как “все пользователи авито”.
формально блок заполнен.
по смыслу — мусор.
```

поэтому:

```text
у сущности есть maturity level;
у документа есть важные смысловые блоки;
плагин может сказать, какие блоки weak / missing / unclear;
но не надо превращать это в детальную систему статусов на каждый абзац.
```

---

## 6. user-facing архитектура

пользовательские модули:

```text
0. context collection / onboarding
1. entry / router
2. opp doc module
3. opp backlog module
4. solution / prd module
5. solution / prd backlog module
6. planning module
```

### 6.1 context collection / onboarding

context module активируется в начале.

его задача:

- понять специфику продакта / команды / продукта;
- собрать базовый reusable context;
- подгружать этот context в остальные workflow.

на первом этапе он мокаeтся, а не строится полноценно.

mock context pack:

```text
product_area
team
pm_level
user_segments
core_scenarios
main_metric
input_metrics
guardrail_metrics
current_goals
strategic_context
data_sources
research_sources
stakeholders
delivery_cadence
rough_capacity
artifact_templates
constraints
```

важно: context module в начале активируется явно, но позже может вызываться снова, если системе не хватает контекста.

пример:

```text
не понимаю, какая метрика для этой работы главная.
не знаю, какие источники evidence доступны.
не понимаю, кто принимает решение.
```

### 6.2 entry / router

это отдельный важный пользовательский слой.

пользователь может прийти с чем угодно:

- сырым сигналом;
- идеей решения;
- слабым opportunity doc;
- solution candidate;
- prd;
- целью на квартал;
- кучей инициатив;
- существующим backlog item;
- фразой “я не знаю, на какой я стадии”.

router должен:

- классифицировать вход;
- понять entity type;
- понять стадию / maturity;
- найти похожие items в backlog;
- предложить продолжить существующую сущность или создать новую;
- выбрать подходящий workflow;
- не дать плодить дубли.

пример поведения:

```text
pm:
хочу сделать подсказки новым продавцам при подаче объявления.

plugin:
похоже, ты пришел с solution idea.
я нашел похожую opportunity: opp-123 про низкую активацию новых продавцов.
это продолжение opp-123 или новая идея?

варианты:
a. привязать как solution candidate к opp-123
b. создать новую opportunity
c. сначала пройти solution detox и понять, какую проблему решаем
```

это must-have, потому что в реальности уже будет существовать backlog, и люди будут приносить похожие идеи.

### 6.3 opp doc module

главный первый модуль.

задача:

```text
вести opportunity item от сигнала до opp-r3
и породить 1–3 solution candidates.
```

entry points:

- у меня сырой сигнал;
- у меня слабый opportunity doc;
- я пришел с решением, но не доказал проблему;
- у меня существующий backlog item;
- у меня новый сигнал, похожий на старую opportunity.

maturity:

```text
opp-r0: raw signal
opp-r1: framed opportunity
opp-r2: evidence-backed opportunity
opp-r3: decision-ready opportunity
```

выходы:

- opportunity doc;
- gaps;
- validation tasks;
- maturity assessment;
- decision summary;
- 1–3 solution candidates;
- обновление opportunity backlog;
- создание / обновление solution backlog items.

важнейший паттерн:

```text
solution idea detox
```

если pm приходит с фичей:

```text
давайте сделаем ai-помощника
давайте добавим подсказки
давайте изменим форму
```

плагин не запрещает, но возвращает к дисциплине:

- какую проблему решаем?
- для кого?
- в каком сценарии?
- какое поведение хотим изменить?
- какую метрику / outcome хотим сдвинуть?
- какие альтернативные решения есть?
- есть ли похожая opportunity в backlog?

исходная идея становится solution candidate, а не “истиной”.

### 6.4 opp backlog module

это не просто внутреннее хранилище. пользователь должен явно видеть и активировать управление opportunity backlog.

модуль управляет:

- signals;
- opportunity candidates;
- opportunity docs;
- статусами;
- maturity;
- дублями;
- слиянием сигналов;
- prioritization;
- stale items;
- park / kill / continue decisions.

важные сценарии:

- пользователь накидывает новый сигнал;
- система ищет похожие opportunities;
- плагин спрашивает: это продолжение старой идеи или новая?
- плагин помогает отличить duplicate от genuinely new;
- плагин помогает приоритизировать opportunities.

это включает приоритизацию, но не в смысле “магически решить за продакта”, а в смысле:

- нормализовать items;
- подсветить impact/confidence/urgency/strategic fit;
- найти дубли;
- показать, что stale;
- подготовить decision summary.

### 6.5 solution / prd module

ключевая идея:

```text
prd — это следующий этап solution candidate.
```

не так:

```text
solution отдельно, prd отдельно.
```

а так:

```text
solution item взрослеет до prd.
```

maturity path:

```text
sol-s0: solution candidate
sol-s1: framed solution
sol-s2: prd-ready solution
prd-r1: prd skeleton
prd-r2: review-ready prd
prd-r3: delivery/test-ready prd
```

entry points:

- у меня есть solution candidate, можно ли писать prd?
- я выбрал решение и хочу первый prd;
- у меня сырой prd;
- prd расползается;
- непонятно, готов ли prd к работе.

плагин помогает:

- проверить связь с parent opportunity;
- сформулировать product hypothesis;
- понять target behavior;
- собрать scope / out of scope;
- предложить метрики;
- найти risks / unknowns;
- сжать scope;
- понять readiness.

выходы:

- prd readiness check;
- prd-r1 skeleton;
- улучшенный prd;
- scope / out of scope;
- метрики и guardrails;
- open questions;
- риски;
- delivery/test readiness decision.

### 6.6 solution / prd backlog module

второй явный backlog management tool.

он управляет:

- solution candidates;
- гипотезами;
- prd candidates;
- prd maturity;
- readiness;
- приоритизацией;
- дублями;
- park / kill / continue;
- выбором решений в работу.

важно:

```text
solution backlog не должен становиться помойкой идей.
```

в него нельзя класть просто:

```text
сделать ai-помощника.
```

нормальный solution backlog item должен иметь хотя бы:

- parent opportunity;
- какую проблему решает;
- для какого сегмента;
- solution hypothesis;
- target behavior;
- target outcome / metric;
- почему это может сработать;
- ключевые assumptions.

но без фанатизма и бюрократии.

### 6.7 planning module

planning — последнее, потому что он должен смотреть на все:

- context;
- opportunity backlog;
- solution / prd backlog;
- maturity каждого item;
- цели / intents;
- capacity;
- зависимости;
- готовность ставок.

уточнение: не все квартальные ставки обязаны быть metric bets.

в реальности бывают стратегические research / discovery, которые могут дать impact только через год.

честная модель:

```text
каждая ставка должна быть связана с intent.
metric goal — частый, но не единственный intent.
```

intent types:

```text
metric intent — хотим изменить метрику
strategic learning intent — хотим разобраться в большой теме
capability / platform intent — строим способность
risk / quality / compliance intent — снижаем риск или долг
business / stakeholder intent — явная бизнесовая необходимость
```

типы ставок пока оставляем двумя:

```text
discovery bet:
signal / opportunity → solution candidates

delivery bet:
solution / hypothesis / prd → prod / test
```

эксперимент пока внутри delivery bet:

```text
delivery_mode:
experiment / mvp / rollout / full launch / test
```

planning module помогает:

- от intent / цели найти candidate bets;
- классифицировать discovery vs delivery;
- сформировать shortlist;
- показать, что не готово;
- показать, что не берем;
- проверить rough fit;
- разложить по неделям / спринтам через maturity milestones.

важно:

```text
planning раскладывает не просто задачи,
а движение сущностей по зрелости.
```

пример:

```text
discovery bet:
opp-r1 → opp-r2 → opp-r3 → solution candidates

delivery bet:
solution candidate → prd → prod / test
```

---

## 7. core system layers

внутренние системные слои:

```text
a. mock context layer → later real context layer
b. entity graph
c. state / maturity engine
d. contract engine
e. workflow registry
f. backlog state store
g. artifact renderer / parser
h. quality / eval layer
```

ранее обсуждался тяжелый decision / revision log, но решили не раздувать это сейчас. можно оставить легкий trace, где нужно, но не строить сложную систему revision / downstream invalidation.

### 7.1 context layer

на первом этапе mocked.

зачем нужен:

- чтобы ai не работал в вакууме;
- чтобы workflow знали специфику команды / продукта / метрик;
- чтобы не задавать каждый раз одни и те же вопросы.

позже превращается в полноценный context collection module.

### 7.2 entity graph

сердце системы.

мы думаем сущностями, а не документами.

сущности:

```text
signal
opportunity item
solution candidate / solution item
prd state
quarter bet
intent / goal
metric
evidence
assumption
risk
decision
```

связи many-to-many:

```text
одна opportunity может иметь много signals;
один signal может относиться к нескольким opportunities;
одна opportunity порождает 1–3 solution candidates;
один solution candidate может закрывать несколько opportunities;
один quarter bet может включать несколько opportunities / solutions;
одна метрика может связывать много opportunities / bets.
```

это важно, потому что реальная продуктовая работа не линейна.

### 7.3 maturity engine

определяет текущую зрелость сущности и следующий meaningful step.

не должен превращаться в микроменеджмент блоков.

задачи maturity engine:

- понять, можно ли принимать следующее решение;
- сказать, чего критически не хватает;
- не дать слабому документу притворяться зрелым.

пример:

```text
это похоже на opp-r1, но не opp-r2:
- есть гипотеза проблемы;
- есть сегмент;
- но нет evidence;
- impact не обоснован;
- альтернативные объяснения не проверены.
```

### 7.4 contract engine

контракты нужны как рамка проектирования поведения системы.

контракт отвечает:

- что должно быть известно, чтобы перейти дальше?
- какой output должен появиться?
- какие ошибки надо поймать?
- где нужен human approval?

но контракты не обязательно описывать в stash как отдельные страницы. они нужны нам сейчас, чтобы проектировать модули и workflow.

важно:

```text
контракты не должны душить сильную модель.
они должны задавать boundaries:
что получить / чего избежать / где остановиться.
```

предварительная contract map:

```text
c1. raw input → classified entry
c2. signal → opp-r1
c3. opp-r1 → opp-r2
c4. opp-r2 → opp-r3
c5. opp-r3 → solution candidate
c6. solution candidate → prd-ready solution
c7. prd-r1 → prd-r2
c8. prd-r2 → prd-r3
c9. backlog item → quarter candidate bet
c10. selected bets → weekly / sprint maturity plan
```

контракты надо прорабатывать отдельной сессией.

### 7.5 workflow registry

workflow registry — это machine-readable каталог разрешенных движений системы.

не для человека каждый день. для llm / агента.

он описывает:

- с каким input пришел пользователь;
- какое состояние сейчас;
- куда можно вести сущность;
- какой контекст нужен;
- какие контракты проверить;
- какой output создать;
- какие решения должен подтвердить человек.

пример по-человечески:

```text
workflow:
solution idea detox

input:
сырая идея решения

output:
opp-r1 + исходная идея как possible solution candidate

задача:
не дать фиче притвориться проблемой.
```

machine-readable format можно прорабатывать позже. сначала нужно хорошо понять сами flow.

### 7.6 backlog state store

хранит состояние backlog items.

на первом этапе может быть мок:

```text
json
markdown
таблица
локальный файл
простая база
```

нужен уже в phase 1, потому что opp doc module должен уметь:

- создать opportunity item;
- найти похожий item;
- обновить maturity;
- породить solution candidates;
- положить их в mock solution backlog.

### 7.7 artifact renderer / parser

слой, который превращает state в документ и обратно.

```text
entity state → rendered artifact
artifact draft → extracted entity state
```

это важно, потому что пользователь может принести уже существующий doc.

плагин должен уметь:

- прочитать слабый opportunity doc;
- понять maturity;
- найти gaps;
- обновить state;
- сгенерировать улучшенную версию.

### 7.8 quality / eval layer

позже нужен для проверки качества outputs.

пока не главный фокус, но в backlog стоит положить:

- симуляции;
- тестовые кейсы;
- quality rubrics;
- good/bad examples.

---

## 8. ключевые решения

### решение 1. два backlog-а

есть две очереди принятия решений:

```text
opportunity backlog:
какие проблемы / opportunities достойны внимания?

solution / prd backlog:
какие решения / гипотезы достойны prd / delivery / test?
```

это разные очереди, разные критерии, разная приоритизация.

### решение 2. signal и opportunity doc — состояния одного item

```text
opportunity backlog item
  → raw signal
  → framed opportunity
  → evidence-backed opportunity
  → decision-ready opportunity
```

### решение 3. solution candidate и prd — состояния одного item

```text
solution backlog item
  → solution candidate
  → framed solution
  → prd-ready solution
  → prd-r1
  → prd-r2
  → prd-r3
```

### решение 4. opportunity doc заканчивается не одним финальным решением

opportunity doc должен доводить до:

- decision-ready opportunity;
- решения kill / park / continue / generate solutions;
- 1–3 solution candidates.

opportunity doc не обязан выбрать одно решение. он должен породить нормальные кандидаты.

### решение 5. prd начинается с выбранного solution candidate

prd — следующий этап solution item.

он не должен начинаться с сырого сигнала или просто хотелки.

### решение 6. квартал имеет два основных типа ставок

```text
discovery bet:
signal / opportunity → solutions

delivery bet:
solution / hypothesis / prd → prod / test
```

эксперимент пока внутри delivery bet.

### решение 7. не все ставки обязаны быть metric bets

добавляем intent types:

- metric;
- strategic learning;
- capability / platform;
- risk / quality;
- business / stakeholder.

каждая ставка должна иметь intent и контролируемый quarter outcome.

### решение 8. плагин должен искать дубли

при новом сигнале / идее плагин должен проверять backlog:

- это похоже на существующую opportunity?
- это продолжение старой идеи?
- чем новая идея отличается?
- создаем новое или линковать к существующему?

### решение 9. плагин должен возвращать к дисциплине

пример поведения:

```text
pm просит: напиши prd.

plugin сначала диагностирует:
- это вообще solution candidate?
- есть parent opportunity?
- понятен target behavior?
- есть success metric?
- готово ли к prd?

и только потом помогает писать.
```

---

## 9. как проектировать ai-специалистов

не надо микроменеджить сильные модели.

каждого “виртуального специалиста” лучше описывать через:

- роль;
- цель;
- вход;
- желаемый выход;
- что он обязан проверять;
- чего он не должен делать;
- какие типичные ошибки ловит;
- где просит human confirmation;
- какой стиль помощи нужен.

пример:

### specialist: solution idea detoxer

цель:

```text
не дать идее решения притвориться проблемой.
```

хочет получить:

- problem hypothesis;
- target user / segment;
- scenario;
- target behavior;
- metric / outcome;
- original idea as solution candidate;
- альтернативные решения.

не хочет получить:

- prd из воздуха;
- уверенное утверждение, что фича нужна;
- натягивание проблемы под любимое решение;
- игнорирование похожих opportunities.

это лучше, чем заставлять модель идти по 40 микрошагам.

---

## 10. roadmap разработки

### phase 0. mock context

не строим полноценный context module.

делаем простой context pack, чтобы первые workflow не работали в вакууме.

### phase 1. opp doc module

первый настоящий инкремент.

объем:

- mock context;
- entry/router lite;
- opportunity entity;
- opp maturity r0/r1/r2/r3;
- canonical flow для opp doc;
- solution idea detox;
- weak opp doc review;
- solution candidate generation;
- mock opp backlog;
- mock solution backlog;
- duplicate detection lite.

цель:

```text
пользователь приходит с signal / weak opp / solution idea;
плагин ведет его до opp-r3;
на выходе есть opportunity doc и 1–3 solution candidates;
solution candidates можно положить в mock solution backlog.
```

### phase 2. solution / prd module

после opp doc.

цель:

```text
solution candidate
→ prd readiness
→ prd-r1/r2/r3
```

ключевые сценарии:

- можно ли уже писать prd;
- создать prd-r1;
- отревьюить сырой prd;
- сжать scope;
- понять readiness.

### phase 3. backlog modules

после того как понятны сущности и states.

делаем:

- opp backlog module;
- solution / prd backlog module.

функции:

- управление очередями;
- поиск дублей;
- prioritization;
- stale items;
- park / kill / continue;
- readiness views;
- что готово к следующему шагу.

### phase 4. planning module

после backlog modules.

цель:

```text
intent / goal
→ candidate bets
→ discovery / delivery classification
→ shortlist
→ rough fit
→ weekly / sprint maturity plan.
```

planning должен смотреть на:

- context;
- opp backlog;
- solution/prd backlog;
- maturity;
- capacity;
- dependencies;
- intent type.

### phase 5. real context module

возвращаемся к context module после того, как понятно, какие контекстные поля реально нужны.

не строим “богатый профиль pm” заранее.

---

## 11. короткий glossary

```text
entity
реальная рабочая сущность: opportunity item, solution item, quarter bet.

artifact
видимое представление сущности: opportunity doc, prd, quarter plan.

maturity
готовность сущности к следующему meaningful decision.

canonical flow
идеальный путь взросления сущности.

entry point
момент, в который пользователь входит в flow: signal, idea, weak doc, prd, goal.

contract
рамка перехода: что должно быть известно, что нельзя пропустить, где нужен человек.

router
слой, который понимает, с чем пришел пользователь и куда вести.

opportunity backlog
очередь сигналов / opportunities.

solution / prd backlog
очередь решений / гипотез / prd-items.

discovery bet
ставка “дойти от signal / opportunity до solution candidates”.

delivery bet
ставка “дойти от solution / hypothesis / prd до prod / test”.

intent
зачем ставка существует: metric, strategic learning, capability, risk, business.
```

---

## 12. финальная формулировка проекта

мы проектируем ai-плагин для pm, который помогает не писать документы ради документов, а двигать продуктовую работу по зрелости.

пользователь может прийти с сигналом, идеей решения, слабым доком, prd, backlog item или квартальной целью.

система диагностирует вход, ищет похожие сущности в backlog, определяет maturity, подгружает нужный workflow, помогает добрать недостающее, генерирует / ревьюит артефакты и двигает item дальше.

главные пользовательские зоны:

```text
context/onboarding
router
opp doc
opp backlog
solution/prd
solution/prd backlog
planning
```

первый инкремент:

```text
mock context + router lite + opp doc module + mock backlogs
```

главный принцип:

```text
не ускорять хаос, а возвращать продакта к дисциплине.
```
