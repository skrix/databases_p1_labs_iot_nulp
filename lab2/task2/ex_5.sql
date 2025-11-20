USE sixt_development;

SELECT
  p.id, p.address, p.country, p.city,
  DATE(r.start_at) AS rental_date,
  SUM(CASE
    WHEN py.currency = 'UAH' THEN py.amount
    WHEN py.currency = 'EUR' THEN py.amount * 42
    WHEN py.currency = 'USD' THEN py.amount * 37
    END)
  AS total_payments_amount_uah
FROM parkings AS p
JOIN parkings_vehicles AS pv ON pv.parking_id = p.id
JOIN vehicles AS v ON v.id = pv.vehicle_id
JOIN rentings AS r ON r.vehicle_id = v.id
JOIN rentings_payments AS rp ON rp.renting_id = r.id
JOIN payments AS py ON py.id = rp.payment_id
WHERE py.status = 'paid'
GROUP BY p.id, p.address, p.country, p.city, rental_date
ORDER BY total_payments_amount_uah DESC, rental_date DESC;
