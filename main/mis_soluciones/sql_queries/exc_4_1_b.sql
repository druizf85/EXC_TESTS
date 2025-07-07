
WITH recovered_patients AS (
SELECT patient_id 
FROM treatments
WHERE outcome = 'Recovered'
),

recovered_from_each_doctor AS (
SELECT d.doctor_id, d.name, COUNT(DISTINCT a.patient_id) AS recovered_patients
FROM appointments a
JOIN recovered_patients rp ON rp.patient_id = a.patient_id
JOIN doctors d ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.name
ORDER BY COUNT(DISTINCT a.patient_id) DESC
),

treated_from_each_doctor AS (
SELECT d.doctor_id, d.name, COUNT(DISTINCT a.patient_id) AS treated_patients
FROM appointments a
JOIN treatments t ON t.patient_id = a.patient_id
JOIN doctors d ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.name
ORDER BY COUNT(DISTINCT a.patient_id) DESC
)

SELECT tfed.name, recovered_patients, treated_patients, ROUND(1.0 * recovered_patients/treated_patients,2) AS recovery_rate
FROM treated_from_each_doctor tfed
JOIN recovered_from_each_doctor rfed ON tfed.doctor_id = rfed.doctor_id
ORDER BY recovery_rate DESC
LIMIT 1