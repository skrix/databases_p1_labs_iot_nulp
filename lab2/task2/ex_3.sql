USE sixt_development;

SELECT v.id, v.make, v.model, v.plate
FROM vehicles AS v
JOIN rentings AS r ON v.id = r.vehicle_id
GROUP BY v.id, v.make, v.model, v.plate
HAVING COUNT(r.id) <= 2
ORDER BY v.id;

