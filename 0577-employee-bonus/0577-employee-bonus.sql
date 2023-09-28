# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e 
LEFT JOIN Bonus b
USING(empId)
HAVING b.bonus < 1000 or b.bonus IS NULL