# Write your MySQL query statement below

SELECT S.user_id, ROUND(COUNT(CASE WHEN action="confirmed" THEN 1 END) / COUNT(user_id), 2) as confirmation_rate 
FROM Signups S
LEFT JOIN Confirmations
USING(user_id)
GROUP BY user_id
