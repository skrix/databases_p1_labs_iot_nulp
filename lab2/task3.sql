USE Labor_SQL;

SELECT DISTINCT
    l1.model AS model1, 
    l2.model AS model2, 
    l1.hd, 
    l1.ram
FROM Laptop l1, Laptop l2
WHERE l1.code <> l2.code
	AND l1.hd = l2.hd 
	AND l1.ram = l2.ram
ORDER BY l1.model, l2.model;
