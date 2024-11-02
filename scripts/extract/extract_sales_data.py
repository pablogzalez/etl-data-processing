import pandas as pd

def extract_data():
    print("Extrayendo datos desde el archivo CSV de ventas...")
    df = pd.read_csv('/opt/airflow/data/input/sales/sales_data.csv')
    df.to_csv('/opt/airflow/data/output/sales/extracted_data.csv', index=False)
    return '/opt/airflow/data/output/sales/extracted_data.csv'
