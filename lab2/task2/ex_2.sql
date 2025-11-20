USE sixt_development;

SELECT v.id, v.make, v.model, v.plate, SUM(p.amount) AS total_rentings_payments
FROM vehicles AS v
JOIN rentings AS r ON v.id = r.vehicle_id
JOIN rentings_payments AS rp ON r.id = rp.renting_id
JOIN payments AS p ON p.id = rp.payment_id AND p.status = 'paid'
GROUP BY v.id, v.make, v.model, v.plate
ORDER BY v.id;

