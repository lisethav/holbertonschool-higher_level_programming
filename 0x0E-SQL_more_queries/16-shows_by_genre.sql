-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
Join tv_genres on tv_show_genres.genres_id 
ORDER BY tv_shows.title, tv_genres.name ASC;