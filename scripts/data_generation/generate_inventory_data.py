import os
import random
from faker import Faker
import pandas as pd


def generate_inventory_data():
    fake = Faker()
    data = []
    suppliers = [
        {'supplier_id': 'S001', 'supplier_name': 'Supplier Inc.'},
        {'supplier_id': 'S002', 'supplier_name': 'ElectroGoods'},
        {'supplier_id': 'S003', 'supplier_name': 'SoundTech'},
        {'supplier_id': 'S004', 'supplier_name': 'TimeWear'},
        {'supplier_id': 'S005', 'supplier_name': 'TechSuppliers'},
        {'supplier_id': 'S006', 'supplier_name': 'Computers Co.'},
        {'supplier_id': 'S007', 'supplier_name': 'PhotoGear'}
    ]
    categories = ['Smartphones', 'Accessories', 'Tablets', 'Laptops', 'Cameras']

    for i in range(10000):
        product_id = f"P{10000 + i}"
        product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()
        category = random.choice(categories)
        brand = fake.company()
        model = 'Model ' + fake.word().upper()
        stock_level = random.randint(10, 500)
        reorder_point = random.randint(5, 50)
        supplier = random.choice(suppliers)
        cost_price = round(random.uniform(50, 1000), 2)
        selling_price = round(cost_price * random.uniform(1.1, 1.5), 2)
        last_restock_date = fake.date_between(start_date='-90d', end_date='today')
        warranty_period = random.choice(['6 months', '12 months', '18 months', '24 months'])
        specs = fake.sentence(nb_words=6)
        total_value = round(stock_level * cost_price, 2)

        data.append({
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'brand': brand,
            'model': model,
            'stock_level': stock_level,
            'reorder_point': reorder_point,
            'supplier_id': supplier['supplier_id'],
            'supplier_name': supplier['supplier_name'],
            'cost_price': cost_price,
            'selling_price': selling_price,
            'last_restock_date': last_restock_date,
            'warranty_period': warranty_period,
            'specs': specs,
            'total_value': total_value
        })
    df = pd.DataFrame(data)

    # Definir la ruta de salida usando una ruta absoluta
    output_dir = '/opt/airflow/data/input/inventory'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'inventory_data.csv')

    # Guardar el archivo CSV
    df.to_csv(output_file, index=False)
    print(f"Archivo '{output_file}' generado con {len(data)} registros.")


# Ejecutar la función
if __name__ == "__main__":
    generate_inventory_data()
