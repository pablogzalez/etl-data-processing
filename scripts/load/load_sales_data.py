from elasticsearch import Elasticsearch, helpers
import pandas as pd
import os

def create_sales_index(es):
    mapping = {
        "mappings": {
            "properties": {
                "order_id": {"type": "keyword"},
                "customer_id": {"type": "keyword"},
                "customer_name": {"type": "text"},
                "product_id": {"type": "keyword"},
                "product_name": {"type": "text"},
                "category": {"type": "keyword"},
                "quantity": {"type": "integer"},
                "price_per_unit": {"type": "float"},
                "discount": {"type": "float"},
                "total_amount": {"type": "float"},
                "order_date": {"type": "date"},
                "shipping_date": {"type": "date"},
                "status": {"type": "keyword"},
                "payment_method": {"type": "keyword"},
                "sales_rep": {"type": "text"},
                "date_upd": {"type": "date"}  # No especificamos el formato para usar el predeterminado
            }
        }
    }
    es.indices.create(index='sales', body=mapping)
    print("Índice 'sales' creado con mapping personalizado.")

def load_data(file_path):
    print("Cargando datos transformados en Elasticsearch...")

    es = Elasticsearch(['http://elasticsearch:9200'])

    # Eliminar y crear el índice si existe
    if es.indices.exists(index='sales'):
        es.indices.delete(index='sales')
        print("Índice 'sales' eliminado.")
    create_sales_index(es)

    # Leer los datos transformados
    df = pd.read_csv(file_path)

    # Convertir fechas a formato datetime
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['shipping_date'] = pd.to_datetime(df['shipping_date'])
    df['date_upd'] = pd.to_datetime(df['date_upd'])

    # Convertir DataFrame a registros
    records = df.to_dict(orient='records')

    # Preparar acciones para la indexación en bulk
    actions = [
        {
            "_index": "sales",
            "_id": record['order_id'],
            "_source": record
        }
        for record in records
    ]

    # Indexar los datos en bulk
    helpers.bulk(es, actions)

    print("Datos cargados exitosamente en el índice 'sales' de Elasticsearch.")