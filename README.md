# Weekly Active Users (WAU) - Airflow + Snowflake + Superset
--------------------------------------------------------------


### 1. Import Data into Snowflake (ETL)
- Two tables were created and populated:
  - `raw.user_session_channel`
  - `raw.session_timestamp`
- These were imported using an Airflow DAG (`dag_import_snowflake.py`)

---

### 2. Transform Data in Airflow (ELT)
- A second Airflow DAG (`dag_create_summary.py`) was created to:
  - JOIN the two raw tables on `sessionId`
  - Output the result into `analytics.session_summary`
  - Use `SELECT DISTINCT` to remove duplicates 

---

### 3. Connect Superset to Snowflake
- Superset was configured using a SQLAlchemy URI to connect to Snowflake
- Dataset `analytics.session_summary` was added to Superset

---

### 4. Create WAU Chart in Superset
- A bar chart was created using:
  - Time grain: **Week**
  - Metric: **COUNT(DISTINCT userId)**, labeled as `WAU`
  - X-axis: timestamp (`ts`)

---



