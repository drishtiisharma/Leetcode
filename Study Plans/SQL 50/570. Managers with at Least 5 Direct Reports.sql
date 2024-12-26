SELECT x.name
FROM Employee x
JOIN Employee y ON x.id=y.managerId
GROUP BY y.managerID
HAVING COUNT(*)>=5
