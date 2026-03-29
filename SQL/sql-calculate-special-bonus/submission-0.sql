-- Write your query below
SELECT e.employee_id,
    CASE 
        WHEN e.employee_id%2=1 AND e.name NOT LIKE 'M%' THEN e.salary
        else 0
    end as bonus
from employees as e order by e.employee_id asc