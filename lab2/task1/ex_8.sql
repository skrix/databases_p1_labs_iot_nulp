USE Labor_SQL;

SELECT 
    maker,
    (SELECT MIN(speed) FROM PC WHERE PC.model IN (SELECT model FROM Product WHERE Product.maker = P.maker AND Product.type = 'PC')) AS min_speed
FROM Product P
WHERE 
	type = 'PC'
  AND 
	(SELECT MIN(speed) FROM PC WHERE PC.model IN (SELECT model FROM Product WHERE Product.maker = P.maker AND Product.type = 'PC')) >= 500
GROUP BY maker;