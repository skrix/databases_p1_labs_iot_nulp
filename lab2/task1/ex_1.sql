USE Labor_SQL;

SELECT
    Ships.name, Ships.launched
FROM
    Ships
WHERE
    Ships.launched > 1920
        AND Ships.launched < 1942
ORDER BY Ships.launched DESC;
