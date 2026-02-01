from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

from src.analysis.run_experiment import run_experiment_analysis


with DAG(
    dag_id="voucher_ui_experiment_daily",
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 0 * * *",  # daily at midnight
    catchup=False,
    tags=["ab-testing", "experimentation"],
) as dag:

    refresh_experiment_outcomes = SQLExecuteQueryOperator(
        task_id="refresh_experiment_outcomes",
        conn_id="analytics_warehouse",
        sql="sql/user_outcomes.sql",
    )

    analyze_experiment = PythonOperator(
        task_id="analyze_experiment_results",
        python_callable=run_experiment_analysis,
    )

    refresh_experiment_outcomes >> analyze_experiment
