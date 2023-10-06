# Write your MySQL query statement below
SELECT s.user_id, ROUND(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
USING(user_id)
GROUP BY user_id


