-- This displays the average temperature by city ordered by temperatures desc

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
