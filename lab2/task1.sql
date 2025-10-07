SELECT 
    Labor_SQL.Ships.name, Labor_SQL.Ships.launched
FROM
    Labor_SQL.Ships
WHERE
    Labor_SQL.Ships.launched > 1920
        AND Labor_SQL.Ships.launched < 1942
ORDER BY Labor_SQL.Ships.launched DESC;