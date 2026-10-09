# Writing examples: structure, stories, processes and invariants

These Russian excerpts teach the form of a PRD block. They are fictional, not Avito product contracts. Copy the reasoning and layout, not the actors, policies, IDs or priorities. The negative examples deliberately show defects. Use the PM's accepted format and language profile when working on a real document.

## Shared teaching brief

For this example only, assume the PM has selected:

- Two stages: preparation and receipt of the result. The processes are file validation, report creation and report download.
- An operator validates a file and creates a report to find errors before handing the result to an analyst. The analyst downloads the selected report to share its result with colleagues.
- A valid file can be used to create a report. An invalid file cannot; the operator sees the row number and error description.
- A successfully created report contains its creation date and the selected file's row count. A downloaded file contains the selected completed report. D-01–D-04 have priority 1.
- Report-creation failure behavior and report retention are open. No delivery deadline, architecture or other product result has been selected.

## 1. Structure

### Good: one connected fragment

The stages, stories and processes below come from the brief. Each process has its own nearby invariant table. This is a block example, not a replacement for every section of a full PRD.

```markdown
## Этап 1. Подготовка отчёта

Оператор хочет проверить файл и создать отчёт, чтобы найти ошибки до передачи результата аналитику.

### БП 1. Проверка файла

Начало: оператор выбрал файл для проверки.

1. Оператор загружает выбранный файл.
2. Система показывает результат проверки.

- Если ошибок нет, файл доступен для создания отчёта. Оператор может перейти к БП 2.
- Если найдены ошибки, оператор видит номер строки и описание ошибки. Такой файл недоступен для создания отчёта.

| ID | Критерий приёмки | Приоритет |
| --- | --- | --- |
| D-01 | Если файл проходит проверку, он доступен для создания отчёта. | 1 |
| D-02 | Если проверка находит ошибку, оператор видит номер строки и описание ошибки. Такой файл недоступен для создания отчёта. | 1 |

### БП 2. Создание отчёта

Начало: выбранный файл прошёл проверку.

1. Оператор запрашивает отчёт по выбранному файлу.

Если отчёт создан, он содержит дату создания и число строк в выбранном файле.

| ID | Критерий приёмки | Приоритет |
| --- | --- | --- |
| D-03 | Если отчёт создан, он содержит дату создания и число строк в выбранном файле. | 1 |

Открытый вопрос: что получает оператор, если отчёт не удалось создать?

## Этап 2. Получение результата

Аналитик хочет скачать выбранный отчёт, чтобы поделиться результатом с коллегами.

### БП 3. Скачивание отчёта

Начало: доступен готовый отчёт.

1. Аналитик выбирает готовый отчёт.
2. Аналитик скачивает выбранный отчёт.

| ID | Критерий приёмки | Приоритет |
| --- | --- | --- |
| D-04 | Скачанный файл содержит выбранный готовый отчёт. | 1 |

Открытый вопрос: как долго хранить отчёты?
```

The failure question limits acceptance of that branch; the fragment does not promise a successful report for every request. Priority 1 is selected in this brief. It is not a default for other PRDs. Conditions remain mandatory whenever the associated function is implemented.

### Bad for this requested block: disconnected collections

```markdown
## Все пользовательские истории
История оператора. История аналитика.

## Все процессы
Проверка файла. Создание отчёта. Скачивание отчёта.

## Все требования
Общая таблица D-01–D-04.
```

The selected stage order and process/table pairs disappear. The reader must reconstruct the associations. This is not a universal ban on a flat table: preserve one if the PM chose it or a scoped edit does not authorize restructuring.

## 2. User story

### Good: an actor, a selected goal and its value

> Аналитик хочет скачать выбранный отчёт, чтобы поделиться результатом с коллегами.

This is one paragraph, not a requirement table or an implementation task. It explains the selected goal without specifying a button, API or delivery method. The value comes from the brief.

### Bad

> Как пользователь, я хочу удобный отчёт, чтобы эффективно работать.

The reader cannot name the actor's action or what becomes possible. “Convenient” and “effective” supply no selected result.

> Аналитик хочет скачать отчёт, чтобы повысить доход компании.

The action is clear, but the brief does not support this motive. A well-formed template can still invent intent. Do not add roles or motives merely to fill actor/goal/value fields.

## 3. Business process and its formatting

### Good

Use the format of BP 1 above: a named process, initial state, numbered observable actions, explicit validation branches and the adjacent invariant table. Keep one action per numbered step. Describe process behavior; do not command the developer to implement it.

The failed-validation branch ends without report creation. The successful branch names the next available process. The table contains the pass/fail conditions; the flow explains their order and connection.

### Bad

```markdown
### Проверка и отчёт

- Сделать загрузку, проверку и удобную обработку ошибок.
- Файл обрабатывается, затем формируется результат и предоставляется пользователю.
- Пользователь получает отчёт.
```

The bullets mix a development task with an unspecified process. They do not identify the affected actors, branch on failed validation or explain whether an invalid file can produce a report. The final sentence promises a report despite the open creation-failure branch.

Numbering alone does not repair this. First recover the selected actions, conditions, branches and outcome. Then format them in their actual order. Do not invent a failure policy to complete the flow.

## 4. Invariant: obligation and acceptance in one expression

### Good

| ID | Критерий приёмки | Приоритет |
| --- | --- | --- |
| D-02 | Если проверка находит ошибку, оператор видит номер строки и описание ошибки. Такой файл недоступен для создания отчёта. | 1 |

The condition, visible error details and prohibition are selected together. A reader can distinguish a pass from a failure without choosing the target result. Keep the accepted bundle in one row; two independently testable effects do not automatically require two IDs. The wording leaves the implementation open.

For example, an error message without a row number fails D-02. So does allowing report creation from the invalid file. These checks illustrate the acceptance boundary; they are not extra PRD fields to copy.

### Bad

| Text | Why it fails this brief |
| --- | --- |
| Ошибки обрабатываются корректно. | It does not define the selected visible result or prohibition. |
| Если файл не прошёл проверку, оператор видит ошибку. | It omits the selected row number, description and ban on report creation. |
| Любой загруженный файл доступен для создания отчёта. | It contradicts the agreed failed-validation exception. |
| Проверка реализована отдельным сервисом, который отвечает за 10 секунд. | It adds an unchosen architecture and deadline instead of the selected result. |

Do not duplicate the same meaning in “Requirement” and “Acceptance” columns. Use ID plus the combined criterion; add a selected or requested priority. An unknown value remains open, even if filling it would make the sentence easier to test.

### Selected research uses the same acceptance logic

Additional fictional brief: the PM selected an investigation of an agreed case list. Its deliverable is a report with the evidence checked for each case. The report must state the cause or explicitly record that it remains unknown. No fix or new event has been selected.

**Good:**

| ID | Критерий приёмки |
| --- | --- |
| R-01 | Для каждого случая из согласованного списка в отчёте приведены проверенные данные и причина отсутствия события. Неизвестная причина отмечена явно. |

**Bad:** «Разобраться с событиями». It identifies work to do but no agreed deliverable or question answered. «Случаев без события больше нет» would invent a product promise for this research brief. If the PM later selects that product result, describe and accept it as selected work instead.

## Use the examples in review

Ask whether the intended reader can name the selected change and its acceptance without choosing the target result. Luna checks the wording and structure under criteria 1/3/4. Astra checks source support and acceptance under 2/5. A clearly worded sentence can still invent a choice; a review suggestion is not a PM decision.
