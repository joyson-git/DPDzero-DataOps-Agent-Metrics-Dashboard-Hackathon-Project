# DPDzero Data Ops Assignment

## 📌 Objective

Build a simplified end-to-end data pipeline to mimic a real-world operational use case for a loan collections call campaign. The pipeline performs ingestion, validation, transformation, and reporting on call data.(https://www.youtube.com/watch?v=kHCgHTOIhiI) live link

---

## 📂 Input Files

The system expects **3 CSV files** with the following structure:

### 1. `call_logs.csv`
| Column Name   | Description                               |
|---------------|-------------------------------------------|
| call_id       | Unique ID for each call                   |
| agent_id      | Identifier for the calling agent          |
| org_id        | Organization ID                           |
| installment_id| Unique loan installment identifier        |
| status        | Call status (`completed`, `connected`, etc.) |
| duration      | Duration of the call in seconds           |
| created_ts    | Timestamp of the call                     |
| call_date     | Date of the call (YYYY-MM-DD)             |

---

### 2. `agent_roster.csv`
| Column Name           | Description          |
|------------------------|----------------------|
| agent_id              | Unique agent ID       |
| users_first_name      | Agent's first name    |
| users_last_name       | Agent's last name     |
| users_office_location | Office location       |
| org_id                | Organization ID       |

---

### 3. `disposition_summary.csv`
| Column Name | Description             |
|-------------|-------------------------|
| agent_id    | Unique agent ID         |
| org_id      | Organization ID         |
| call_date   | Date of login           |
| login_time  | Agent login time (nullable) |

---

## ✅ Tasks Performed

1. **Data Ingestion & Validation**
   - Loaded CSVs using `pandas`
   - Validated required fields: `agent_id`, `org_id`, `call_date`
   - Flagged missing or duplicate entries

2. **Data Joining**
   - Merged all datasets on `agent_id`, `org_id`, `call_date`
   - Ensured no data loss in the join (used `outer` join and logged mismatches)

3. **Feature Engineering**
   - Computed the following metrics for each agent per day:
     - `Total Calls Made`
     - `Unique Loans Contacted`
     - `Connect Rate = Completed Calls / Total Calls`
     - `Average Call Duration (in minutes)`
     - `Presence` (1 if login time exists, else 0)

4. **Reporting**
   - Final output saved to `agent_performance_summary.csv`
   - Slack-style summary printed:
     ```
     Agent Summary for 2025-04-28
     Top Performer: Ravi Sharma (98% connect rate)
     Total Active Agents: 45
     Average Duration: 6.5 min
     ```

---

## 📤 Output

### 1. `agent_performance_summary.csv`

| agent_id | agent_name    | org_id | call_date  | total_calls | unique_loans | connect_rate | avg_call_duration | presence |
|----------|----------------|--------|------------|-------------|---------------|---------------|-------------------|----------|
| 101      | Ravi Sharma    | 2001   | 2025-04-28 | 50          | 47            | 0.98          | 6.5               | 1        |

### 2. Slack-style Message Example
