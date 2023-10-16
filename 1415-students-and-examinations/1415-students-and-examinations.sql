select  s.student_id, s.student_name, s.subject_name, count(e.subject_name) as attended_exams
from (select *
from Students
inner join Subjects) as s
left outer join Examinations as e on s.student_id = e.student_id and s.subject_name = e.subject_name
group by s.student_id, s.subject_name
order by s.student_id, s.subject_name asc;