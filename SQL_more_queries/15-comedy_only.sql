-- List all shows with comedy genre
SELECT s.title
FROM tv_show_genres AS sg
INNER JOIN tv_shows AS s ON sg.show_id = s.id
INNER JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY s.title
