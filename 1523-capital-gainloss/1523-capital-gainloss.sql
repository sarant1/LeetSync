# Write your MySQL query statement below

SELECT q.stock_name, SUM(q.capital_gain_loss) as capital_gain_loss
FROM
(SELECT stock_name, operation, price * CASE WHEN operation = 'Buy' THEN -1 ELSE 1 END AS capital_gain_loss
FROM Stocks) as q
GROUP BY stock_name




