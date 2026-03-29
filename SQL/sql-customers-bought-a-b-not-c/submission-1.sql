-- Write your query below
SELECT * from customers where
    customer_id not in (SELECT customer_id from orders where product_name = 'C')
    and customer_id in 
        (SELECT customer_id from orders where product_name = 'A') 
    and customer_id in 
        (SELECT customer_id from orders where product_name = 'B') 
    ORDER BY customer_name 