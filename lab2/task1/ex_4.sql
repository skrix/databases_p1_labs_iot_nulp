USE Labor_SQL;

SELECT country, class
FROM Classes
WHERE country = 'USA' 
UNION ALL 
	SELECT country, class
	FROM Classes
	WHERE 
		NOT EXISTS( 
			SELECT *
			FROM Classes
			WHERE country = 'USA'
		);
