-- List all genres related to Dexter
SELECT g.name
FROM tv_show_genres AS sg
INNER JOIN tv_shows AS s ON sg.show_id = s.id
INNER JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE s.title = "Dexter"
ORDER BY g.name
