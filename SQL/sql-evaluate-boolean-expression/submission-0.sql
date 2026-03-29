-- Write your query below
select a.left_operand,a.operator,a.right_operand,
CASE
    WHEN operator = '>' and l>v.value THEN 'true'
    WHEN operator = '=' and l=v.value THEN 'true'
    WHEN operator = '<' and l<v.value THEN 'true'
    ELSE 'false'
END as value
from (select e.left_operand,e.operator,e.right_operand,v.value as l from expressions e left join variables v on e.left_operand=v.name) a join variables v on a.right_operand=v.name
