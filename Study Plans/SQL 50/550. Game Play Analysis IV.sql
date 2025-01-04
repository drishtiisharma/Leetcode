WITH game_analysis As (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT 
    ROUND(
        SUM(DATEDIFF(a.event_date, ga.first_login) = 1) / COUNT(DISTINCT a.player_id), 2
        ) AS fraction
FROM Activity a
JOIN game_analysis ga USING (player_id);
