# Write your MySQL query statement below
select max(num) as num
from MyNumbers
where num in (
    select if(count(num) = 1, num, null)
    from MyNumbers
    group by num
)