select
    query_name,
    round(sum(q.rating / q.position) / count(q.rating), 2) as quality, 
    round(sum(q.rating < 3)/count(q.rating) * 100, 2) as poor_query_percentage
from Queries as q
group by query_name