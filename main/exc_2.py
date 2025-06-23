import pandas as pd
import sqlite3
import funciones.test_func as tf

conn = sqlite3.connect('mi_base.db') 
tables = tf.excecute_query_tables(conn)

dfs = tf.create_df_variable(tables, conn)
transactions = dfs['transactions']
customers= dfs['customers']
products = dfs['products']

"""
Challenge #2: Monthly revenue trend for the store
Problem Statement:

Calculate the total net revenue per month from all transactions.
Only include credit transactions.

Requirements:
Output should include:

month (e.g., '2023-01')

total_credit_amount

Sort by month in ascending order.

Use either SQL or pandas.

Optional: If you're using pandas, format transaction_date properly if it's not already a datetime.
"""

#SQL 

query = """
SELECT strftime('%m-%Y', transaction_date) AS month_trans, type, SUM(amount) AS total_credit_amount
FROM transactions
WHERE type = 'credit' 
GROUP BY strftime('%m-%Y', transaction_date), type
ORDER BY month_trans
"""

tf.excecute_query(query,conn)

#Python

transactions_credit = transactions[transactions['type'] == 'credit'].copy()
transactions_credit['transaction_date'] = pd.to_datetime(transactions_credit['transaction_date'], format = '%Y-%m-%d', errors='coerce')
transactions_credit['transaction_date_month'] = transactions_credit['transaction_date'].dt.month
transactions_credit_grouped = transactions_credit.groupby(['transaction_date_month','type']).agg({'amount':'sum'}).reset_index().sort_values(by='transaction_date_month', ascending=True)
transactions_credit_grouped.rename(columns={'amount':'total_credit_amount'}, inplace=True)
transactions_credit_grouped