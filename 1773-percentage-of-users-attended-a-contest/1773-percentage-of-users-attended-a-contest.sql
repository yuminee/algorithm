select r.contest_id, round((count(r.user_id)/u.count_u)*100,2) as percentage
from (
    select count(user_id) as count_u
    from Users
) as u, Register as r
group by r.contest_id
order by percentage desc, r.contest_id asc