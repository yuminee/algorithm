select e_uni.unique_id as unique_id, name
from Employees as e
LEFT JOIN EmployeeUNI as e_uni
ON e.id = e_uni.id;