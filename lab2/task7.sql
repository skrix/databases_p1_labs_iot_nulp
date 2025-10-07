USE Labor_SQL;

SELECT
	model,
	COUNT(model) AS model_count,
    AVG(price) AS avg_price
FROM PC
GROUP BY model
HAVING avg_price < 800;
