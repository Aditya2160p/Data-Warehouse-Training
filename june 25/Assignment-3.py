from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

def parent_task():
    print("Parent done")

def child_task(execution_date=None, **kwargs):
    print(f"Child running, parent date: {execution_date}")

with DAG("parentDag",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as parentDag:

    task1 = PythonOperator(task_id="parentTask", python_callable=parent_task)
    trigger = TriggerDagRunOperator(
        task_id="trigger_child",
        trigger_dag_id="childDag",
        conf={"parent_exec_date": "{{ ds }}"}
    )
    task1 >> trigger

with DAG("childDag",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as childDag:

    t2 = PythonOperator(
        task_id="childTask",
        python_callable=child_task,
        op_kwargs={"execution_date": "{{ dag_run.conf.parent_exec_date }}"}
    )