SELECT d.doctor_id, d.name, COUNT(status) AS cancelled_appointments
FROM doctors d 
JOIN appointments a ON a.doctor_id = d.doctor_id
WHERE status = 'Cancelled' 
GROUP BY d.doctor_id, d.name
ORDER BY COUNT(status) DESC
LIMIT 1