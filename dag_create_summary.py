≈from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
}

with DAG(
    dag_id='build_session_summary',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['elt', 'snowflake']
) as dag:

    join_tables = SnowflakeOperator(
        task_id='create_session_summary',
        sql="""
        CREATE OR REPLACE TABLE analytics.session_summary AS
        SELECT DISTINCT
            a.userId,
            a.sessionId,
            a.channel,
            b.ts
        FROM raw.user_session_channel a
    JOIN raw.session_timestamp b
    ON a.sessionId = b.sessionId;
    """,
        snowflake_conn_id='snowflake_conn' 
    )

