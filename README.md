<h1 align="center">A Modular Large Language Model Agent Architecture<br>for Adaptive and Autonomous Process-Aware Execution</h1>

<p align="center"><strong>Online Appendix</strong></p>

---

# Online Appendix

## 1. Additional Results

### 1.1 Aggregate Results

The following tables present aggregate results across two GPT models with two reasoning levels each (GPT-5.1 and GPT-5.4 with reasoning `none` and reasoning `high`) and Qwen 3.5:35b (reasoning `high` only), evaluated against three rule adaptation methods (Modular Agents Add Rule, Modular Agents BPMN Rule, Classic Agent Prompt). Process adaptations are grouped by capability layer (operational, tactical) and exception experiments (typing errors and database errors) are aggregated across all adaptations.

**Table A1: Average Time (s) per Process Adaptation**

| Model | Reasoning | Modality | Base Rule | Area 0 | Area 500 | Area 900 | Excl. Cities | Mand. Reading | Dir. Mail | Typing Err. | DB Err. | Avg. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-5.4 | none | Modular Agents Add Rule | 34.6 | 36.4 | 40.9 | 38.5 | 39.5 | 110.6 | 167.9 | 47.3 | 14.4 | 58.9 |
| GPT-5.4 | none | Modular Agents BPMN Rule | 40.7 | 45.4 | 53.9 | 51.8 | 52.6 | 78.6 | 120.3 | 66.8 | 22.3 | 59.2 |
| GPT-5.4 | none | Classic Agent Prompt | 33.3 | 33.1 | 32.3 | 31.7 | 34.6 | 91.7 | 100.9 | 39.2 | 5.9 | 44.7 |
| GPT-5.4 | high | Modular Agents Add Rule | 41.2 | 42.5 | 47.3 | 45.8 | 46.7 | 131.4 | 114.4 | 58.1 | 22.2 | 61.1 |
| GPT-5.4 | high | Modular Agents BPMN Rule | 65.3 | 43.3 | 50.2 | 44.8 | 48.8 | 89.1 | 161.6 | 96.9 | 27.6 | 69.7 |
| GPT-5.4 | high | Classic Agent Prompt | 36.0 | 35.3 | 34.6 | 32.1 | 31.5 | 85.9 | 102.0 | 43.1 | 5.5 | 45.1 |
| GPT-5.1 | none | Modular Agents Add Rule | 40.3 | 41.6 | 50.6 | 54.3 | 52.6 | 104.9 | 88.5 | 56.4 | 17.0 | 56.2 |
| GPT-5.1 | none | Modular Agents BPMN Rule | 65.5 | 65.3 | 68.8 | 72.2 | 79.1 | 103.9 | 123.0 | 87.8 | 23.5 | 76.6 |
| GPT-5.1 | none | Classic Agent Prompt | 35.2 | 32.4 | 31.9 | 28.0 | 30.2 | 51.4 | 81.2 | 35.6 | 8.5 | 37.2 |
| GPT-5.1 | high | Modular Agents Add Rule | 161.1 | 178.0 | 117.4 | 131.9 | 178.0 | 201.9 | 313.4 | 177.3 | 54.1 | 168.1 |
| GPT-5.1 | high | Modular Agents BPMN Rule | 218.1 | 188.5 | 187.5 | 157.6 | 157.1 | 240.6 | 375.6 | 225.3 | 101.3 | 205.7 |
| GPT-5.1 | high | Classic Agent Prompt | 107.7 | 129.0 | 105.3 | 222.6 | 190.2 | 217.1 | 301.6 | 185.2 | 42.9 | 166.8 |
| Qwen3.5:35B | high | Modular Agents Add Rule | 107.8 | 126.5 | 115.2 | 186.7 | 114.3 | 138.0 | 119.9 | 132.8 | 49.3 | 121.2 |
| Qwen3.5:35B | high | Modular Agents BPMN Rule | 502.4 | 270.4 | 265.8 | 279.3 | 297.3 | 453.7 | 366.7 | 300.1 | 198.9 | 326.1 |
| Qwen3.5:35B | high | Classic Agent Prompt | 45.3 | 46.8 | 53.0 | 46.7 | 55.3 | 30.1 | 101.2 | 48.6 | 10.1 | 48.6 |

**Table A2: Average Steps (AI Messages) per Process Adaptation**

| Model | Reasoning | Modality | Base Rule | Area 0 | Area 500 | Area 900 | Excl. Cities | Mand. Reading | Dir. Mail | Typing Err. | DB Err. | Avg. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-5.4 | none | Modular Agents Add Rule | 15.0 | 15.4 | 16.2 | 15.6 | 15.8 | 18.9 | 22.4 | 15.8 | 8.8 | 16.0 |
| GPT-5.4 | none | Modular Agents BPMN Rule | 14.7 | 15.1 | 16.5 | 15.9 | 16.2 | 19.0 | 21.4 | 15.9 | 8.4 | 15.9 |
| GPT-5.4 | none | Classic Agent Prompt | 10.1 | 10.0 | 9.6 | 10.0 | 10.1 | 14.6 | 16.4 | 10.5 | 3.0 | 10.5 |
| GPT-5.4 | high | Modular Agents Add Rule | 15.0 | 15.2 | 16.2 | 15.6 | 15.6 | 20.4 | 20.1 | 16.4 | 8.3 | 15.9 |
| GPT-5.4 | high | Modular Agents BPMN Rule | 14.8 | 15.2 | 16.2 | 15.4 | 15.9 | 18.2 | 21.7 | 15.6 | 8.5 | 15.7 |
| GPT-5.4 | high | Classic Agent Prompt | 10.0 | 10.1 | 9.8 | 10.0 | 9.9 | 13.6 | 15.9 | 10.5 | 3.0 | 10.3 |
| GPT-5.1 | none | Modular Agents Add Rule | 15.4 | 16.4 | 17.8 | 19.2 | 19.2 | 25.6 | 25.8 | 19.6 | 8.0 | 18.6 |
| GPT-5.1 | none | Modular Agents BPMN Rule | 21.0 | 20.4 | 22.4 | 23.0 | 23.5 | 29.0 | 29.6 | 24.5 | 8.7 | 22.5 |
| GPT-5.1 | none | Classic Agent Prompt | 11.6 | 11.4 | 9.8 | 8.2 | 10.0 | 16.2 | 17.2 | 11.2 | 3.0 | 11.0 |
| GPT-5.1 | high | Modular Agents Add Rule | 18.0 | 20.0 | 18.8 | 21.6 | 20.0 | 25.6 | 30.2 | 21.5 | 8.8 | 20.5 |
| GPT-5.1 | high | Modular Agents BPMN Rule | 22.0 | 21.6 | 23.4 | 22.4 | 22.2 | 28.5 | 35.9 | 24.8 | 9.6 | 23.4 |
| GPT-5.1 | high | Classic Agent Prompt | 11.8 | 13.2 | 12.4 | 15.2 | 16.0 | 17.8 | 22.0 | 14.2 | 4.1 | 14.1 |
| Qwen3.5:35B | high | Modular Agents Add Rule | 18.8 | 22.2 | 21.6 | 29.5 | 22.0 | 24.1 | 21.8 | 24.3 | 12.5 | 21.9 |
| Qwen3.5:35B | high | Modular Agents BPMN Rule | 29.5 | 19.0 | 20.2 | 20.5 | 23.2 | 38.0 | 26.6 | 23.8 | 10.6 | 23.5 |
| Qwen3.5:35B | high | Classic Agent Prompt | 10.8 | 10.0 | 11.8 | 11.0 | 13.2 | 7.5 | 23.8 | 11.8 | 5.2 | 11.7 |

**Table A3: Ablation experiment with GPT-5.4 (Summary across Models, Reasoning Levels, and Modalities)**

The summary table aggregates the per-adaptation completion rate, average wall-clock time, and average step count (AI messages) per session. Reasoning ablation pairs (`none` vs. `high`) isolate the effect of the model's reasoning effort while keeping every other configuration constant; the GPT-5.4 reasoning ablation is the headline comparison and is reported alongside the equivalent GPT-5.1 pair and the Qwen3.5:35B baseline for context.

| Model | Reasoning | Modality | Completion (%) | Avg Time (s) | Avg Steps |
|---|---|---|---|---|---|
| GPT-5.4 | none | Modular Agents Add Rule | 91.6 | 57.4 +/- 73.3 | 15.8 +/- 4.5 |
| GPT-5.4 | none | Modular Agents BPMN Rule | 92.6 | 58.4 +/- 64.8 | 15.7 +/- 3.9 |
| GPT-5.4 | none | Classic Agent Prompt | 86.3 | 43.6 +/- 37.8 | 10.3 +/- 4.4 |
| GPT-5.4 | high | Modular Agents Add Rule | 92.6 | 60.0 +/- 52.5 | 15.7 +/- 4.0 |
| GPT-5.4 | high | Modular Agents BPMN Rule | 91.1 | 69.4 +/- 85.5 | 15.5 +/- 4.0 |
| GPT-5.4 | high | Classic Agent Prompt | 87.9 | 44.0 +/- 39.6 | 10.1 +/- 4.3 |
| GPT-5.1 | none | Modular Agents Add Rule | 83.7 | 55.2 +/- 52.6 | 18.3 +/- 6.2 |
| GPT-5.1 | none | Modular Agents BPMN Rule | 78.4 | 75.5 +/- 43.4 | 22.1 +/- 7.4 |
| GPT-5.1 | none | Classic Agent Prompt | 73.7 | 36.4 +/- 32.0 | 10.8 +/- 5.8 |
| GPT-5.1 | high | Modular Agents Add Rule | 81.6 | 165.4 +/- 128.4 | 20.2 +/- 7.2 |
| GPT-5.1 | high | Modular Agents BPMN Rule | 86.3 | 203.5 +/- 118.7 | 23.0 +/- 8.3 |
| GPT-5.1 | high | Classic Agent Prompt | 86.3 | 164.1 +/- 199.5 | 13.8 +/- 7.6 |
| Qwen3.5:35B | high | Modular Agents Add Rule | 48.4 | 119.6 +/- 66.2 | 21.7 +/- 8.2 |
| Qwen3.5:35B | high | Modular Agents BPMN Rule | 33.7 | 322.0 +/- 159.4 | 23.2 +/- 10.6 |
| Qwen3.5:35B | high | Classic Agent Prompt | 43.7 | 47.6 +/- 33.6 | 11.5 +/- 7.2 |

### 1.2 Example Agent Conversation Log

The following is a complete agent conversation log from session `processadaptation_base_rule_processadaptationmethod_generate_bpmn_tour_J09A_seed_42` (GPT-5.1, BPMN Rule Generation method). This example demonstrates the full pipeline: BPMN-to-rule conversion by the Frame Agent, delegation to the Process Agent, and autonomous SQL-based process execution.

#### Frame Agent -- Process Rule Addition

The Frame Agent receives an instruction to generate a process rule from a BPMN file. It calls `generate_process_rule_from_bpmn` which reads the BPMN XML and uses an LLM to convert it into sequential process steps. The generated rule is then stored in the database via `add_process_rule`.

```
================================ Human Message =================================

Use the generate_process_rule_from_bpmn tool to generate a process rule from the
following BPMN file: bpmn/J09A_base_rule.bpmn and store it in the database as J09A

================================== Ai Message ==================================
Tool Calls:
  generate_process_rule_from_bpmn (call_CGNtQMdPWXWhYQcnszOPfnv7)
    Args:
      bpmn_path: bpmn/J09A_base_rule.bpmn
      process_rule_id: J09A

================================= Tool Message =================================
Name: generate_process_rule_from_bpmn

{"success":true,"process_rule_id":"J09A","process_rule":"1. Copy all rows from the
decision table into a temporary table `J09A_temp`, including only rows where the tour
starts with `J09A`.\n\n2. In `J09A_temp`, add a new column named `ENTSCHEIDUNG`.
\n\n3. In `J09A_temp`, classify the meter reading type: for each `HAUS`, count its
associated `EQUNR`; if a `HAUS` has less than 3 `EQUNR`, set `ENTSCHEIDUNG` = `KSA`
for all its rows, else set `ENTSCHEIDUNG` = `EVU` for all its rows.\n\n4. Join
`J09A_temp` with table `EABLG` using `INSTALLATION` as the join key...\n\n...
10. After successfully sending the email, delete the temporary table `J09A_temp`."}

================================== Ai Message ==================================
Tool Calls:
  add_process_rule (call_OTgDuZKNDqthL0Fowazfaes3)
    Args:
      process_rule_id: J09A
      process_rule: <10-step generated rule stored in database>

================================= Tool Message =================================
Name: add_process_rule

{"success":true,"process_rule_id":"J09A","message":"Process rule added successfully"}

================================== Ai Message ==================================

The process rule has been generated from bpmn/J09A_base_rule.bpmn and stored in the
database under the ID J09A.
```

#### Frame Agent -- Process Execution

The Frame Agent delegates execution to the Process Agent via `call_process_agent`.

```
================================ Human Message =================================

Run process_rule with process_rule_id 'J09A'.

================================== Ai Message ==================================
Tool Calls:
  call_process_agent (call_xg2ZauI6Jr8F2LTRidLqVsYb)
    Args:
      query: Run process with process_rule_id 'J09A'.

================================= Tool Message =================================
Name: call_process_agent

{"success":true,"response":"The process with process_rule_id = 'J09A' has been
executed completely:\n\n- Filtered decision_table to TOUR starting with J09A into
J09A_temp.\n- Classified each HAUS into ENTSCHEIDUNG = 'KSA' or 'EVU'.\n- Joined
with EABLG, NET_MASTER, SALES_MASTER.\n- Exported J09A.csv with 20,866 rows.\n-
Sent email to meter.readings@evu.com.\n- Dropped temporary table J09A_temp."}
```

#### Process Agent -- Autonomous Execution

The Process Agent retrieves the stored rule, inspects the database schema, then autonomously executes all steps through a sequence of SQL queries and tool calls. Below is a condensed view of its key actions:

```
================================ Human Message =================================

Run process with process_rule_id 'J09A'.

================================== Ai Message ==================================
Tool Calls:
  retrieve_process (call_8AZJm7bV2yNjelh13YE8ilzm)
    Args: { process_rule_id: J09A }

  -- Agent retrieves the 10-step process rule from the database --

================================== Ai Message ==================================
Tool Calls:
  -- Parallel schema inspection --
  run_sqlite_query: PRAGMA table_info('decision_table');
  run_sqlite_query: PRAGMA table_info('EABLG');
  run_sqlite_query: PRAGMA table_info('NET_MASTER');
  run_sqlite_query: PRAGMA table_info('SALES_MASTER');
  get_db_schema: {}

================================== Ai Message ==================================
  -- Step 1: Create filtered temporary table --
  run_sqlite_query: CREATE TABLE J09A_temp AS
    SELECT d.*, NULL AS ENTSCHEIDUNG FROM decision_table d
    WHERE d.TOUR LIKE 'J09A%';

  -- Step 3: Classify ENTSCHEIDUNG --
  run_sqlite_query: UPDATE J09A_temp SET ENTSCHEIDUNG = (
    SELECT CASE WHEN COUNT(DISTINCT d2.EQUNR) < 3 THEN 'KSA' ELSE 'EVU' END
    FROM J09A_temp d2 WHERE d2.HAUS = J09A_temp.HAUS);
  -- Result: 4,900 rows affected --

  -- Step 4: JOIN with EABLG --
  run_sqlite_query: CREATE TABLE J09A_temp2 AS
    SELECT t.*, e.[Meter Reading (MR) Doc. No.]
    FROM J09A_temp t LEFT JOIN eablg e ON t.ANLAGE = e.Installation;

  -- Step 5: JOIN with NET_MASTER and SALES_MASTER --
  run_sqlite_query: CREATE TABLE J09A_temp2 AS
    SELECT j.*, n.TITLE AS NET_TITLE, ..., s.TITLE AS SALES_TITLE, ...
    FROM J09A_temp j
    LEFT JOIN net_master n ON j.EQUNR = n.EQUNR
    LEFT JOIN sales_master s ON j.EQUNR = s.EQUNR;

  -- Step 6-7: Determine and apply customer data source --
  run_sqlite_query: SELECT COUNT(*) AS sales_nonempty FROM J09A_temp
    WHERE SALES_TITLE IS NOT NULL OR ...;  -- Result: 18,589 --
  run_sqlite_query: UPDATE J09A_temp SET
    TITLE = COALESCE(SALES_TITLE, NET_TITLE), ...;
  -- Result: 20,866 rows affected --

  -- Step 8: Export CSV --
  prepare_csv: SELECT [...16 columns...] FROM J09A_temp;
  -- Result: 20,866 rows exported to J09A.csv --

  -- Step 9: Send email --
  send_mail: { file_path: .../J09A.csv, email_address: meter.readings@evu.com }

  -- Step 10: Cleanup --
  run_sqlite_query: DROP TABLE IF EXISTS J09A_temp;

================================== Ai Message ==================================

The process with process_rule_id = 'J09A' has been executed completely.
```

The full, unabridged agent logs for all sessions are available in the `sessions/` directory.

---

## 2. Processes and Process Rules

This section presents all seven process adaptations with their corresponding BPMN diagrams and process rule prompts. The BPMN diagrams are structurally identical across tours (J09A, J09B, J09C, J09D) -- only the tour identifier changes. The examples below use tour **J09A**; all other tours follow the same pattern.

### 2.1 Base Rule

![Base Rule BPMN](bpmn/images/J09A_base_rule.png)

#### Process Prompt (Classic Agent)

```
I need you to process the meter readings for tour J09A. Take all entries from the
decision_table where the TOUR starts with "J09A" and put them into a temporary table
called J09A_temp. Then add a new column called ENTSCHEIDUNG to that table.

For classifying each house: count how many equipment numbers (EQUNR) belong to each
house (HAUS). If a house has fewer than 3 equipment numbers, set its ENTSCHEIDUNG to
"KSA". Otherwise, set it to "EVU".

Next, enrich the data by joining it with the EABLG table using the INSTALLATION field,
and also pull in customer contact details from both the net_master and sales_master
tables using the EQUNR field. When both net and sales data exist for a customer, prefer
the sales data and leave the net data fields empty. If only net data exists, keep that.

Export the final result as a CSV file named "J09A" with these columns: `Meter Reading
(MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`,
`TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`,
`EMAIL`.

Send the CSV to the EVU team at meter.readings@evu.com. After that, delete the
temporary table.
```

#### Process Rule Generation from BPMN

The BPMN diagram XML is provided as input together with the following prompt:

```
You are an assistant that converts business process models defined with the business
process model notation in XML into process steps an LLM agent will automatically run
to complete the process.

Convert the BPMN XML into unambiguous and pragmatic steps that include important step
information, decision rules, and the additional text annotations.

- The steps need to be designed as clear, unambiguous instructions for an LLM agent.
- Convert XOR statements to if-else statements based on the XOR gateway decision rules.
- Nest every step of an if path within the if statement and every else path step within
  an else statement.
- Linearize parallelization gateways into sequential steps.
- Include all additional text annotations from the BPMN XML in the respective step
  instruction.
- Only refer to the multi-agent system lane. Do not include steps from other lanes.
- Hold the formatting of the steps as simple as possible.
- Make this clear and precise steps. The need to be correctly in sequential order.
- Hold text short but include **all** necessary information.

Convert the following XML BPMN modeling according to the instructions above:

<BPMN XML content>
```

#### Process Rule Addition (Add Method)

```
1. Make a copy of decision_table with TOURS starting with J09A named J09A_temp
2. Update the table with an additional empty column ENTSCHEIDUNG
3. Apply the following rules to the joined table:
    1. Count the number of EQUNR for every HAUS and set ENTSCHEIDUNG to "KSA" if there
       are less than 3 EQUNR. ELSE set ENTSCHEIDUNG to "EVU"
4. JOIN this table with the EABLG table using INSTALLATION.
5. JOIN this table with the NET_MASTER table and the SALES_MASTER table using EQUNR.
6. Compare sales data and net data for these IDs:
    If sales data is there, take sales data and empty net data.
    Otherwise stay with net data and empty sales data.
7. Export the final data from the table as CSV file named J09A including the columns:
   `Meter Reading (MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`,
   `ENTSCHEIDUNG`, `TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`,
   `CITY1`, `CITY2`, `EMAIL`
8. Send them to the EVU team to meter.readings@evu.com
9. Delete the temporary table after exporting the data.
```

---

### 2.2 Area 0 Values

![Area 0 Values BPMN](bpmn/images/J09A_0_values.png)

#### Process Prompt (Classic Agent)

```
I need you to process the meter readings for tour J09A. Take all entries from the
decision_table where the TOUR starts with "J09A" and put them into a temporary table
called J09A_temp. Then add a new column called ENTSCHEIDUNG to that table.

For classifying each house: count how many equipment numbers (EQUNR) belong to each
house (HAUS). If a house has fewer than 3 equipment numbers, set its ENTSCHEIDUNG to
"KSA". Otherwise, set it to "EVU". Additionally, any house where HOUSE_NUM1 is 0
should always be set to "EVU" regardless of the count.

Next, enrich the data by joining it with the EABLG table using the INSTALLATION field,
and also pull in customer contact details from both the net_master and sales_master
tables using the EQUNR field. When both net and sales data exist for a customer, prefer
the sales data and leave the net data fields empty. If only net data exists, keep that.

Export the final result as a CSV file named "J09A" with these columns: `Meter Reading
(MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`,
`TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`,
`EMAIL`.

Send the CSV to the EVU team at meter.readings@evu.com. After that, delete the
temporary table.
```

#### Process Rule Addition (Add Method)

```
1. Make a copy of decision_table with TOURS starting with J09A named J09A_temp
2. Update the table with an additional empty column ENTSCHEIDUNG
3. Apply the following rules to the joined table:
    1. Count the number of EQUNR for every HAUS and set ENTSCHEIDUNG to "KSA" if there
       are less than 3 EQUNR. ELSE set ENTSCHEIDUNG to "EVU"
    2. SET all houses with HOUSE_NUM1 of 0 to "EVU"
4. JOIN this table with the EABLG table using INSTALLATION.
5. JOIN this table with the NET_MASTER table and the SALES_MASTER table using EQUNR.
6. Compare sales data and net data for these IDs:
    If sales data is there, take sales data and empty net data.
    Otherwise stay with net data and empty sales data.
7. Export the final data from the table as CSV file named J09A including the columns:
   `Meter Reading (MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`,
   `ENTSCHEIDUNG`, `TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`,
   `CITY1`, `CITY2`, `EMAIL`
8. Send them to the EVU team to meter.readings@evu.com
9. Delete the temporary table after exporting the data.
```

---

### 2.3 Area 500 Values

![Area 500 Values BPMN](bpmn/images/J09A_500_values.png)

#### Process Prompt (Classic Agent)

```
I need you to process the meter readings for tour J09A. Take all entries from the
decision_table where the TOUR starts with "J09A" and put them into a temporary table
called J09A_temp. Then add a new column called ENTSCHEIDUNG to that table.

For classifying each house: count how many equipment numbers (EQUNR) belong to each
house (HAUS). If a house has fewer than 3 equipment numbers, set its ENTSCHEIDUNG to
"KSA". Otherwise, set it to "EVU". There are two additional overrides: any house where
HOUSE_NUM1 is 0 should be set to "EVU", and any house where HOUSE_NUM1 is in the range
500 to 599 should also be set to "EVU".

Next, enrich the data by joining it with the EABLG table using the INSTALLATION field,
and also pull in customer contact details from both the net_master and sales_master
tables using the EQUNR field. When both net and sales data exist for a customer, prefer
the sales data and leave the net data fields empty. If only net data exists, keep that.

Export the final result as a CSV file named "J09A" with these columns: `Meter Reading
(MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`,
`TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`,
`EMAIL`.

Send the CSV to the EVU team at meter.readings@evu.com. After that, delete the
temporary table.
```

#### Process Rule Addition (Add Method)

```
1. Make a copy of decision_table with TOURS starting with J09A named J09A_temp
2. Update the table with an additional empty column ENTSCHEIDUNG
3. Apply the following rules to the joined table:
    1. Count the number of EQUNR for every HAUS and set ENTSCHEIDUNG to "KSA" if there
       are less than 3 EQUNR. ELSE set ENTSCHEIDUNG to "EVU"
    2. SET all houses with HOUSE_NUM1 of 0 to "EVU"
    3. SET all houses with HOUSE_NUM1 500 - 599 to "EVU"
4. JOIN this table with the EABLG table using INSTALLATION.
5. JOIN this table with the NET_MASTER table and the SALES_MASTER table using EQUNR.
6. Compare sales data and net data for these IDs:
    If sales data is there, take sales data and empty net data.
    Otherwise stay with net data and empty sales data.
7. Export the final data from the table as CSV file named J09A including the columns:
   `Meter Reading (MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`,
   `ENTSCHEIDUNG`, `TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`,
   `CITY1`, `CITY2`, `EMAIL`
8. Send them to the EVU team to meter.readings@evu.com
9. Delete the temporary table after exporting the data.
```

---

### 2.4 Area 900 Values

![Area 900 Values BPMN](bpmn/images/J09A_900_values.png)

#### Process Prompt (Classic Agent)

```
I need you to process the meter readings for tour J09A. Take all entries from the
decision_table where the TOUR starts with "J09A" and put them into a temporary table
called J09A_temp. Then add a new column called ENTSCHEIDUNG to that table.

For classifying each house: count how many equipment numbers (EQUNR) belong to each
house (HAUS). If a house has fewer than 3 equipment numbers, set its ENTSCHEIDUNG to
"KSA". Otherwise, set it to "EVU". There are three additional overrides that always
result in "EVU": houses where HOUSE_NUM1 is 0, houses where HOUSE_NUM1 is between 500
and 599, and houses where HOUSE_NUM1 is between 900 and 999.

Next, enrich the data by joining it with the EABLG table using the INSTALLATION field,
and also pull in customer contact details from both the net_master and sales_master
tables using the EQUNR field. When both net and sales data exist for a customer, prefer
the sales data and leave the net data fields empty. If only net data exists, keep that.

Export the final result as a CSV file named "J09A" with these columns: `Meter Reading
(MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`,
`TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`,
`EMAIL`.

Send the CSV to the EVU team at meter.readings@evu.com. After that, delete the
temporary table.
```

#### Process Rule Addition (Add Method)

```
1. Make a copy of decision_table with TOURS starting with J09A named J09A_temp
2. Update the table with an additional empty column ENTSCHEIDUNG
3. Apply the following rules to the joined table:
    1. Count the number of EQUNR for every HAUS and set ENTSCHEIDUNG to "KSA" if there
       are less than 3 EQUNR. ELSE set ENTSCHEIDUNG to "EVU"
    2. SET all houses with HOUSE_NUM1 of 0 to "EVU"
    3. SET all houses with HOUSE_NUM1 500 - 599 to "EVU"
    4. SET all houses with HOUSE_NUM1 900 - 999 to "EVU"
4. JOIN this table with the EABLG table using INSTALLATION.
5. JOIN this table with the NET_MASTER table and the SALES_MASTER table using EQUNR.
6. Compare sales data and net data for these IDs:
    If sales data is there, take sales data and empty net data.
    Otherwise stay with net data and empty sales data.
7. Export the final data from the table as CSV file named J09A including the columns:
   `Meter Reading (MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`,
   `ENTSCHEIDUNG`, `TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`,
   `CITY1`, `CITY2`, `EMAIL`
8. Send them to the EVU team to meter.readings@evu.com
9. Delete the temporary table after exporting the data.
```

---

### 2.5 Excluding Cities

![Excluding Cities BPMN](bpmn/images/J09A_city_values.png)

#### Process Prompt (Classic Agent)

```
I need you to process the meter readings for tour J09A. Take all entries from the
decision_table where the TOUR starts with "J09A" and put them into a temporary table
called J09A_temp. Then add a new column called ENTSCHEIDUNG to that table.

For classifying each house: count how many equipment numbers (EQUNR) belong to each
house (HAUS). If a house has fewer than 3 equipment numbers, set its ENTSCHEIDUNG to
"KSA". Otherwise, set it to "EVU". There are four additional overrides that always
result in "EVU": houses where HOUSE_NUM1 is 0, houses where HOUSE_NUM1 is between 500
and 599, houses where HOUSE_NUM1 is between 900 and 999, and houses located in the
areas of Wiblingwerde or Breckerfeld.

Next, enrich the data by joining it with the EABLG table using the INSTALLATION field,
and also pull in customer contact details from both the net_master and sales_master
tables using the EQUNR field. When both net and sales data exist for a customer, prefer
the sales data and leave the net data fields empty. If only net data exists, keep that.

Export the final result as a CSV file named "J09A" with these columns: `Meter Reading
(MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`,
`TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`,
`EMAIL`.

Send the CSV to the EVU team at meter.readings@evu.com. After that, delete the
temporary table.
```

#### Process Rule Addition (Add Method)

```
1. Make a copy of decision_table with TOURS starting with J09A named J09A_temp
2. Update the table with an additional empty column ENTSCHEIDUNG
3. Apply the following rules to the joined table:
    1. Count the number of EQUNR for every HAUS and set ENTSCHEIDUNG to "KSA" if there
       are less than 3 EQUNR. ELSE set ENTSCHEIDUNG to "EVU"
    2. SET all houses with HOUSE_NUM1 of 0 to "EVU"
    3. SET all houses with HOUSE_NUM1 500 - 599 to "EVU"
    4. SET all houses with HOUSE_NUM1 900 - 999 to "EVU"
    5. SET all houses with address area Wiblingwerde or Breckerfeld to "EVU"
4. JOIN this table with the EABLG table using INSTALLATION.
5. JOIN this table with the NET_MASTER table and the SALES_MASTER table using EQUNR.
6. Compare sales data and net data for these IDs:
    If sales data is there, take sales data and empty net data.
    Otherwise stay with net data and empty sales data.
7. Export the final data from the table as CSV file named J09A including the columns:
   `Meter Reading (MR) Doc. No.`, `HAUS`, `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`,
   `ENTSCHEIDUNG`, `TITLE`, `FORENAME`, `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`,
   `CITY1`, `CITY2`, `EMAIL`
8. Send them to the EVU team to meter.readings@evu.com
9. Delete the temporary table after exporting the data.
```

---

### 2.6 Mandatory Reading Extension

![Mandatory Reading BPMN](bpmn/images/J09A_extension_estimates.png)

#### Process Prompt (Classic Agent)

```
I need you to process the meter readings for tour J09A. Take all entries from the
decision_table where the TOUR starts with "J09A" and put them into a temporary table
called J09A_temp. Then add a new column called ENTSCHEIDUNG to that table.

For classifying each house: count how many equipment numbers (EQUNR) belong to each
house (HAUS). If a house has fewer than 3 equipment numbers, set its ENTSCHEIDUNG to
"KSA". Otherwise, set it to "EVU". There are four additional overrides that always
result in "EVU": houses where HOUSE_NUM1 is 0, houses where HOUSE_NUM1 is between 500
and 599, houses where HOUSE_NUM1 is between 900 and 999, and houses located in the
areas of Wiblingwerde or Breckerfeld.

Next, enrich the data by joining it with the EABLG table using the INSTALLATION field,
and also pull in customer contact details from both the net_master and sales_master
tables using the EQUNR field. When both net and sales data exist for a customer, prefer
the sales data and leave the net data fields empty. If only net data exists, keep that.

There is one more classification to handle: check the EABL table for equipment numbers
that had "Maschinelle Schaetzung - SAP" as ISTABLART_TXT in both 2023 and 2024 (based
on Record created on). For those, set ENTSCHEIDUNG to "MANDATORY_READING".

Export the MANDATORY_READING entries separately as a CSV file named "J09A_MANDATORY_
READING" with these columns: `Meter Reading (MR) Doc. No.`, `HAUS`, `ANLAGE`,
`ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`, `TITLE`, `FORENAME`, `SURNAME`,
`STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`, `EMAIL`. Send that file to the
internal team at mandatory.reading@provider.com.

Then export all remaining entries (everything except MANDATORY_READING) as a CSV file
named "J09A" with the same columns. Send that to the EVU team at
meter.readings@evu.com. After that, delete the temporary table.
```

#### Process Rule Addition (Add Method)

```
1. Make a copy of decision_table with TOURS starting with J09A named J09A_temp
2. Update the table with an additional empty column ENTSCHEIDUNG
3. Apply the following rules to the joined table:
    1. Count the number of EQUNR for every HAUS and set ENTSCHEIDUNG to "KSA" if there
       are less than 3 EQUNR. ELSE set ENTSCHEIDUNG to "EVU"
    2. SET all houses with HOUSE_NUM1 of 0 to "EVU"
    3. SET all houses with HOUSE_NUM1 500 - 599 to "EVU"
    4. SET all houses with HOUSE_NUM1 900 - 999 to "EVU"
    5. SET all houses with address area Wiblingwerde or Breckerfeld to "EVU"
4. JOIN this table with the EABLG table using INSTALLATION.
5. JOIN this table with the NET_MASTER table and the SALES_MASTER table using EQUNR.
6. Compare sales data and net data for these IDs:
    If sales data is there, take sales data and empty net data.
    Otherwise stay with net data and empty sales data.
7. Set ENTSCHEIDUNG to "MANDATORY_READING", for every EQUNR in EABL where both
   ISTABLART_TXT = "Maschinelle Schaetzung - SAP" and the Record created on 2024 and
   ISTABLART_TXT = "Maschinelle Schaetzung - SAP" and the Record created on 2023.
8. Export all MANDATORY_READING entries from the final table as CSV file named
   J09A_MANDATORY_READING including the columns: `Meter Reading (MR) Doc. No.`, `HAUS`,
   `ANLAGE`, `ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`, `TITLE`, `FORENAME`,
   `SURNAME`, `STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`, `EMAIL`
9. Send them to the internal team to mandatory.reading@provider.com
10. Export the final data except MANDATORY_READING entries from the table as CSV file
    named J09A including the columns: [same 16 columns]
11. Send them to the EVU team to meter.readings@evu.com
12. Delete the temporary table after exporting the data.
```

---

### 2.7 Direct Mail Extension

![Direct Mail BPMN](bpmn/images/J09A_extension_mail.png)

#### Process Prompt (Classic Agent)

```
I need you to process the meter readings for tour J09A. Take all entries from the
decision_table where the TOUR starts with "J09A" and put them into a temporary table
called J09A_temp. Then add a new column called ENTSCHEIDUNG to that table.

For classifying each house: count how many equipment numbers (EQUNR) belong to each
house (HAUS). If a house has fewer than 3 equipment numbers, set its ENTSCHEIDUNG to
"KSA". Otherwise, set it to "EVU". There are four additional overrides that always
result in "EVU": houses where HOUSE_NUM1 is 0, houses where HOUSE_NUM1 is between 500
and 599, houses where HOUSE_NUM1 is between 900 and 999, and houses located in the
areas of Wiblingwerde or Breckerfeld.

Next, enrich the data by joining it with the EABLG table using the INSTALLATION field,
and also pull in customer contact details from both the net_master and sales_master
tables using the EQUNR field. When both net and sales data exist for a customer, prefer
the sales data and leave the net data fields empty. If only net data exists, keep that.

There are two more classifications to handle. First, check the EABL table for equipment
numbers that had "Maschinelle Schaetzung - SAP" as ISTABLART_TXT in both 2023 and 2024
(based on Record created on). For those, set ENTSCHEIDUNG to "MANDATORY_READING".
Export them as a CSV file named "J09A_MANDATORY_READING" with the columns listed below
and send it to the internal team at mandatory.reading@provider.com.

Second, check the EABL table for equipment numbers that had "Ablesung durch Kunden -
SAP" as ISTABLART_TXT in both 2023 and 2024. For those, set ENTSCHEIDUNG to
"DIRECT_MAIL". Export them as a CSV file named "J09A_DIRECT_MAIL" with the columns
listed below and upload that file to the send_bulk_mail service so emails go out to all
those customers directly.

Finally, export all remaining entries (excluding MANDATORY_READING and DIRECT_MAIL) as
a CSV file named "J09A" with the same columns. Send that to the EVU team at
meter.readings@evu.com. After that, delete the temporary table.

The columns for all exports are: `Meter Reading (MR) Doc. No.`, `HAUS`, `ANLAGE`,
`ME_MA_ID`, `EQUNR`, `HOUSE_NUM1`, `ENTSCHEIDUNG`, `TITLE`, `FORENAME`, `SURNAME`,
`STREET`, `STREETNO`, `POST_CODE1`, `CITY1`, `CITY2`, `EMAIL`.
```

#### Process Rule Addition (Add Method)

```
1. Make a copy of decision_table with TOURS starting with J09A named J09A_temp
2. Update the table with an additional empty column ENTSCHEIDUNG
3. Apply the following rules to the joined table:
    1. Count the number of EQUNR for every HAUS and set ENTSCHEIDUNG to "KSA" if there
       are less than 3 EQUNR. ELSE set ENTSCHEIDUNG to "EVU"
    2. SET all houses with HOUSE_NUM1 of 0 to "EVU"
    3. SET all houses with HOUSE_NUM1 500 - 599 to "EVU"
    4. SET all houses with HOUSE_NUM1 900 - 999 to "EVU"
    5. SET all houses with address area Wiblingwerde or Breckerfeld to "EVU"
4. JOIN this table with the EABLG table using INSTALLATION.
5. JOIN this table with the NET_MASTER table and the SALES_MASTER table using EQUNR.
6. Compare sales data and net data for these IDs:
    If sales data is there, take sales data and empty net data.
    Otherwise stay with net data and empty sales data.
7. Set ENTSCHEIDUNG to "MANDATORY_READING", for every EQUNR in EABL where both
   ISTABLART_TXT = "Maschinelle Schaetzung - SAP" and the Record created on 2024 and
   ISTABLART_TXT = "Maschinelle Schaetzung - SAP" and the Record created on 2023.
8. Export all MANDATORY_READING entries from the final table as CSV file named
   J09A_MANDATORY_READING including the columns: [16 columns]
9. Send them to the internal team to mandatory.reading@provider.com
10. Set ENTSCHEIDUNG to "DIRECT_MAIL", for every EQUNR in EABL where
    ISTABLART_TXT = "Ablesung durch Kunden - SAP" in 2024 and
    ISTABLART_TXT = "Ablesung durch Kunden - SAP" in 2023.
11. Export all DIRECT_MAIL entries from the final table as CSV file named
    J09A_DIRECT_MAIL including the columns: [16 columns]
12. Upload the file to send_bulk_mail service for sending direct emails to all
    the customers.
13. Export the final data except MANDATORY_READING and DIRECT_MAIL entries from the
    table as CSV file named J09A including the columns: [16 columns]
14. Send them to the EVU team to meter.readings@evu.com
15. Delete the temporary table after exporting the data.
```

---

## 3. Updates

### 3.1 Unpacking Session Archives

The full agent conversation logs (~18 GB across 27,657 files) are stored as per-model `.tar.gz` archives in `sessions/` and tracked via Git LFS. After cloning the repository, fetch and extract them with:

```bash
# Pull the LFS-tracked tarballs (sessions/*.tar.gz)
git lfs pull

# Extract sessions/<model>.tar.gz back into sessions/<model>/ (parallelized across models)
python manage_sessions.py unpack
```

This restores the original `sessions/<model>/<reasoning>/<session>/` layout. The extracted subdirectories are listed in `.gitignore`, so they won't show up as changes.

A small set of representative sessions (one per model/reasoning combination) is also committed under `sessions_examples/` for quick inspection without needing to unpack the full archives.

For maintainers, repacking after adding new sessions:

```bash
python manage_sessions.py pack       # sessions/<model>/ -> sessions/<model>.tar.gz
python manage_sessions.py examples   # refresh sessions_examples/ from sessions/
```

---

# Repository Structure, Installation, and How to Run

## Repository Structure

```
├── config/                        # Experiment and model configuration
│   ├── experiment_config.py       # Run parameters (adaptations, tours, seeds, sampling)
│   ├── model_config.py            # LLM factory supporting OpenAI, Anthropic, Ollama
│   ├── server_config.py           # ExperimentType enum, prompt configs, tool behavior
│   └── process_adaptations.py     # TEXT_RULES, CLASSIC_RULES, and BPMN_RULES (all prompts)
├── servers/                       # Two-server MCP architecture
│   ├── process_server.py          # FastAPI + FastMCP: DB tools, mail, schema (Process Server)
│   └── frame_server.py            # FastAPI + FastMCP: rule management, process agent (Frame Server)
├── experiment/                    # Experiment pipeline
│   ├── runner.py                  # Experiment loop (rule addition + process execution)
│   ├── session.py                 # Session lifecycle (seed, session_id, DB reset)
│   ├── evaluator.py               # Ground truth computation + evaluation metrics
│   └── results.py                 # Results aggregation, LaTeX tables
├── db/
│   └── setup.py                   # Database creation from CSVs
├── scripts/                       # Shell scripts to run full experiment suites
│   ├── run_all.sh                 # Run all 9 experiment configurations sequentially
│   ├── run_all_add.sh             # Run all add-method experiments
│   ├── run_all_bpmn.sh            # Run all BPMN-method experiments
│   ├── run_all_classic.sh         # Run all classic-method experiments
│   ├── test_all.sh                # Smoke test (1 run per config)
│   ├── 01_base_add.sh             # Individual experiment scripts
│   ├── 02_base_bpmn.sh
│   ├── 03_exception_handling_add.sh
│   ├── ...
│   └── 09_db_error_classic.sh
├── bpmn/                          # BPMN XML files per tour/adaptation (28 files)
├── data/                          # Ground truth CSVs for evaluation
├── data_prep/                     # Source CSVs for database setup
├── sessions/                      # Agent conversation logs and outputs per session
├── failed_session_examples/       # Examples of failed sessions (see below)
├── experiment_results/            # Partial CSV results per experiment run
├── results/                       # Aggregated XLSX results
├── run_experiment.py              # CLI entry point (run/evaluate experiments)
├── generate_xlsx_results.py       # Generate final XLSX result files from experiment_results/
└── calculate_results.py           # Aggregate results into summary + LaTeX tables
```

## Special Folders and Scripts

- **`scripts/`** -- Shell scripts that handle the full lifecycle: database setup, server start/stop, experiment execution, and evaluation. Use `bash scripts/run_all.sh` to run all experiments or individual scripts like `bash scripts/01_base_add.sh`.
- **`config/process_adaptations.py`** -- Contains all process rule prompts: `TEXT_RULES` (add method), `CLASSIC_RULES` (classic agent prompt method), and `BPMN_RULES` (BPMN file references for generate_bpmn method).
- **`servers/`** -- Two-server MCP architecture. The Process Server exposes database tools (`run_sqlite_query`, `prepare_csv`, `send_mail`, etc.). The Frame Server manages rule generation and delegates to the process agent.
- **`sessions/`** -- Full logging of agent conversations. Each session folder contains `frame_agent_process_addition.txt`, `frame_agent_process_execution.txt`, `process_agent.txt`, exported CSVs, and metadata files.
- **`failed_session_examples/`** -- Curated examples of agent failures that motivated implementation decisions such as timeouts (15 min for Frame Agent, 30 min for Process/Tactical Agent, 45 min for Classic Agent baseline) and recursion limits.
- **`bpmn/`** -- BPMN 2.0 XML files created with Camunda Modeler, one per tour (J09A-J09D) and process adaptation (7 adaptations = 28 files total).
- **`generate_xlsx_results.py`** -- Generates the final XLSX result workbooks from the partial CSVs in `experiment_results/`. Produces per-model and cross-model result files in `results/`.

## Installation

**Prerequisites:** Python 3.12+

```bash
# Option A: Using conda
conda create -n ape python=3.12
conda activate ape
pip install -r requirements.txt

# Option B: Using venv
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Configure environment variables:**

Copy `.env.example` to `.env` and set your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and set: OPENAI_API_KEY=<your-key-here>
```

For running experiments with local Ollama models, configure `.env.ollama`:
```bash
# .env.ollama (already provided with defaults)
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_API_KEY=ollama
```
This requires a running Ollama instance (`ollama serve`) with the desired model pulled.

## Running Experiments

```bash
# Database setup
python run_experiment.py --setup-db --experiment-type base

# Run all experiments
bash scripts/run_all.sh

# Or with a different model
bash scripts/run_all.sh --model gpt-5.4

# Smoke test (1 run per configuration)
bash scripts/test_all.sh

# Generate final result files
python generate_xlsx_results.py
```

---

# Changelog
