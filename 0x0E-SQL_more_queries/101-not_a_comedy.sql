-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT S.title
FROM tv_shows AS s
WHERE s.id NOT IN (
	SELECT sg.show_id
	FROM tv_show_genres AS sg
	JOIN tv_genres AS g
	ON sg.genre_id = g.id
	WHERE g.name = "Comedy"
)
ORDER BY s.title ASC;
