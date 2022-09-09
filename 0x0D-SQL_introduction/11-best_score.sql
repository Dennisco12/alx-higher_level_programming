-- This displays all records with a score >= 0 in the table
-- second_table of the database hbtn_0c_0 in MySQL server

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score desc;
