from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
}

with DAG(
    dag_id='import_snowflake_tables',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['etl', 'snowflake']
) as dag:

    test_user_session_channel = SnowflakeOperator(
        task_id='test_user_session_channel',
        sql='SELECT * FROM user_session_channel LIMIT 5;',
        snowflake_conn_id='snowflake_conn' 
    )

    test_session_timestamp = SnowflakeOperator(
        task_id='test_session_timestamp',
        sql='SELECT * FROM session_timestamp LIMIT 5;',
        snowflake_conn_id='snowflake_conn'
    )

    test_user_session_channel >> test_session_timestamp

