USE Labor_SQL;

SELECT
    *
FROM
    Trip
WHERE
    TIME(Trip.time_out) BETWEEN '12:00:00' AND '17:00:00';
