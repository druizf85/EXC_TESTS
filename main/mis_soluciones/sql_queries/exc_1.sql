WITH credit_trans AS (
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