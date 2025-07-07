SELECT t.illness, AVG((CAST(end_date AS date) - CAST(start_date AS date))) AS avg_treatment_duration
FROM treatments t
GROUP BY t.illness
ORDER BY avg_treatment_duration DESC