truncate orders;
truncate archive_orders;

insert into orders values
    (1, 'First sale order', '2016-01-01'),
    (2, 'Old oder', '2015-11-21'),
    (3, 'from previous year', '2015-03-24'),
    (4, 'to be archived', '2014-12-09'),
    (5, 'First sale order', '2016-07-17'),
    (6, 'First sale order', '2016-07-20'),
    (7, 'First sale order', '2016-07-24');
