SELECT TO_CHAR(CAST(transaction_date AS date), 'YYYY-MM') AS month_trans, SUM(amount) AS total_credit_amount
FROM transactions
WHERE type = 'credit' 
GROUP BY TO_CHAR(CAST(transaction_date AS date), 'YYYY-MM'), type
ORDER BY month_trans