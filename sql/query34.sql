create view view34 as (select * from 
(select * from 
(select count(*) as number1, year(p.start_date) as year1, f.id as f_id1, f.name as name1 from project p 
inner join 
foundation f on p.foundation_id = f.id group by year1, f_id1) g where g.number1 > 9) k 
inner join 
(select * from 
(select count(*) as number2, year(p.start_date) as year2, f.id as f_id2, f.name as name2 from project p 
inner join 
foundation f on p.foundation_id = f.id group by year2, f_id2) l where l.number2 > 9) b 
on k.f_id1 = b.f_id2 and k.year1 = b.year2 + 1 and k.number1 = b.number2);