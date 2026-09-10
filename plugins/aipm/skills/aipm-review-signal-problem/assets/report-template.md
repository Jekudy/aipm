# Шаблон отчёта

Три слоя в фиксированном порядке: человеческий (наружу), машинный (под свёрнутым блоком в конце), append-only блок аудита (только при явной просьбе записать в документ).

Человеческий слой — перевод машинного по [глоссарию](glossary.md): каждый пункт соответствует ровно одному `issue`, новых фактов в нём нет. Коды (`NOT_READY`, `PROVIDE_EVIDENCE`, `S-02` и подобные) в человеческом слое запрещены; D1, D2, D5 пишутся вместе с расшифровкой из глоссария. Не больше 25 строк без машинного слоя.

## Человеческий слой

```markdown
## Проверка: {название документа}

**Что проверяли:** можно ли принять решение «{переход словами}» ({D-код}).
**Вердикт:** {Достаточно, можно принимать решение | Недостаточно: {N} препятствий | Проверка не началась: {причина словами}}
**Почему:** {одна фраза: главное препятствие или главная опора; при D5 добавь «остановить» или «заморозить»}

### Чего не хватает (показано {n}, ещё {m} в машинном слое)
1. **{Что не так: одной фразой по содержанию документа, без служебного префикса вроде «В документе этого нет:»}**
   Где: «{дословная цитата}», {место}. {Если в документе нет: «в документе не нашли, искали: {граница поиска}»}
   Что сделать: {действие из глоссария, конкретизированное под документ}. Кто: {автор | аналитик | {сторона}}.
   Готово, когда: {acceptance_test того же instance словами}.
2. …
3. …

### Что перевернуло бы вывод
{decision_flipping_observation словами}. В документе: {есть, вывод устоял | нет, наблюдение против вывода | данных для этой проверки нет}.

### Границы проверки
Прочитано: {названия ресурсов}. Не прочитано: {названия или «ничего»}. Недоступно: {названия или «ничего»}.
```

Правила:

- Порядок пунктов: `BLOCKS_ASSESSMENT → BLOCKS_DOSSIER → CHANGES_CANDIDATE → NO_CURRENT_EFFECT`, затем стабильный `issue_id`; показывать максимум три, остальные считать в «ещё {m}».
- Критерий называется текстом из каталога, а не ID.
- При «Достаточно» блок «Чего не хватает» заменяется строкой «Препятствий нет»; улучшения и похвалу не добавлять.
- При `BLOCKED` после «Вердикта» идёт ровно один вопрос с вариантами словами; блоки «Чего не хватает», «Что перевернуло бы вывод» и «Границы» опускаются, машинный слой остаётся.

Пример блокировки:

```markdown
## Проверка: Страница с условиями сотрудничества

**Что проверяли:** не удалось определить.
**Вердикт:** Проверка не началась: в документе не сказано, какое решение по нему принимают.

Какое решение проверяем?
- D1: взять сигнал в работу;
- D2: признать проблему подтверждённой и открыть поиск решений;
- D5: остановить или заморозить инициативу.
```

## Машинный слой

Сразу после человеческого слоя, обёрнутый в `<details><summary>Машинный слой</summary> … </details>`. Схема не меняется:

```yaml
audit:
  rubric_version: "criteria-d1-d2-d5@1.0.0"
  model_version: <exact id>
  transition: D1 | D2 | D5
  track: discovery
  thread_id: <stable id>
  dossier_status: DECISION_READY_DOSSIER | NOT_READY | BLOCKED
  transition_candidate: D2_CANDIDATE | CONTINUE_CANDIDATE | STOP_CANDIDATE | BLOCKED
  canonical_transition_candidate: D2_CANDIDATE | CONTINUE_CANDIDATE | D5_STOP_CANDIDATE | D5_PARK_CANDIDATE | NO_CANDIDATE
  candidate_available: true | false
  d5_mode: STOP | PARK | null
  decision_outcome: TAKE_SIGNAL_INTO_DISCOVERY | OPEN_SOLUTION_DISCOVERY | CONTINUE_PROBLEM_DISCOVERY | STOP | PARK | NOT_DECIDED
  problem_status:
    central_hypothesis: SUPPORTS | REFUTES | MIXED | DOES_NOT_BEAR | UNKNOWN
    occurrence: SUPPORTS | REFUTES | MIXED | DOES_NOT_BEAR | UNKNOWN
    reach: SUPPORTS | REFUTES | MIXED | DOES_NOT_BEAR | UNKNOWN
    harm: SUPPORTS | REFUTES | MIXED | DOES_NOT_BEAR | UNKNOWN
  essential_claims: {claim_id: SUPPORTS | REFUTES | MIXED | DOES_NOT_BEAR | UNKNOWN}
  below_attention: {rule_id, result} | null
  source_coverage:
    status: COMPLETE | INCOMPLETE | NOT_ASSESSABLE
    resources: [{resource_id, locator, scope_state, review_state, required_by}]
  claim_inventory:
    class_counts: {NUMBER, PERCENT, MULTIPLIER_EXACT, MULTIPLIER_RHETORICAL, TIMESPAN_EXACT, TIMESPAN_DESCRIPTIVE, QUOTE, COMPARISON, INTENSIFIER, OWNER}
  limitations: [{limitation_id, type, claim_ids, resource_ids, detail}]
  criteria:
    - {id, applicability, applicability_rule_id, assessability, result, primary_reason, anchor}
  issues:
    - {issue_id, kind, criterion_id, primary_reason, anchors, candidate_impact, action, target_ids, acceptance_test}
  falsification:
    status: NO_FINDING | FINDING_RAISED | CANNOT_ASSESS
    claim_ids: [<ids>]
    resource_ids: [<supplied ids>]
    decision_flipping_observation: <bounded statement or null>
    finding: <bounded statement or null>
  omitted_count: <integer >= 0>
```

Все machine issues сохраняются в машинном слое. Finding не меняет result или candidate, пока владелец не примет его как новый claim/unknown и не запустит аудит заново.

## Append-only audit layer

Записывай этот блок в конец исходного документа только при явной просьбе изменить источник. Иначе верни его готовым для вставки. Здесь хранятся подтверждённые атомы; во внешнем feedback их не повторяют.

```markdown
## Аудит сигнала и проблемы

### {YYYY-MM-DD HH:MM} — {transition}, rubric v1.0.0

- Вердикт: {dossier_status} / {transition_candidate}; candidate_available={value}; d5_mode={value}; решение владельца={не принято | значение}
- Границы: {source coverage summary}
- Подтверждено:
  - [{criterion_instance_id}] «{дословная цитата}» — {location}; evidence={evidence_id | не требуется}
- Открытые расхождения: {issue_ids или «нет»}
- Проход-опровержение: {status}; «{bounded finding или наблюдение}»; опоры={claim/resource ids}
```

Новый прогон добавляет запись, а не переписывает предыдущую.
