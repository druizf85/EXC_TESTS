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
Problem Statement
Find the top 2 customers who spent the most money (net total amount) on transactions, considering only successful credit transactions.

Requirements:
Use only credit transactions.
Use either SQL or pandas (your choice).
Return a table (or DataFrame) with:

- customer_id
- customer_name
- total_credit_amount

Sort from highest to lowest.
Show only the top 2.
"""

#SQL 

query = """
WITH credit_trans AS 
(
SELECT * 
FROM transactions 
WHERE type = 'credit'
)

SELECT c.customer_id, c.name, SUM(cr.amount) AS total_credit_amount
FROM customers AS c
JOIN credit_trans AS cr
ON cr.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_credit_amount DESC
LIMIT 2
"""

tf.excecute_query(query,conn)

#Python

transactions_credit = transactions.loc[transactions['type'] == 'credit',:]
trans_credit_users = pd.merge(transactions_credit, customers[['name','customer_id']], on='customer_id')
trans_credit_users_grouped = trans_credit_users.groupby(['customer_id','name']).agg({'amount':'sum'}).reset_index().sort_values(by='amount', ascending=False).head(2)
trans_credit_users_grouped = trans_credit_users_grouped[['customer_id','name', 'amount']].rename(columns={'amount':'total_credit_amount'})
trans_credit_users_grouped