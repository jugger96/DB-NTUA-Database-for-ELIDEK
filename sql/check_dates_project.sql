select *, count(*) from project where foundation_id = 17 and (year(start_date) = 2015 or year(start_date) = 2016) group by year(start_date);
