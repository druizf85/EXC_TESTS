SELECT p.patient_id, p.name, t.illness, (CAST(end_date AS date) - CAST(start_date AS date)) AS treatment_duration
FROM treatments t
JOIN patients p on p.patient_id = t.patient_id
ORDER BY treatment_duration DESC
LIMIT 1