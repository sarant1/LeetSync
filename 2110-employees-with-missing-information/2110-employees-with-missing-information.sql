# Write your MySQL query statement below
SELECT q.employee_id
FROM
(SELECT *
FROM Employees  
LEFT JOIN Salaries  
USING(employee_id)
UNION
SELECT *
FROM Salaries 
LEFT JOIN Employees 
USING(employee_id)) as q
WHERE q.salary IS NULL or q.name IS NULL
ORDER BY employee_id
