DELETE FROM Person
WHERE Id NOT IN(SELECT min_id FROM(SELECT min(Id)AS min_id FROM Person GROUP BY Email)AS a);
