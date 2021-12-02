-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT DISTINCT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_shows on tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;