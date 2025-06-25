from pathlib import Path
from datetime import datetime
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator

Source= Path("/opt/airflow/dags/data/incoming/report.csv")
Archive= Path("/opt/airflow/dags/archive/")

def process_report():
    print(f"Processing {Source}")

def archive_report():
    Archive.mkdir(parents=True, exist_ok=True)
    Source.rename(Archive/ Source.name)
    print(f"Archived to {Archive}")

with DAG(
    dag_id="file_sensor_pipeline",
    start_date=datetime(2025,1,1),
    schedule_interval=None,
    catchup=False
) as dag:
    wait = FileSensor(
        task_id="wait_for_report",
        filepath=str(Source),
        poke_interval=30,
        timeout=600,
        mode="poke"
    )
    task1 = PythonOperator(task_id="process_report", python_callable=process_report)
    task2 = PythonOperator(task_id="archive_report", python_callable=archive_report)

    wait >> task1 >> task2