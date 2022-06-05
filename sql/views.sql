
-- -----------------------------------------------------
-- Views
-- -----------------------------------------------------

CREATE VIEW view32a AS
    (SELECT 
        res_id, first_name, last_name, Project_ID, title
    FROM
        (SELECT 
            *
        FROM
            researcher_works_on_project) a
            INNER JOIN
        (SELECT 
            r.id AS res_id, r.first_name, r.last_name
        FROM
            researcher r) b ON a.researcher_id = b.res_id
            INNER JOIN
        (SELECT 
            p.title, p.id
        FROM
            project p) d ON d.id = project_id
    ORDER BY res_id);

-- Query 3.3
CREATE VIEW view33 AS
    (SELECT 
        ps.scientific_field_name,
        ps.project_id,
        p.title,
        rw.researcher_id,
        r.first_name,
        r.last_name,
        p.end_date
    FROM
        (project_scientific_field ps
        INNER JOIN project p ON p.id = ps.project_id
        INNER JOIN researcher_works_on_project rw ON rw.project_id = ps.project_id
        INNER JOIN researcher r ON r.id = rw.researcher_id)
    WHERE
        p.end_date > CURDATE());


CREATE VIEW view34 AS
    (SELECT 
        *
    FROM
        (SELECT 
            *
        FROM
            (SELECT 
            COUNT(*) AS number1,
                YEAR(p.start_date) AS year1,
                f.id AS f_id1,
                f.name AS name1
        FROM
            project p
        INNER JOIN foundation f ON p.foundation_id = f.id
        GROUP BY year1 , f_id1) g
        WHERE
            g.number1 > 9) k
            INNER JOIN
        (SELECT 
            *
        FROM
            (SELECT 
            COUNT(*) AS number2,
                YEAR(p.start_date) AS year2,
                f.id AS f_id2,
                f.name AS name2
        FROM
            project p
        INNER JOIN foundation f ON p.foundation_id = f.id
        GROUP BY year2 , f_id2) l
        WHERE
            l.number2 > 9) b ON k.f_id1 = b.f_id2
            AND k.year1 = b.year2 + 1
            AND k.number1 = b.number2);


-- Query 3.5
CREATE VIEW view35 AS
    (SELECT 
        ps1.Scientific_Field_Name AS sf1,
        ps2.Scientific_Field_Name AS sf2,
        COUNT(*) AS count
    FROM
        project_scientific_field ps1
            INNER JOIN
        project_scientific_field ps2 ON ps1.Project_ID = ps2.Project_ID
            AND ps1.Scientific_Field_Name > ps2.Scientific_Field_Name
    GROUP BY ps1.Scientific_Field_Name , ps2.Scientific_Field_Name
    ORDER BY count DESC
    LIMIT 3);


-- Query 3.7
CREATE VIEW view37 AS
    (SELECT 
        executive_ID,
        first_name,
        last_name,
        name AS Company_Name,
        ta.id AS company_id,
        SUM(funding) AS total_funding
    FROM
        (SELECT 
            p.funding, p.executive_id, p.foundation_id
        FROM
            project p) te
            INNER JOIN
        (SELECT 
            f.name, f.id
        FROM
            foundation f
        WHERE
            f.id IN (SELECT 
                    c.foundation_id
                FROM
                    company c)) ta ON te.foundation_id = ta.id
            INNER JOIN
        executive e ON e.id = te.executive_id
    GROUP BY executive_id , company_id
    ORDER BY total_funding DESC
    LIMIT 5);

-- Query 3.6
CREATE VIEW view36 AS
    (SELECT 
        id, first_name, last_name, COUNT(*) AS projects
    FROM
        (SELECT 
            *
        FROM
            (SELECT 
            r.id, r.first_name, r.last_name, r.birth_date
        FROM
            researcher r
        WHERE
            DATEDIFF(CURDATE(), birth_date) < 14600) te
        INNER JOIN researcher_works_on_project rp ON te.id = rp.researcher_id) ta
            INNER JOIN
        (SELECT 
            p.id AS project_id, p.end_date
        FROM
            project p
        WHERE
            p.end_date > CURDATE()) tb ON tb.project_id = ta.project_id
    GROUP BY id
    ORDER BY projects DESC , last_name
    LIMIT 5);


-- Query 3.8
CREATE VIEW view38 AS
    (SELECT 
        *
    FROM
        (SELECT 
            project_id,
                researcher_id,
                first_name,
                last_name,
                COUNT(*) AS total_projects
        FROM
            (SELECT 
            *
        FROM
            (SELECT 
            p.id
        FROM
            project p
        WHERE
            p.id NOT IN (SELECT 
                    d.project_id
                FROM
                    deliverable d)) te
        INNER JOIN researcher_works_on_project rp ON rp.project_id = te.id) ta
        INNER JOIN (SELECT 
            first_name, last_name, id AS res_id
        FROM
            researcher) r ON r.res_id = ta.researcher_id
        GROUP BY ta.researcher_id) tt
    WHERE
        total_projects > 4
    ORDER BY total_projects DESC , last_name);

CREATE VIEW foundations_with_phones AS
    SELECT 
        id,
        name,
        abbreviation,
        postal_code,
        street,
        street_number,
        city,
        GROUP_CONCAT(phone_number
            SEPARATOR ', ') AS phones
    FROM
        foundation f
            INNER JOIN
        foundation_extra_phones p ON f.id = p.foundation_id
    GROUP BY id;

CREATE VIEW company_v AS
    SELECT 
        id,
        name,
        abbreviation,
        postal_code,
        street,
        street_number,
        city,
        phones,
        FORMAT(equaty_capitals, 'C') AS equaty_capitals
    FROM
        foundations_with_phones
            INNER JOIN
        company ON id = foundation_id;

CREATE VIEW university_v AS
    SELECT 
        id,
        name,
        abbreviation,
        postal_code,
        street,
        street_number,
        city,
        phones,
        FORMAT(min_edu_budget, 'C') AS min_edu_budget
    FROM
        foundations_with_phones
            INNER JOIN
        university ON id = foundation_id;

CREATE VIEW research_center_v AS
    SELECT 
        id,
        name,
        abbreviation,
        postal_code,
        street,
        street_number,
        city,
        phones,
        FORMAT(min_edu_budget, 'C') AS min_edu_budget,
        FORMAT(private_budget, 'C') AS private_budget
    FROM
        foundations_with_phones
            INNER JOIN
        research_center ON id = foundation_id;
        
CREATE VIEW workers AS
    SELECT 
        project_id, first_name, last_name, researcher_id
    FROM
        (SELECT 
            project_id, researcher_id
        FROM
            (SELECT 
            id, title
        FROM
            project) p
        INNER JOIN researcher_works_on_project rw ON rw.project_id = p.id) a
            INNER JOIN
        (SELECT 
            first_name, last_name, id
        FROM
            researcher) b ON a.researcher_id = b.id;