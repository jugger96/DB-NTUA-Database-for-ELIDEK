#!/usr/bin/env python
# coding: utf-8

# In[1]:


import faker
fake = faker.Faker()
import random
import numpy as np
import random
from datetime import datetime, date
from datetime import timedelta 


# In[2]:


DUMMY_DATA_NUMBER = 30;
TABLE_NAME = "foundation";
TABLE_COLUMNS = ["Name", "Abbreviation", "postal_code", "street", "street_number", "city"                  , "Foundation_Phone_1", "Foundation_Phone_2"]

content1 = "";

for _ in range(DUMMY_DATA_NUMBER):
    name = fake.company()
    abr = fake.company_suffix()
    pc = fake.postcode()
    stre = fake.street_name()
    strn = random.randint(1, 30)
    city = fake.city()
    fp1 = fake.bothify(text='210#######')
    fp2 = fake.bothify(text='210#######')
    content1 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{name}", "{abr}",     "{pc}", "{stre}", "{strn}", "{city}", "{fp1}", "{fp2}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content1)


# In[3]:


DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "Foundation_Extra_Phones";
TABLE_COLUMNS = ["Phone_Number", "Foundation_ID"]

content2 = "";

for _ in range(DUMMY_DATA_NUMBER):
    ph = fake.bothify(text='210#######')
    Fid = random.randint(1, 30)
    content2 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{ph}", "{Fid}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content2)


# In[4]:


l = []
fundings = []
for i in range(30):
    l.append(i+1)
    fundings.append(0)
random.shuffle(l)
fundings.append(0)


# In[5]:


DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "University";
TABLE_COLUMNS = ["Min_Edu_Budget", "Foundation_ID"]

content3 = "";


for i in range(DUMMY_DATA_NUMBER):
    budg = format(random.uniform(10**7, 10**8),".2f")
    Fid = l[i]
    fundings[Fid] = budg
    content3 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{budg}", "{Fid}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content3)


# In[6]:


DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "Company";
TABLE_COLUMNS = ["Equaty_Capitals", "Foundation_ID"]

content4 = "";

for i in range(DUMMY_DATA_NUMBER):
    budg = format(random.uniform(10**7, 10**8),".2f")
    Fid = l[i+10]
    fundings[Fid] = budg
    content4 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{budg}", "{Fid}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content4)


# In[7]:


DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "Research_Center";
TABLE_COLUMNS = ["Min_Edu_Budget", "Private_Budget", "Foundation_ID"]

content5 = "";

for i in range(DUMMY_DATA_NUMBER):
    budg = random.uniform(10**7, 10**8)
    n = random.randint(1, 10)
    budg1 = format(budg/n,".2f")
    budg2 = format(budg - budg/n,".2f")
    fundings[Fid] = budg1 + budg2
    Fid = l[i+20]
    content5 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{budg1}", "{budg2}", "{Fid}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content5)


# In[8]:


DUMMY_DATA_NUMBER = 300;
TABLE_NAME = "Researcher";
TABLE_COLUMNS = ["ID", "First_Name", "Last_Name", "Sex", "Birth_Date", "Foundation_ID", "Foundation_Date"]
ssns = []
start_date_res = []
content6 = "";
sex_ = ["male", "female"]
for i in range(DUMMY_DATA_NUMBER):
    n = random.randint(0,1)
    if n == 0:
        a = fake.ssn()
        ssns.append(a)
        rid = a
        first = fake.first_name_male()
        last = fake.last_name_male()
        sex = sex_[n]
        birth = fake.date_between_dates(date_start=datetime(1950,1,1), date_end=datetime(1992,1,1))
        Fid = random.randint(1, 30)
        Fdate = fake.date_between_dates(date_start=birth + timedelta(days=6570), date_end=datetime(2010,6,5))
        start_date_res.append(Fdate)
    if n == 1:
        a = fake.ssn()
        ssns.append(a)
        rid = a
        first = fake.first_name_female()
        last = fake.last_name_female()
        sex = sex_[n]
        birth = fake.date_between_dates(date_start=datetime(1950,1,1), date_end=datetime(1992,1,1))
        Fid = random.randint(1, 30)
        Fdate = fake.date_between_dates(date_start=birth + timedelta(days=6570), date_end=datetime(2010,6,5))
        start_date_res.append(Fdate)
    content6 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{rid}", "{first}", "{last}",    "{sex}", "{birth}", "{Fid}", "{Fdate}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content6)


# In[9]:


DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "Scientific_Field";
TABLE_COLUMNS = ["Name"]

content7 = "";
names = ["Mathematics", "Physical science", "Chemical sciences",         "Computer and information sciences", "Earth and related Environmental sciences", "Biological science",          "Economies and Business", "Electrical engineering", "Mechanical engineering", "Health Sciences"]

for i in range(DUMMY_DATA_NUMBER): 
    name = names[i]
    content7 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{name}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content7)


# In[10]:


DUMMY_DATA_NUMBER = 7;
TABLE_NAME = "Executive";
TABLE_COLUMNS = ["ID", "First_Name", "Last_Name"]

content8 = "";
ssns_executive = []
for i in range(DUMMY_DATA_NUMBER):
    n = random.randint(0,1)
    if n == 0:
        a = fake.ssn()
        while (a in ssns):
            a = fake.ssn()
        eid = a
        first = fake.first_name_male()
        last = fake.last_name_male()
        ssns_executive.append(a)
    if n == 1:
        a = fake.ssn()
        while (a in ssns):
            a = fake.ssn()
        eid = a
        first = fake.first_name_female()
        last = fake.last_name_female()
        ssns_executive.append(a)
    content8 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{eid}", "{first}", "{last}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content8)


# In[11]:


DUMMY_DATA_NUMBER = 10;
TABLE_NAME = "Program";
TABLE_COLUMNS = ["Name", "ELIDEK_Sector"]

content9 = "";
names_program = ["Aigaio", "Athens", "Megalos Peripatos",                 "CMOS research", "Data Base Development for ELIDEK", "Covid Hotel Data Base",                 "Covid Research", "Sofoklis", "Serious Games", "Artificial Intelligence"]
elidek = ["Health Sector", "Engineering Sector", "Humanitarian Sector"]

for i in range(DUMMY_DATA_NUMBER): 
    name = names_program[i]
    n = random.randint(0,2)
    el = elidek[n]
    content9 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{name}", "{el}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content9)


# In[12]:


DUMMY_DATA_NUMBER = 200;

TABLE_NAME = "Project";

TABLE_COLUMNS = ["Title", "Start_Date", "End_Date", "Summary", "Funding",                 "Executive_ID", "Program_ID", "Foundation_ID", "Researcher_ID_Boss",                 "Researcher_ID_Eval", "Evaluation_Date", "Evaluation_Grade", "Scientific_Field_Name"]

content10 = "";

dates_st = []
dates_en = []
titles = []
list_default_worker = []
list_evaluators = []
list_default_sfield = []
list_boss = []
kl = []

for i in range(200):
    a = fake.bs()
    while (a in titles):
        a = fake.bs()
    titles.append(a)
    
for i in range(DUMMY_DATA_NUMBER):
    title = titles[i]
    st_date = fake.date_between_dates(date_start=datetime(2012,1,1), date_end=datetime(2022,5,26))
    dates_st.append(st_date)
    en_date = fake.date_between_dates(date_start=st_date + timedelta(days=365), date_end=st_date + timedelta(days=4*365))
    dates_en.append(en_date)
    summ = fake.paragraph(nb_sentences=2)
    Fid = random.randint(1, 30)
    while Fid == 5 or Fid == 17:
        Fid = random.randint(1,30)
    fund = format(random.uniform(10**5, 10**6),".2f")
    ex = ssns_executive[random.randint(0, 6)]
    pid = random.randint(1, 10)
    y = random.sample(range(1, 300), 3)
    res_id_b = ssns[y[0]]
    
    #gets a default researcher so every project has some workers
    res_id_def = ssns[y[1]]
    list_default_worker.append(res_id_def)
    
    res_id_ev = ssns[y[2]]
    list_evaluators.append(ssns[y[2]])
    list_boss.append(res_id_b)
    ev_date = fake.date_between_dates(date_start=st_date - timedelta(days=365), date_end=st_date)
    ev_grade = random.randint(60, 100)
    sfn = names[random.randint(0, 9)]
    list_default_sfield.append(sfn)
    kl.append(str(i+1) + sfn)
    
    content10 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{title}", "{st_date}", "{en_date}",    "{summ}", "{fund}", "{ex}", "{pid}", "{Fid}", "{res_id_b}", "{res_id_ev}",    "{ev_date}", "{ev_grade}", "{sfn}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content10)


# In[13]:


DUMMY_DATA_NUMBER = 11;

TABLE_NAME = "Project";

TABLE_COLUMNS = ["Title", "Start_Date", "End_Date", "Summary", "Funding",                 "Executive_ID", "Program_ID", "Foundation_ID", "Researcher_ID_Boss",                 "Researcher_ID_Eval", "Evaluation_Date",                  "Evaluation_Grade", "Scientific_Field_Name"]

content20 = "";

for i in range(DUMMY_DATA_NUMBER):
    a = fake.bs()
    while (a in titles):
        a = fake.bs()
    titles.append(a)
    
for i in range(DUMMY_DATA_NUMBER):
    title = titles[i]
    st_date = fake.date_between_dates(date_start=datetime(2012,1,1), date_end=datetime(2012,12,31))
    dates_st.append(st_date)
    en_date = fake.date_between_dates(date_start=st_date + timedelta(days=365), date_end=st_date + timedelta(days=4*365))
    dates_en.append(en_date)
    summ = fake.paragraph(nb_sentences=2)
    Fid = 5
    fund = format(random.uniform(10**5, 10**6),".2f")
    ex = ssns_executive[random.randint(0, 6)]
    pid = random.randint(1, 10)
    y = random.sample(range(1, 300), 3)
    res_id_b = ssns[y[0]]
    res_id_def = ssns[y[1]]
    list_default_worker.append(res_id_def)
    res_id_ev = ssns[y[2]]
    list_evaluators.append(ssns[y[2]])
    list_boss.append(res_id_b)
    ev_date = fake.date_between_dates(date_start=st_date - timedelta(days=365), date_end=st_date)
    ev_grade = random.randint(60, 100)
    sfn = names[random.randint(0, 9)]
    list_default_sfield.append(sfn)
    kl.append(str(i+1) + sfn)
    
    content20 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{title}", "{st_date}", "{en_date}",    "{summ}", "{fund}", "{ex}", "{pid}", "{Fid}", "{res_id_b}", "{res_id_ev}",    "{ev_date}", "{ev_grade}", "{sfn}");\n'

with open(f"dummy_data_{TABLE_NAME}_A.txt", 'w') as f:
    f.write(content20)


# In[14]:


DUMMY_DATA_NUMBER = 11;

TABLE_NAME = "Project";

TABLE_COLUMNS = ["Title", "Start_Date", "End_Date", "Summary", "Funding",                 "Executive_ID", "Program_ID", "Foundation_ID", "Researcher_ID_Boss",                 "Researcher_ID_Eval", "Evaluation_Date",                  "Evaluation_Grade", "Scientific_Field_Name"]

content30 = "";

for i in range(DUMMY_DATA_NUMBER):
    a = fake.bs()
    while (a in titles):
        a = fake.bs()
    titles.append(a)
    
for i in range(DUMMY_DATA_NUMBER):
    title = titles[i]
    st_date = fake.date_between_dates(date_start=datetime(2013,1,1), date_end=datetime(2013,12,31))
    dates_st.append(st_date)
    en_date = fake.date_between_dates(date_start=st_date + timedelta(days=365), date_end=st_date + timedelta(days=4*365))
    dates_en.append(en_date)
    summ = fake.paragraph(nb_sentences=2)
    Fid = 5
    fund = format(random.uniform(10**5, 10**6),".2f")
    ex = ssns_executive[random.randint(0, 6)]
    pid = random.randint(1, 10)
    y = random.sample(range(1, 300), 3)
    res_id_b = ssns[y[0]]
    res_id_def = ssns[y[1]]
    list_default_worker.append(res_id_def)
    res_id_ev = ssns[y[2]]
    list_evaluators.append(ssns[y[2]])
    list_boss.append(res_id_b)
    ev_date = fake.date_between_dates(date_start=st_date - timedelta(days=365), date_end=st_date)
    ev_grade = random.randint(60, 100)
    sfn = names[random.randint(0, 9)]
    list_default_sfield.append(sfn)
    kl.append(str(i+1) + sfn)
    
    content30 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{title}", "{st_date}", "{en_date}",    "{summ}", "{fund}", "{ex}", "{pid}", "{Fid}", "{res_id_b}", "{res_id_ev}",    "{ev_date}", "{ev_grade}", "{sfn}");\n'

with open(f"dummy_data_{TABLE_NAME}_B.txt", 'w') as f:
    f.write(content30)


# In[15]:


DUMMY_DATA_NUMBER = 13;

TABLE_NAME = "Project";

TABLE_COLUMNS = ["Title", "Start_Date", "End_Date", "Summary", "Funding",                 "Executive_ID", "Program_ID", "Foundation_ID", "Researcher_ID_Boss",                 "Researcher_ID_Eval", "Evaluation_Date",                  "Evaluation_Grade", "Scientific_Field_Name"]

content40 = "";

for i in range(DUMMY_DATA_NUMBER):
    a = fake.bs()
    while (a in titles):
        a = fake.bs()
    titles.append(a)
    
for i in range(DUMMY_DATA_NUMBER):
    title = titles[i]
    st_date = fake.date_between_dates(date_start=datetime(2015,1,1), date_end=datetime(2015,12,31))
    dates_st.append(st_date)
    en_date = fake.date_between_dates(date_start=st_date + timedelta(days=365), date_end=st_date + timedelta(days=4*365))
    dates_en.append(en_date)
    summ = fake.paragraph(nb_sentences=2)
    Fid = 17
    fund = format(random.uniform(10**5, 10**6),".2f")
    ex = ssns_executive[random.randint(0, 6)]
    pid = random.randint(1, 10)
    y = random.sample(range(1, 300), 3)
    res_id_b = ssns[y[0]]
    res_id_def = ssns[y[1]]
    list_default_worker.append(res_id_def)
    res_id_ev = ssns[y[2]]
    list_evaluators.append(ssns[y[2]])
    list_boss.append(res_id_b)
    ev_date = fake.date_between_dates(date_start=st_date - timedelta(days=365), date_end=st_date)
    ev_grade = random.randint(60, 100)
    sfn = names[random.randint(0, 9)]
    list_default_sfield.append(sfn)
    kl.append(str(i+1) + sfn)
    
    content40 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{title}", "{st_date}", "{en_date}",    "{summ}", "{fund}", "{ex}", "{pid}", "{Fid}", "{res_id_b}", "{res_id_ev}",    "{ev_date}", "{ev_grade}", "{sfn}");\n'

with open(f"dummy_data_{TABLE_NAME}_C.txt", 'w') as f:
    f.write(content40)


# In[16]:


DUMMY_DATA_NUMBER = 13;

TABLE_NAME = "Project";

TABLE_COLUMNS = ["Title", "Start_Date", "End_Date", "Summary", "Funding",                 "Executive_ID", "Program_ID", "Foundation_ID", "Researcher_ID_Boss",                 "Researcher_ID_Eval", "Evaluation_Date",                  "Evaluation_Grade", "Scientific_Field_Name"]

content50 = "";

for i in range(DUMMY_DATA_NUMBER):
    a = fake.bs()
    while (a in titles):
        a = fake.bs()
    titles.append(a)
    
for i in range(DUMMY_DATA_NUMBER):
    title = titles[i]
    st_date = fake.date_between_dates(date_start=datetime(2016,1,1), date_end=datetime(2016,12,31))
    dates_st.append(st_date)
    en_date = fake.date_between_dates(date_start=st_date + timedelta(days=365), date_end=st_date + timedelta(days=4*365))
    dates_en.append(en_date)
    summ = fake.paragraph(nb_sentences=2)
    Fid = 17
    fund = format(random.uniform(10**5, 10**6),".2f")
    ex = ssns_executive[random.randint(0, 6)]
    pid = random.randint(1, 10)
    y = random.sample(range(1, 300), 3)
    res_id_b = ssns[y[0]]
    res_id_def = ssns[y[1]]
    list_default_worker.append(res_id_def)
    res_id_ev = ssns[y[2]]
    list_evaluators.append(ssns[y[2]])
    list_boss.append(res_id_b)
    ev_date = fake.date_between_dates(date_start=st_date - timedelta(days=365), date_end=st_date)
    ev_grade = random.randint(60, 100)
    sfn = names[random.randint(0, 9)]
    list_default_sfield.append(sfn)
    kl.append(str(i+1) + sfn)
    
    content50 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{title}", "{st_date}", "{en_date}",    "{summ}", "{fund}", "{ex}", "{pid}", "{Fid}", "{res_id_b}", "{res_id_ev}",    "{ev_date}", "{ev_grade}", "{sfn}");\n'

with open(f"dummy_data_{TABLE_NAME}_D.txt", 'w') as f:
    f.write(content50)


# In[17]:


DUMMY_DATA_NUMBER = 200;
TABLE_NAME = "Deliverable";
TABLE_COLUMNS = ["Title", "Summary", "Submission_Date", "Project_ID"]

content11 = "";
num_pid = []

for i in range(DUMMY_DATA_NUMBER):
    Pid = random.randint(1, 200)
    num_pid.append(Pid)
    count = num_pid.count(Pid)
    tit = "Report " + str(count)
    summ = fake.paragraph(nb_sentences=2)
    if dates_en[Pid-1] < date(2022,6,1):
        s_d = fake.date_between_dates(date_start=dates_st[Pid-1], date_end=dates_en[Pid-1])
    else:
        s_d = fake.date_between_dates(date_start=dates_st[Pid-1], date_end=datetime(2022,6,1))
    content11 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{tit}", "{summ}", "{s_d}", "{Pid}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content11)


# In[18]:


DUMMY_DATA_NUMBER = 1000;
TABLE_NAME = "Researcher_works_on_Project";
TABLE_COLUMNS = ["Researcher_ID", "Project_ID"]

content12 = "";

k = []

for i in range(200):
    Pid = i + 1
    Rid = list_default_worker[i]
    k.append(str(Pid) + Rid)
    content12 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{Rid}", "{Pid}");\n'
    
for i in range(DUMMY_DATA_NUMBER):
    Pid = random.randint(1,200)
    ran = random.randint(1,300)
    while (dates_st[Pid-1] < start_date_res[ran-1]) or (ssns[ran-1] == list_evaluators[Pid-1])            or (list_default_worker[Pid-1] == ssns[ran-1])or (ssns[ran-1] == list_boss[Pid-1])    or (str(Pid) + ssns[ran-1]) in k:
        ran = random.randint(1,300)
    Rid = ssns[ran-1]
    k.append(str(Pid) + Rid)
    content12 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{Rid}", "{Pid}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content12)


# In[19]:


DUMMY_DATA_NUMBER = 400;
TABLE_NAME = "Project_Scientific_Field";
TABLE_COLUMNS = ["Project_ID", "Scientific_Field_Name"]

content13 = "";


#for i in range(60):
#    Pid = i + 1
#    SF = list_default_sfield[i]
#    k.append(str(Pid) + SF)
#    content13 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{Pid}", "{SF}");\n'

for i in range(DUMMY_DATA_NUMBER):
    Pid = random.randint(1,200)
    ran = random.randint(1,10)
    while (str(Pid) + names[ran-1]) in kl:
        ran = random.randint(1,10)
        Pid = random.randint(1,200)
    SF = names[ran-1]
    kl.append(str(Pid) + names[ran-1])
    content13 += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{Pid}", "{SF}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content13)


# In[20]:


with open(f"dummy_data.txt", 'w') as f:
    f.write("-- Inserting data in foundation table" +'\n'  +'\n')
    f.write(content1)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Foundation_Extra_Phones table"+'\n'  +'\n')
    f.write(content2)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in University table"+'\n'  +'\n')
    f.write(content3)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Company table"+'\n'  +'\n')
    f.write(content4)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Research_Center table"+'\n'  +'\n')
    f.write(content5)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Researcher table"+'\n'  +'\n')
    f.write(content6)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Scientific_Field table"+'\n'  +'\n')
    f.write(content7)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Executive table"+'\n'  +'\n')
    f.write(content8)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Program table"+'\n'  +'\n')
    f.write(content9)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Project table"+'\n'  +'\n')
    f.write(content10)
    f.write(content20)
    f.write(content30)
    f.write(content40)
    f.write(content50)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Deliverable table"+'\n'  +'\n')
    f.write(content11)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Researcher_works_on_Project table"+'\n'  +'\n')
    f.write(content12)
    f.write('\n'  +'\n' + "-- ***************************************"+'\n'  +'\n')
    f.write("-- Inserting data in Project_Scientific_Field table"+'\n'  +'\n')
    f.write(content13)

# companies = ("African Telecommunications Union", "Asia-Pacific Telecommunity", "Caribbean Association of National Telecommunication Organizations",\
            "Regional Commonwealth in the Field of Communications", "Regional African Satellite Communications Organization", "International Satellite System for Search and Rescue", \
            "Arab States Broadcasting Union", "Asia Pacific Network Information Centre", "Asia-Pacific Broadcasting Union", \
             "Asociación Interamericana de Empresas de Telecomunicaciones", "Association for Progressive Communications", "Association of Andean Community Telecommunications Enterprises", \
             "Caribbean Broadcasting Union", "Centre for Environment and Development for the Arab Region and Europe", "Child Helpline International", \
             "Committee on Space Research", "Commonwealth ITU Group", "Communauté économique des Etats de l'Afrique centrale", \
             "Consumers International", "Digital Opportunity Trust", "Dominic Foundation", \
             "East African Communications Organization", "East African Community", "Eastern Caribbean Telecommunications Authority", \
             "Ecole Supérieure Multinationale des Télécommunications", "European Broadcasting Union", "European Radio Amateurs' Organization", \
             "FTTH Council Asia-Pacific", "Global Knowledge Partnership Foundation", "Global VSAT Forum Limited")