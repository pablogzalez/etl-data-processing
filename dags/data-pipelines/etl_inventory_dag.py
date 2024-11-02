import sys

# Añadir la ruta al sys.path
sys.path.append('/opt/airflow')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract.extract_inventory_data import extract_inventory_data
from scripts.transform.transform_inventory_data import transform_inventory_data
from scripts.load.load_inventory_data import load_inventory_data
from airflow.operators.bash import BashOperator

# Definir el DAG
with DAG('etl_inventory_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily', catchup=False) as dag:


    generate_data_task = BashOperator(
        task_id='generate_inventory_data',
        bash_command='python /opt/airflow/scripts/data_generation/generate_inventory_data.py',
    )

    extract_task = PythonOperator(
        task_id='extract_inventory_data',
        python_callable=extract_inventory_data
    )

    transform_task = PythonOperator(
        task_id='transform_inventory_data',
        python_callable=lambda: transform_inventory_data('/opt/airflow/data/output/inventory/extracted_inventory_data.csv')
    )

    load_task = PythonOperator(
        task_id='load_inventory_data',
        python_callable=lambda: load_inventory_data('/opt/airflow/data/output/inventory/transformed_inventory_data.csv')
    )

    generate_data_task >> extract_task >> transform_task >> load_task
