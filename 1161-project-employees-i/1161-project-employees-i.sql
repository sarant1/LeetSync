# Write your MySQL query statement below
SELECT p.project_id, ROUND(SUM(e.experience_years)/COUNT(p.project_id),2) AS average_years
FROM Project p
LEFT JOIN Employee e
USING(employee_id)
GROUP BY project_id
