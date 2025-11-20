USE sixt_development;

SELECT *
FROM vehicles
WHERE id IN (SELECT vehicle_id FROM parkings_vehicles WHERE parking_id=3);
    
