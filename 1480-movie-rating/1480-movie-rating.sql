# Write your MySQL query statement below
select *
from
  (
    select name as results
    from (
      select name, count(rating) as count_rating
      from Users as u
      inner join MovieRating as mr on mr.user_id = u.user_id
      group by u.user_id
      order by count_rating desc , name asc
      limit 1
    ) as best_rating_user_name
    union all
    select title as results
    from (
      select avg(rating) as avg_rating, title
      from Movies as m
      inner join MovieRating as mr on mr.movie_id = m.movie_id
      where created_at between "2020-02-01" and "2020-02-29"
      group by m.movie_id
      order by avg_rating desc, m.title asc
      limit 1
    ) as feb_best_avg_movie
  ) as results

