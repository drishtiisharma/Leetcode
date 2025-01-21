SELECT visited_on,
    (SELECT SUM(amount) FROM customer
    WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
    ) AS amount,
    (SELECT ROUND(SUM(amount)/7,2) FROM customer
    WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
    ) AS average_amount
FROM customer c
WHERE visited_on >=(SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM CUSTOMER)
GROUP BY visited_on
