SELECT 
    maker,
    CASE 
        WHEN EXISTS (
            SELECT 1 
            FROM Product p2 
            WHERE p2.maker = p1.maker AND p2.type = 'Laptop'
        ) THEN CONCAT('yes(',
             (
                SELECT COUNT(*) 
                FROM Laptop l
                WHERE l.model IN (
                    SELECT model 
                    FROM Product 
                    WHERE maker = p1.maker AND type = 'Laptop'
                )
            ), ')')
        ELSE 'no'
    END AS laptop
FROM Product p1
GROUP BY maker;