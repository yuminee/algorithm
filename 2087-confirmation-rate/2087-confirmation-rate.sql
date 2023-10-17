select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s
left outer join Confirmations as c on (s.user_id=c.user_id) or c.user_id is null
group by s.user_id