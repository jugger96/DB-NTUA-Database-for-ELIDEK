
-- -----------------------------------------------------
-- Views
-- -----------------------------------------------------

-- Query 3.2a
create view view32a as (select res_id, first_name, last_name, Project_ID, title from
(select * from researcher_works_on_project) a inner join
(select r.id as res_id, r.first_name, r.last_name from researcher r) b
on a.researcher_id = b.res_id
inner join
(select p.title, p.id from project p) d
on d.id = project_id
order by res_id);

-- Query 3.3
create view view33 as (select ps.scientific_field_name, ps.project_id, p.title, rw.researcher_id,
r.first_name, r.last_name, p.end_date from (project_scientific_field ps inner join 
project p on p.id = ps.project_id inner join researcher_works_on_project rw on
rw.project_id = ps.project_id inner join researcher r on r.id = rw.researcher_id)
where p.end_date > curdate());
-- where ps.scientific_field_name = '{Name1}' 


-- Query 3.4
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


-- Query 3.5
create view view35 as (select ps1.Scientific_Field_Name as sf1, ps2.Scientific_Field_Name as sf2, count(*) as count 
from project_scientific_field ps1 inner join project_scientific_field ps2 
on ps1.Project_ID = ps2.Project_ID and ps1.Scientific_Field_Name > ps2.Scientific_Field_Name
group by ps1.Scientific_Field_Name, ps2.Scientific_Field_Name 
order by count DESC
limit 3);


-- Query 3.7
create view view37 as (select executive_ID, first_name, last_name, name as Company_Name, ta.id as company_id, 
sum(funding) as total_funding from 
(select p.funding, p.executive_id, p.foundation_id from project p) te inner join 
(select f.name, f.id from foundation f where f.id in (select c.foundation_id from company c)) ta 
on te.foundation_id = ta.id 
inner join executive e  
on e.id = te.executive_id 
group by executive_id, company_id 
order by total_funding desc 
limit 5);

-- Query 3.6
create view view36 as (select id, first_name, last_name, count(*) as projects from (select * from 
 (select r.id, r.first_name, r.last_name, r.birth_date 
from researcher r where datediff(curdate(), birth_date) < 14600) te 
inner join researcher_works_on_project rp on te.id = rp.researcher_id) ta 
inner join (select p.id as project_id, p.end_date from project p where p.end_date > curdate()) tb 
on tb.project_id = ta.project_id 
group by id 
order by projects DESC, last_name 
limit 5);


-- Query 3.8
create view view38 as (select * from (select project_id, researcher_id, first_name, last_name, count(*) as total_projects 
from (select * from (select p.id from project p 
where p.id not in (select d.project_id from deliverable d)) te 
inner join researcher_works_on_project rp on rp.project_id = te.id) ta 
inner join (select first_name, last_name, id as res_id from researcher) r 
on r.res_id = ta.researcher_id 
group by ta.researcher_id) tt 
where total_projects > 4 
order by total_projects DESC, last_name);

create view foundations_with_phones as select id, name, abbreviation, postal_code, street, street_number, city, 
GROUP_CONCAT(phone_number separator ', ') as phones 
from foundation f inner join foundation_extra_phones p on f.id=p.foundation_id group by id;

create view company_v as select id, name, abbreviation, postal_code, street, street_number, 
city, phones, FORMAT(equaty_capitals, 'C') as equaty_capitals from foundations_with_phones 
inner join company on id = foundation_id;

create view university_v as select id, name, abbreviation, postal_code, street, street_number, 
city, phones, FORMAT(min_edu_budget, 'C') as min_edu_budget from foundations_with_phones 
inner join university on id = foundation_id;

create view research_center_v as select id, name, abbreviation, postal_code, street, street_number, 
city, phones, FORMAT(min_edu_budget, 'C') as min_edu_budget, FORMAT(private_budget, 'C') as private_budget 
from foundations_with_phones inner join research_center on id = foundation_id;