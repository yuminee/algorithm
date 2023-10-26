# # Write your MySQL query statement below
select e.employee_id, e.name, count(r.reports_to) as reports_count, round(avg(r.age),0) as average_age
from Employees as e
inner join (
    select reports_to, age
    from Employees
    where reports_to is not null
) as r on e.employee_id = r.reports_to
group by employee_id
order by e.employee_id