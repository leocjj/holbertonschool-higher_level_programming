-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>.
SELECT tv_genres.name FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name;
