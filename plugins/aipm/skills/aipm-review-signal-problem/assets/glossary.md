# Глоссарий: код машинного слоя → фраза человеческого слоя

Закрытый список. Скилл подставляет фразу справа и никогда не показывает код слева в человеческом слое. Если код не найден в глоссарии, это дефект скилла, а не повод сочинить фразу.

## Переходы

| Код | Фраза |
|---|---|
| D1 | взять сигнал в работу |
| D2 | признать проблему подтверждённой и открыть поиск решений |
| D3 | зафиксировать выбор решения |
| D4 | позвать команду, документ готов к PRD |
| D5 | остановить или заморозить инициативу |
| track=discovery | (не показывать) |

## Вердикт (signal-problem: `dossier_status`)

| Код | Фраза |
|---|---|
| DECISION_READY_DOSSIER | Достаточно, можно принимать решение |
| NOT_READY | Недостаточно: {N} препятствий |
| BLOCKED | Проверка не началась: {причина словами} |

Solution уже пишет «достаточно для D3/D4» и «не достаточно»; рендерить теми же фразами, что выше.

## Рекомендация (signal-problem: `canonical_transition_candidate`, `decision_outcome`, `d5_mode`)

| Код | Фраза |
|---|---|
| D2_CANDIDATE / OPEN_SOLUTION_DISCOVERY | документ тянет на признание проблемы и поиск решений |
| CONTINUE_CANDIDATE / CONTINUE_PROBLEM_DISCOVERY | продолжать исследование проблемы |
| D5_STOP_CANDIDATE / STOP | остановить |
| D5_PARK_CANDIDATE / PARK | заморозить |
| TAKE_SIGNAL_INTO_DISCOVERY | взять сигнал в работу |
| NO_CANDIDATE / NOT_DECIDED | рекомендации нет, решение не принято |
| candidate_available | (не показывать; следует из фразы выше) |

## Вид препятствия (`kind`)

| Код | Фраза |
|---|---|
| BLOCKS_ASSESSMENT | мешает начать проверку |
| BLOCKS_DOSSIER | мешает принять решение |
| CHANGES_CANDIDATE | меняет рекомендацию |
| NO_CURRENT_EFFECT | сейчас на вывод не влияет |

## Причина (`primary_reason`, signal-problem)

| Код | Фраза «что не так» |
|---|---|
| INVALID_INPUT | не хватает входных данных для проверки |
| TRACK_NOT_SUPPORTED | такой тип инициативы пока не проверяем |
| ABSENT | в документе этого нет |
| INVALID_FORM | есть, но не в проверяемом виде |
| TRANSITION_COMMITMENT_MISMATCH | следующий шаг больше заявленного решения |
| CENTRAL_CLAIM_UNRESOLVED | не названа главная гипотеза |
| SOURCE_REF_MISSING | нет ссылки на источник |
| BLOCKED_SOURCE | источник не открывается |
| SOURCE_OBSERVATION_ABSENT | в источнике нет этого наблюдения |
| SOURCE_SCOPE_MISMATCH | источник про другую границу |
| SOURCE_PERIOD_MISMATCH | источник за другой период |
| SOURCE_GRAIN_MISMATCH | источник в другой детализации |
| SOURCE_VALUE_MISMATCH | в источнике другое значение |
| CLAIM_TYPE_AMBIGUOUS | непонятно, факт это, оценка или предположение |
| CLAIM_TYPE_UNSUPPORTED | такой тип утверждения проверить нельзя |
| METHOD_UNSPECIFIED | не назван метод проверки |
| METHOD_NOT_ADMISSIBLE | метод не подходит для такого утверждения |
| METHOD_PROFILE_INCOMPLETE | метод описан не полностью |
| DISCRIMINATION_RULE_MISSING | не сказано, какой результат опроверг бы утверждение |
| DISCRIMINATION_RULE_NON_OBSERVABLE | условие опровержения нельзя наблюдать |
| SELECTION_UNIVERSE_MISSING | не сказано, из чего выбирали |
| SELECTION_RULE_MISSING | не сказано, как выбирали |
| SCOPE_MISMATCH | границы утверждения и данных не совпадают |
| UNSUPPORTED_GENERALIZATION | вывод шире, чем наблюдения |
| CONCLUSION_EVIDENCE_MISMATCH | вывод расходится с данными |
| ESSENTIAL_RELATION_MISSING | проблема не связана с охватом и вредом |
| ESSENTIAL_RELATION_NOT_EVIDENCED | связь заявлена, но не подтверждена |
| RIVAL_MODEL_MISSING | не рассмотрено другое объяснение |
| RIVAL_PREDICTION_MISSING | не сказано, чем другое объяснение отличалось бы в данных |
| RIVAL_TEST_MISSING | другое объяснение не проверено |
| RIVAL_RESULT_MISSING | результат проверки другого объяснения не записан |
| RIVAL_STATUS_MISSING | статус другого объяснения не записан |
| UNCERTAINTY_DECISION_MAPPING_MISSING | не сказано, что решаем при каждом исходе неизвестного |
| UNCERTAINTY_NEXT_TEST_MISSING | не назван следующий тест |
| EVIDENCE_DATE_MISSING | у данных нет даты |
| EVIDENCE_STALE | данные устарели |
| EVIDENCE_PRECEDES_MATERIAL_CHANGE | данные собраны до существенного изменения |
| PROXY_TARGET_BRIDGE_MISSING | прокси-метрика не связана с целевой |
| PROXY_OVERCLAIM | вывод о целевой метрике сделан по прокси |
| CIRCULAR_EVIDENCE | доказательство опирается само на себя |
| INDEPENDENT_VALIDATION_MISSING | нет независимой проверки |
| CONFLICT_DISPOSITION_MISSING | противоречие источников не разрешено |
| CONCLUSION_CONFLICT_MISMATCH | вывод не учитывает противоречие |

Solution уже использует русские причины (Отсутствует, Не по форме, Противоречие и далее по `reason-action-map.md`); они остаются, но в «Что не так» пишется фраза про содержание, а не имя причины.

## Действие (`action`, signal-problem)

| Код | Фраза «что сделать» |
|---|---|
| PROVIDE_EVIDENCE | приложить источник с наблюдением: {что именно} |
| PROVIDE_METHOD | описать метод проверки и фактический результат |
| PROVIDE_BOUNDARY | указать границу: кого, где, за какой период |
| PROVIDE_REQUIRED_INPUT | добавить недостающий факт: {что именно} |
| ALIGN_CONCLUSION | привести вывод в соответствие с данными |
| NARROW_CLAIM | сузить утверждение до того, что подтверждено |
| WITHDRAW_CLAIM | снять утверждение |
| LOWER_TRANSITION | понизить заявленное решение до {переход словами} |

Solution берёт действие дословно из своей `reason-action-map.md`, как сейчас.

## Границы (`source_coverage.status`, `review_state`, `scope_state`)

| Код | Фраза |
|---|---|
| COMPLETE | прочитано всё обязательное |
| INCOMPLETE | часть обязательного не прочитана |
| NOT_ASSESSABLE | границы оценить нельзя |
| READ / NOT_READ / UNAVAILABLE | прочитано / не прочитано / недоступно |
| IN_SCOPE / OUT_OF_SCOPE | (не показывать; попадает в списки «прочитано» и «не прочитано») |

## Опровержение (`falsification.status`)

| Код | Фраза |
|---|---|
| NO_FINDING | В документе: есть, вывод устоял |
| FINDING_RAISED | В документе: нет, наблюдение против вывода |
| CANNOT_ASSESS | В документе: проверить нельзя |

## Статусы утверждений (`problem_status`, `essential_claims`)

Не показывать в человеческом слое. Если нужны в «Почему», использовать: SUPPORTS → «подтверждает», REFUTES → «опровергает», MIXED → «противоречиво», DOES_NOT_BEAR → «не относится к делу», UNKNOWN → «неизвестно».

## Критерии

ID критерия (`DB-04`, `S-01`, `D4.1` и подобные) в человеческом слое не показывать. Вместо него берётся описание из каталога критериев и переписывается как «что не так» (пример: `S-02` → «не назван канал или артефакт, откуда пришёл сигнал»).

## Служебные поля

`rubric_version`, `model_version`, `thread_id`, `claim_inventory`, `below_attention`, `limitation_id`, `issue_id`, `applicability_rule_id`, `target_ids`, `omitted_count` в человеческом слое не показываются; `omitted_count` рендерится фразой «ещё {m} в машинном слое».
