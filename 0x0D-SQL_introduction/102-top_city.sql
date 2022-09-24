-- This displays the top 3 of cities temperature during july August
-- ordered by temperature

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN 7 and 8
GROUP BY avg_temp DESC
LIMIT 3;
