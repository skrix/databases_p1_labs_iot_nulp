SELECT p.maker, pc.model, p.type, pc.price
FROM PC pc
JOIN Product p ON pc.model = p.model
WHERE p.maker = 'B'

UNION
SELECT p.maker, l.model, p.type, l.price
FROM Laptop l
JOIN Product p ON l.model = p.model
WHERE p.maker = 'B'

UNION
SELECT p.maker, pr.model, p.type, pr.price
FROM Printer pr
JOIN Product p ON pr.model = p.model
WHERE p.maker = 'B';