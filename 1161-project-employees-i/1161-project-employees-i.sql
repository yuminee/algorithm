# Write your MySQL query statement below
select p.project_id, ROUND(SUM(e.experience_years)/COUNT(p.project_id), 2) as average_years
from Employee as e
inner join Project p on e.employee_id = p.employee_id
group by p.project_id