WITH deleted as (
    DELETE FROM orders WHERE order_date < '2016-01-01'
    RETURNING *
)
INSERT INTO archive_orders select * from deleted;
