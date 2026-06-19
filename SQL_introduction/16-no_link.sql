-- Show score and name where name isnt null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
