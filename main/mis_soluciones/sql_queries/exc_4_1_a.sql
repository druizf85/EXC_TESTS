WITH recovered_patients AS (
SELECT patient_id 
FROM treatments
WHERE outcome = 'Recovered'
)

SELECT d.name, COUNT(DISTINCT a.patient_id) AS recovered_patients
FROM appointments a
JOIN recovered_patients rp ON rp.patient_id = a.patient_id
JOIN doctors d ON d.doctor_id = a.doctor_id
GROUP BY d.name
ORDER BY COUNT(DISTINCT a.patient_id) DESC
LIMIT 1

