# Write your MySQL query statement below
select
t.month,
t.country,
count(t.country) as trans_count,
sum(IF(t.state = "approved",1,0)) as approved_count,
sum(amount) as trans_total_amount,
sum(if(t.state = "approved", t.amount, 0)) as approved_total_amount
from (
    select DATE_FORMAT(trans_date,'%Y-%m') as month,
    country, state, amount
    from Transactions
) as t
group by t.month, t.country


