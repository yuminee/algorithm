select w.id
from Weather as w
inner join Weather as jw
where DATEDIFF(w.recordDate, jw.recordDate) = 1 and w.temperature > jw.temperature;