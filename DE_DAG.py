from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
import subprocess
from loading import load_data 
from ML import run_ml
from Extract import fetch_and_save_data

default_args = {
    "owner": "airflow",
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    "data_pipeline",
    default_args=default_args,
    schedule_interval="0 * * * *", 
    start_date=datetime(2025, 1, 5),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=fetch_and_save_data,
    )

    sensor_task = FileSensor(
        task_id="file_sensor_verification",
        filepath="/home/hadoop/DE2/diabetes.json",
        poke_interval=10,
        timeout=100,
    )

    transform_data = BashOperator(
        task_id='transform_data',
        bash_command='DataTrans.sh',
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    ml_task = PythonOperator(
        task_id="run_ml",
        python_callable=run_ml,
    )

    extract_task >> sensor_task >> transform_data >> load_task >> ml_task
