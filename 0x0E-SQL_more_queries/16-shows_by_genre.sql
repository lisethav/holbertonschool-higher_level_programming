-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name
FROM tv_genres
RIGHT OUTER JOIN tv_show_genres on tv_show_genres.genre_id = tv_genres.id
RIGHT OUTER JOIN tv_shows on tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;