from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/airflow/scripts')
from transform.transform_sales_data import transform_data
from load.load_sales_data import load_data

default_args = {
    'owner': 'tu_nombre',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['tu_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_sales_dag',
    default_args=default_args,
    description='Pipeline ETL para datos de ventas',
    schedule_interval=None,
    catchup=False
)

generate_data_task = BashOperator(
    task_id='generate_sales_data',
    bash_command='python /opt/airflow/scripts/data_generation/generate_sales_data.py',
    dag=dag
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=lambda: '/opt/airflow/data/input/sales/sales_data.csv',
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=lambda: transform_data('/opt/airflow/data/input/sales/sales_data.csv'),
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=lambda: load_data('/opt/airflow/data/output/sales/transformed_data.csv'),
    dag=dag
)

generate_data_task >> extract_task >> transform_task >> load_task
