(select name as results
from Users as u
inner join MovieRating as mr on mr.user_id = u.user_id
group by u.user_id
order by count(rating) desc , name asc limit 1)
union all
(select title as results
from Movies as m
inner join MovieRating as mr on mr.movie_id = m.movie_id
where created_at between "2020-02-01" and "2020-02-29"
group by m.movie_id
order by avg(rating) desc, m.title asc limit 1)


