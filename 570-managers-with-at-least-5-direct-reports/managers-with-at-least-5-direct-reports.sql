# Write your MySQL query statement below
SELECT name
FROM Employee e
JOIN (SELECT managerId, COUNT(*) as num
    FROM Employee
    GROUP BY managerId
    HAVING num >= 5) sub ON e.id = sub.managerId

        