# Write your MySQL query statement below
SELECT name
FROM Employee
WHERE id IN
(
SELECT e.managerId
FROM Employee e
GROUP BY e.managerId
HAVING COUNT(managerId) >= 5)



