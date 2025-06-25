import time
import random
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def long_task():
    duration = random.randint(1,10)
    print(f"Sleep {duration}s")
    time.sleep(duration)
    if duration > 8:
        raise RuntimeError("Took too long to respond")

def success(): print("Success")
def faliure(): print("Failed after many retries")

with DAG("retry_timeout_dag",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    task = PythonOperator(
        task_id="long_task",
        python_callable=long_task,
        retries=2,
        retry_delay=timedelta(seconds=10),
        retry_exponential_backoff=True,
        execution_timeout=timedelta(seconds=5)
    )
    tsucess = PythonOperator(task_id="success", python_callable=success, trigger_rule="all_success")
    tfailure = PythonOperator(task_id="faliure", python_callable=faliure, trigger_rule="all_failed")

    task >> [tsucess, tfailure]