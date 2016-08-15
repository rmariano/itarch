INSERT INTO archive_orders
SELECT * from orders
WHERE order_date < '2016-01-01';

DELETE from orders WHERE order_date < '2016-01-01';
