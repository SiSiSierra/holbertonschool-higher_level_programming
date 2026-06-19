-- Get scores (above 9) and names
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
