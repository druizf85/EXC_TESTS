WITH product_ranking AS (

SELECT c.customer_id, c.name, p.product_id, p.product_name, COUNT(transaction_id) AS purchase_count, ROW_NUMBER() OVER(PARTITION BY c.customer_id ORDER BY COUNT(transaction_id) DESC) AS rn
FROM transactions AS t
JOIN products AS p
ON t.product_id = p.product_id
JOIN customers AS c
ON t.customer_id = c.customer_id
WHERE t.type = 'credit'
GROUP BY c.customer_id, c.name, p.product_id, p.product_name
ORDER BY purchase_count DESC

)

SELECT customer_id, name, product_id AS top_product_id, product_name AS top_product_name, purchase_count
FROM product_ranking AS p
WHERE rn = 1
ORDER BY customer_id

