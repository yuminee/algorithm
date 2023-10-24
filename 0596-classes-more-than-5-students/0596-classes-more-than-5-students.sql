# Write your MySQL query statement below
select class
from Courses
where class in (
    select if(count(student)>=5, class, null)
    from Courses
    group by class
)
group by class