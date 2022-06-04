delimiter $$
create trigger phone_check_update before update on foundation_extra_phones
for each row
begin
	if exists (select * from foundation f where ((f.Foundation_Phone_1 = new.phone_number) or (f.Foundation_Phone_2 = new.phone_number)))
then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Overlap found!';
    END IF;
end; 
$$

delimiter $$
create trigger researchers_dates_update before update on researcher
for each row
begin
	if (new.birth_date < '1920-1-1')
    then SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The researcher seems to be too old!';
    end if;
    if (new.birth_date > '2020-1-1')
    then SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The researcher seems to be an infant!';
    end if;
    if ((timestampdiff(year, new.birth_date, new.foundation_date)) < 12)
    then SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The researcher seems to be too young for this foundation!';
    END IF;
    -- INSERT into researcher (age) values (timestampdiff(year, new.foundation_date, new.birth_date));
end;
$$

delimiter $$
create trigger legitimate_worker_update before update on researcher_works_on_project
for each row
begin
	if exists (select * from project p where ((p.id = new.project_id) and (p.Researcher_ID_eval = new.researcher_id)))
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'This researcher can`t work for this project because he is the evaluator';
    END IF;
    
    if exists (select * from researcher r, project p where ((r.ID = new.researcher_id) and (p.id = new.project_id) 
					and (r.Foundation_Date > p.end_date)))
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'The researcher isn`t working for any foundation during the the project';
    END IF;
end; 
$$


delimiter $$
create trigger project_parameters_update before update on project
for each row
begin

	if new.evaluation_grade >= 100 or new.evaluation_grade < 59
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Grade must be between 60 and 100 points';
    END IF;
    
	if new.Researcher_ID_eval = new.researcher_id_default
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'This researcher can`t work for this project because he is the evaluator';
    END IF;
    
    if new.Researcher_ID_eval = new.researcher_id_boss
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'This researcher can`t manage this project because he is the evaluator';
    END IF;
    
    if new.Researcher_ID_default = new.researcher_id_boss
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'The manager can`t also work for the project';
    END IF;
    
    if new.start_date > new.end_date
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Start Date can`t be after end date';
    END IF;
    
    if ((timestampdiff(year, new.start_date, new.end_date)) < 1)
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Minimum duration is 1 year';
    END IF;
    
    if ((timestampdiff(year, new.start_date, new.end_date)) > 4)
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Maximum duration is 4 years';
    END IF;
    
    if (new.funding > 1000000 or new.funding < 100000)
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Funding must be between 100k and 1M Euros';
    END IF;
    
    if new.evaluation_date > new.start_date
    then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Evaluation date must be before the start of the project';
    END IF;
    
    if exists (select * from researcher r where ((r.ID = new.researcher_id_boss) and r.Foundation_Date > new.end_date))
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'The manager isn`t working for any foundation during the project';
    END IF;
    
    if exists (select * from researcher r where ((r.ID = new.researcher_id_eval) and r.Foundation_Date > new.evaluation_date))
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'The evaluator isn`t working for any foundation at the moment of the evaluation of the the project';
    END IF;
    
    if exists (select * from researcher r where ((r.ID = new.Researcher_ID_Default) and r.Foundation_Date > new.end_date))
	then 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'The fisrst worker isn`t working for any foundation during the the project';
    END IF;
end; 
$$