# import sqlite3
import pandas as pd
import funciones.test_func as tf

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

host=os.getenv("DB_HOST2")
port=os.getenv("DB_PORT2")
database=os.getenv("DB_NAME2")
user=os.getenv("DB_USER2")
password=os.getenv("DB_PASS2")

data_transactions = pd.DataFrame({
    'transaction_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_id': [101, 102, 101, 103, 102, 101, 104, 103, 102, 101],
    'product_id': [201, 202, 201, 203, 204, 205, 202, 206, 207, 201],
    'transaction_date': [
        '2023-01-05', '2023-01-07', '2023-01-15', '2023-01-20', '2023-02-02',
        '2023-02-14', '2023-02-18', '2023-03-01', '2023-03-02', '2023-03-10'
    ],
    'amount': [200, -100, 500, 1200, -50, -300, 400, -200, 1000, -100],
    'type': ['credit', 'debit', 'credit', 'credit', 'debit', 'debit', 'credit', 'debit', 'credit', 'debit'],
    'payment_method': ['card', 'paypal', 'transfer', 'card', 'paypal', 'card', 'cash', 'cash', 'transfer', 'paypal']
})
data_name_trans='transactions'

data_customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [29, 35, 42, 31],
    'country': ['USA', 'Canada', 'USA', 'UK'],
    'signup_date': ['2022-11-10', '2022-12-15', '2023-01-01', '2023-02-10']
})
data_name_cust = 'customers'

data_products = pd.DataFrame({
    'product_id': [201, 202, 203, 204, 205, 206, 207],
    'product_name': ['Subscription A', 'E-Book', 'Online Course', 'Gift Card', 'Consulting Call', 'Webinar', 'Premium Upgrade'],
    'category': ['subscription', 'digital', 'education', 'gift', 'service', 'event', 'upgrade'],
    'price': [200, 100, 1200, 50, 300, 200, 1000]
})
data_name_prod = 'products'

# engine= sqlite3.connect('mi_base.db') 

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

tf.create_dataframe_sql(engine, data_transactions, data_name_trans)
tf.create_dataframe_sql(engine, data_customers, data_name_cust)
tf.create_dataframe_sql(engine, data_products, data_name_prod)

print("Base de datos creada y tablas cargadas.")
# engine.close()