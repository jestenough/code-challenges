-- you will be given a table, goals, with columns la_liga_goals, copa_del_rey_goals, and champions_league_goals. Return a table with a column, res.
SELECT (la_liga_goals+copa_del_rey_goals+champions_league_goals) as res
FROM goals