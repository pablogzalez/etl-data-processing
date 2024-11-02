import pandas as pd
import os
from datetime import datetime

def transform_inventory_data(file_path):
    print("Transformando datos de inventario...")
    df = pd.read_csv(file_path)

    # Realiza tus transformaciones existentes...

    # Añadir el campo 'date_upd' en formato ISO 8601
    df['date_upd'] = datetime.utcnow().isoformat() + 'Z'

    # Convertir fechas a formato datetime si es necesario
    df['last_restock_date'] = pd.to_datetime(df['last_restock_date'])

    # Guardar el DataFrame transformado
    output_path = '/opt/airflow/data/output/inventory/transformed_inventory_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path
