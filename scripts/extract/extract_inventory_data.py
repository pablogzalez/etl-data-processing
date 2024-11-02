import pandas as pd
import os


def extract_inventory_data():
    print("Extrayendo datos desde el archivo CSV de inventario...")
    input_path = '/opt/airflow/data/input/inventory/inventory_data.csv'
    output_path = '/opt/airflow/data/output/inventory/extracted_inventory_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)
    return output_path
