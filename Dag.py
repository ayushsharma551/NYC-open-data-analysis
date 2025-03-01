from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import subprocess

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'nyc_open_data_ingestion',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    def run_ingestion_script():
        """Execute the existing ingestion script."""
        script_path = '/path/to/initial.py'  # Update with the actual path
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Script failed: {result.stderr}")
        print(result.stdout)
    
    run_script_task = PythonOperator(
        task_id='run_ingestion_script',
        python_callable=run_ingestion_script,
    )
