import pandas as pd
from elasticsearch import Elasticsearch, helpers
import os

def create_inventory_index(es):
    mapping = {
        "mappings": {
            "properties": {
                "product_id": {"type": "keyword"},
                "product_name": {"type": "text"},
                "category": {"type": "keyword"},
                "brand": {"type": "keyword"},
                "model": {"type": "keyword"},
                "stock_level": {"type": "integer"},
                "reorder_point": {"type": "integer"},
                "supplier_id": {"type": "keyword"},
                "supplier_name": {"type": "text"},
                "cost_price": {"type": "float"},
                "selling_price": {"type": "float"},
                "last_restock_date": {"type": "date"},
                "warranty_period": {"type": "keyword"},
                "specs": {"type": "text"},
                "total_value": {"type": "float"},
                "date_upd": {"type": "date"}
            }
        }
    }
    es.indices.create(index='inventory', body=mapping)
    print("Índice 'inventory' creado con mapping personalizado.")

def load_inventory_data(file_path):
    print("Cargando datos transformados en Elasticsearch...")

    # Conectar a Elasticsearch
    es = Elasticsearch(['http://elasticsearch:9200'])

    # Crear el índice si no existe
    if not es.indices.exists(index='inventory'):
        create_inventory_index(es)

    # Leer el archivo transformado
    df_filtered = pd.read_csv(file_path)

    # Convertir fechas a formato datetime si no se hizo en la transformación
    if df_filtered['last_restock_date'].dtype == 'object':
        df_filtered['last_restock_date'] = pd.to_datetime(df_filtered['last_restock_date'])

    # Convertir DataFrame a diccionarios
    records = df_filtered.to_dict(orient='records')

    # Preparar acciones para el método bulk
    actions = [
        {
            "_index": "inventory",
            "_id": record['product_id'],  # Usa 'product_id' como ID único
            "_source": record
        }
        for record in records
    ]

    # Indexar datos en Elasticsearch usando el método bulk
    helpers.bulk(es, actions)

    print("Datos cargados exitosamente en el índice 'inventory' de Elasticsearch.")
