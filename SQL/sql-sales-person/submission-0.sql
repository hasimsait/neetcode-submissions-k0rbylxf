-- Write your query below
select name from sales_person s where s.sales_id not in (select sales_id from orders where com_id in(select com_id from company where name='CRIMSON'))