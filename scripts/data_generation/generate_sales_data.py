import os
import random
from faker import Faker
import pandas as pd


def generate_sales_data(num_records=10000):  # num_records es ahora un parámetro
    fake = Faker()
    data = []
    for i in range(num_records):
        order_id = num_records + 1 + i
        customer_id = f'C{random.randint(1, 100):03d}'
        customer_name = fake.name()
        product_id = f'P{random.randint(100, 200)}'
        product_name = fake.word()
        category = random.choice(['Electronics', 'Furniture', 'Office Supplies', 'Appliances', 'Clothing', 'Toys', 'Sports', 'Books', 'Music', 'Movies'])
        quantity = random.randint(1, 10)
        price_per_unit = round(random.uniform(10, 1000), 2)
        discount = round(random.uniform(0, 0.3), 2)
        total_amount = round(quantity * price_per_unit * (1 - discount), 2)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        shipping_date = fake.date_between(start_date=order_date, end_date='+5d')
        status = random.choice(['Pending', 'Shipped', 'Cancelled', 'Returned', 'Completed'])
        payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash'])
        sales_rep = fake.name()

        data.append({
            'order_id': order_id,
            'customer_id': customer_id,
            'customer_name': customer_name,
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'quantity': quantity,
            'price_per_unit': price_per_unit,
            'discount': discount,
            'total_amount': total_amount,
            'order_date': order_date,
            'shipping_date': shipping_date,
            'status': status,
            'payment_method': payment_method,
            'sales_rep': sales_rep
        })

    df = pd.DataFrame(data)

    # Definir la ruta de salida usando una ruta absoluta
    output_dir = '/opt/airflow/data/input/sales'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'sales_data.csv')

    # Guardar el archivo CSV
    df.to_csv(output_file, index=False)
    print(f"Archivo '{output_file}' generado con {len(data)} registros.")

if __name__ == "__main__":
    generate_sales_data()  # Puedes especificar num_records aquí, por ejemplo, generate_sales_data(num_records=5000)
