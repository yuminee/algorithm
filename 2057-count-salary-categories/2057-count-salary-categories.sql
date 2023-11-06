WITH cte AS 
(
    SELECT CASE 
        WHEN income < 20000 THEN "Low Salary"
        WHEN income >= 20000 AND income<=50000 THEN "Average Salary"
        ELSE "High Salary" END cat, 1 as cnt
    FROM accounts
    UNION ALL
    SELECT "Low Salary", 0 
    UNION ALL
    SELECT "Average Salary", 0
    UNION ALL
    SELECT "High Salary", 0
)
SELECT cat category, SUM(cnt) as accounts_count
FROM cte
GROUP BY cat