import pandas as pd
import os
from datetime import datetime

def transform_data(file_path):
    print("Transformando datos de ventas...")
    df = pd.read_csv(file_path)

    # Realiza tus transformaciones existentes...
    # Por ejemplo, calcular 'total_amount', filtrar por 'status', etc.

    # Añadir el campo 'date_upd' con la fecha y hora actual en formato ISO 8601
    df['date_upd'] = datetime.utcnow().isoformat() + 'Z'

    # Convertir fechas a formato datetime
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['shipping_date'] = pd.to_datetime(df['shipping_date'])

    # Guardar el DataFrame transformado
    output_path = '/opt/airflow/data/output/sales/transformed_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path