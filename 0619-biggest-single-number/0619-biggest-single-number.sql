# Write your MySQL query statement below
select max(n.num) as num
from (
    select if(count(num) = 1, num, null) as num
    from MyNumbers
    group by num
) as n