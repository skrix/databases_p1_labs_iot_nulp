USE Labor_SQL;

SELECT DISTINCT maker 
FROM Product
WHERE EXISTS (
	SELECT model 
    FROM PC
    WHERE PC.model = Product.model
);
