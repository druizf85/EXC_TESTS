SELECT p.patient_id, p.name, COUNT(status) AS cancelled_appointments
FROM patients p 
JOIN appointments a ON a.patient_id = p.patient_id
WHERE status = 'Cancelled' 
GROUP BY p.patient_id, p.name
HAVING COUNT(status) > 1
ORDER BY COUNT(status) DESC