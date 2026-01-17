--  a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command


SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
