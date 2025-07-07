WITH first_appointment_patient AS (
SELECT patient_id, MIN(CAST(appointment_date AS date)) AS first_appointment
FROM appointments
GROUP BY patient_id
),

timegap_recovered_patients AS (
SELECT p.name, t.patient_id, t.start_date, fa.first_appointment, (CAST(t.start_date AS date) - fa.first_appointment) AS timegap
FROM treatments t
JOIN first_appointment_patient fa ON fa.patient_id = t.patient_id
JOIN patients p ON p.patient_id = t.patient_id
WHERE t.outcome = 'Recovered'
)

SELECT AVG(timegap)
FROM timegap_recovered_patients