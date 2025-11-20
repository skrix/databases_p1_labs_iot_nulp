USE sixt_development;

SELECT
    u.id, u.first_name, u.middle_name, u.last_name,
    v.make, v.model, v.plate,
    r.start_at AS rent_start_at, r.end_at AS rent_end_at,
    p.amount AS payment_amount, p.currency AS payment_currency,
    f.violation AS fine, f.amount AS fine_amount, f.currency AS fine_currency
FROM rentings AS r
JOIN users AS u ON u.id = r.user_id
JOIN vehicles AS v ON v.id = r.vehicle_id
JOIN rentings_payments AS rp ON rp.renting_id = r.id
JOIN payments AS p ON p.id = rp.payment_id
JOIN rentings_fines AS rf ON rf.renting_id = r.id
JOIN fines AS f ON f.id = rf.fine_id
ORDER BY u.id;
