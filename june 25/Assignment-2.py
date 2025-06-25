import pandas as pd
from pathlib import Path
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

Source = Path("/opt/airflow/dags/data/orders.csv")

def validation():
    df = pd.read_csv(Source)
    required = {"order_id", "customer_id", "amount"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")
    if df[["order_id", "customer_id", "amount"]].isnull().any().any():
        raise ValueError("Null values found in mandatory fields")
    print("Validation passed")
    return True

def summarization():
    df = pd.read_csv(Source)
    print(df.groupby("customer_id")["amount"].sum())

with DAG("data_quality_validation",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    task1 = PythonOperator(task_id="validation", python_callable=validation)
    task2 = PythonOperator(task_id="summarization", python_callable=summarization)

    task1 >> task2