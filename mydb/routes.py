from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from dbdemo import app, db ## initially created by __init__.py, need to be used here
from dbdemo.forms import StudentForm, ResForm, CreResForm, ProjForm, SciForm, WorksForm, \
                        CompanyForm, CreCompanyForm, UniversityForm,CreUniversityForm,\
                        CreRCForm,RCForm, PhoneForm, programForm, deliverableForm, \
                        CredeliverableForm, CreExForm, ExForm, psfForm, UpProjForm, CreProjForm, project_worker
from datetime import date, datetime

@app.route("/")
def index():
    try:
        ## create connection to database
        cur = db.connection.cursor()
        ## execute query
        cur.execute("select * from view34;")
        ## cursor.fetchone() does not return the column names, only the row values
        ## thus we manually create a mapping between the two, the dictionary res
        #column_names = [i[0] for i in cur.description]
        good_fou = [entry for entry in cur.fetchall()]
        string1 = ''
        i = 0
        for fou in good_fou:
            i += 1
            name = fou[3]
            fou_id = str(fou[2])
            string1 += "'" + name + "'" + ' (ID: ' + fou_id + ')'
            if len(good_fou) > i:
                string1 += ', '

        cur.execute("select * from view35;")
        ## cursor.fetchone() does not return the column names, only the row values
        ## thus we manually create a mapping between the two, the dictionary res
        #column_names = [i[0] for i in cur.description]
        combos = [entry for entry in cur.fetchall()]
        string2 = " '" + combos[0][0] + "' and '" + combos[0][1] + "'"
        string3 = " '" + combos[1][0] + "' and '" + combos[1][1] + "'"
        string4 = " '" + combos[2][0] + "' and '" + combos[2][1] + "'"

        cur.execute("select * from view37;")
        ## cursor.fetchone() does not return the column names, only the row values
        ## thus we manually create a mapping between the two, the dictionary res
        #column_names = [i[0] for i in cur.description]
        tops = [entry for entry in cur.fetchall()]

        string5 = ' ' + tops[0][1] + ' ' + tops[0][2] + " gave to Company '" + tops[0][3] + "' " + str("${:,.2f}".format(tops[0][5])) + " total fundings"
        string6 = ' ' + tops[1][1] + ' ' + tops[1][2] + " gave to Company '" + tops[1][3] + "' " + str("${:,.2f}".format(tops[1][5])) + " total fundings"
        string7 = ' ' + tops[2][1] + ' ' + tops[2][2] + " gave to Company '" + tops[2][3] + "' " + str("${:,.2f}".format(tops[2][5])) + " total fundings"
        string8 = ' ' + tops[3][1] + ' ' + tops[3][2] + " gave to Company '" + tops[3][3] + "' " + str("${:,.2f}".format(tops[3][5])) + " total fundings"
        string9 = ' ' + tops[4][1] + ' ' + tops[4][2] + " gave to Company '" + tops[4][3] + "' " + str("${:,.2f}".format(tops[4][5])) + " total fundings"

        cur.execute("select * from view36;")
        
        topys = [entry for entry in cur.fetchall()]

        string10 = ' ' + topys[0][1] + ' ' + topys[0][2] + " works on " + str(topys[0][3]) + " active projects"
        string11 = ' ' + topys[1][1] + ' ' + topys[1][2] + " works on " + str(topys[1][3]) + " active projects"
        string12 = ' ' + topys[2][1] + ' ' + topys[2][2] + " works on " + str(topys[2][3]) + " active projects"
        string13 = ' ' + topys[3][1] + ' ' + topys[3][2] + " works on " + str(topys[3][3]) + " active projects"
        string14 = ' ' + topys[4][1] + ' ' + topys[4][2] + " works on " + str(topys[4][3]) + " active projects"


        cur.close()

        return render_template("landing.html",
                               pageTitle = "Landing Page",
                               string1 = string1, string2 = string2, string3 = string3, string4 = string4,
                               string5 = string5, string6 = string6, string7 = string7, string8 = string8,
                               string9 = string9, string10 = string10, string11 = string11, string12 = string12,
                               string13 = string13, string14 = string14)
    except Exception as e:
        print(e)
        return render_template("landing.html", pageTitle = "Landing Page")

@app.route("/project", methods = ["GET", "POST"])
def getProject():
    """
    Retrieve projectss from database
    """

    if request.method == "POST":
        try:
            form = ProjForm()
            cur = db.connection.cursor()
            date = request.form["date"]
            dur = request.form["dur"]
            exec_id = request.form["exec_id"]
            print(date, dur, exec_id)
            if (date == '' and dur == '' and exec_id == ''):
                query = "SELECT * FROM project where id = 0"
            elif (date == '' and dur == ''):
                query = "SELECT * FROM project where executive_id = '{}'".format(exec_id)
            elif (exec_id == '' and dur == ''):
                query = "SELECT * FROM project where start_date > '{}'".format(date)
            elif (date == '' and exec_id == ''):
                dur = float(dur) * 365
                query = "SELECT * FROM project where datediff(end_date, start_date) < {}".format(dur)
            elif (date == ''):
                dur = float(dur) * 365
                query = "SELECT * FROM project where executive_id = '{}' and datediff(end_date, start_date) < {}".format(exec_id, dur)
            elif (dur == ''):
                query = "SELECT * FROM project where executive_id = '{}' and start_date > '{}'".format(exec_id, date)
            elif (exec_id == ''):
                dur = float(dur) * 365
                query = "SELECT * FROM project where datediff(end_date, start_date) < {} and start_date > '{}'".format(dur, date)
            else:
                dur = float(dur) * 365
                query = "SELECT * FROM project where datediff(end_date, start_date) < {} \
                        and start_date > '{}' and executive_id = '{}'".format(dur, date, exec_id)
            #query = "SELECT * FROM project where id = '{}'".format(date)
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            project = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()
            return render_template("project.html", project = project, pageTitle = "Projects Page", form = form)
        except Exception as e:
            ## if the connection to the database fails, return HTTP response 500
            flash(str(e), "danger")
            abort(500)
        
    else:
        try:
            form = ProjForm()
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM project")
            column_names = [i[0] for i in cur.description]
            project = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
            cur.close()
            return render_template("project.html", project = project, pageTitle = "Projects Page", form = form)
        except Exception as e:
            ## if the connection to the database fails, return HTTP response 500
            flash(str(e), "danger")
            abort(500)

@app.route("/project/update/<string:projectID>", methods = ["POST"])
def updateproject(projectID):
    
    """
    Update a project in the database, by id
    """
    
    form = UpProjForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE project SET title = '{}', start_date = '{}', end_date = '{}', summary = '{}',\
             funding = '{}', executive_id = '{}', program_id = '{}', foundation_id = '{}', researcher_id_boss = '{}',\
             researcher_id_eval = '{}', evaluation_date = '{}', evaluation_grade = '{}' WHERE id = '{}';".\
             format(updateData['Title'].data, updateData['Start_Date'].data, updateData['End_Date'].data,\
                    updateData['Summary'].data, updateData['Funding'].data, updateData['Executive_ID'].data, \
                    updateData['Program_ID'].data, updateData['Foundation_ID'].data, updateData['Researcher_ID_Boss'].data,\
                    updateData['Researcher_ID_eval'].data, updateData['Evaluation_Date'].data,\
                    updateData['Evaluation_Grade'].data, projectID)
        print(query)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Project updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getProject"))

@app.route("/project/delete/<string:projectID>", methods = ["POST"])
def deleteproject(projectID):
    
    """
    Delete project by id from database
    """
    query = f"DELETE FROM project WHERE id = '{projectID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Project deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getProject"))

@app.route("/project/create", methods = ["GET", "POST"]) ## "GET" by default
def createproject():
    """
    Create new project in the database
    """
    form = CreProjForm()
    #Info for the Drop Down Lists.
    cur = db.connection.cursor()
    cur.execute("select id, name from foundation;")
    ###################################################################
    column_names = [i[0] for i in cur.description]
    fids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.execute("select id, name from program;")
    column_names = [i[0] for i in cur.description]
    progs = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.execute("select id, first_name, last_name from researcher;")
    column_names = [i[0] for i in cur.description]
    ress = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.execute("select * from scientific_field;")
    column_names = [i[0] for i in cur.description]
    sci = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.execute("select * from executive;")
    column_names = [i[0] for i in cur.description]
    exec = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.close()

    ## when the form is submitted

    if(request.method == "POST" and form.validate_on_submit()):
        newproject = form.__dict__
        query = "INSERT INTO project (title, start_date, end_date, summary, funding, executive_id, program_id,\
                foundation_id, researcher_id_boss, researcher_id_eval, evaluation_date, evaluation_grade, \
                scientific_field_name)\
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"\
                 .format(newproject['Title'].data, \
                 newproject['Start_Date'].data, newproject['End_Date'].data, \
                 newproject['Summary'].data, newproject['Funding'].data,\
                 newproject['Executive_ID'].data, newproject['Program_ID'].data,\
                 newproject['Foundation_ID'].data, newproject['Researcher_ID_Boss'].data,\
                 newproject['Researcher_ID_eval'].data, newproject['Evaluation_Date'].data,\
                 newproject['Evaluation_Grade'].data, newproject['Scientific_Field_Name'].data)
        T = 0
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            T = 1
        except Exception as e: ## OperationalError
            flash(str(e), "danger")
        if T == 1:
            try:
                query = "SELECT * FROM project ORDER BY ID DESC limit 1;"
                cur = db.connection.cursor()
                cur.execute(query)
                db.connection.commit()
                column_names = [i[0] for i in cur.description]
                IDD = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
                aa = IDD[0]['ID']
                cur.close()
                flash("Project inserted successfully", "success")
                url = "/project/create/workers/" + str(aa)
                return redirect(url)
            except Exception as e: ## OperationalError
                flash(str(e), "danger")
        

    ## else, response for GET request
    return render_template("project_create.html", pageTitle = "Create Project", form = form, fids = fids\
                                                                              , progs = progs, ress = ress\
                                                                              , exec = exec, sci = sci)

@app.route("/project/create/workers/<string:projectID>", methods = ["GET", "POST"]) ## "GET" by default
def createproject_worker(projectID):
    """
    Create Worker for a new Project
    """
    cur = db.connection.cursor()
    form = project_worker()
    ## when the form is submitted
    cur.execute("select id, first_name, last_name from researcher;")
    column_names = [i[0] for i in cur.description]
    ress = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.close()

    if(request.method == "POST" and form.validate_on_submit()):
        worker = form.__dict__
        query = "INSERT INTO researcher_works_on_project (project_id, researcher_id) VALUES ('{}', '{}');"\
                .format(projectID, worker['researcher_id'].data)
        print(query)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Researcher asigned successfully to this project", "success")
            return redirect(url_for(createproject_worker))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("project_worker.html", pageTitle = "Assign Researchers to new Project", form = form, ress = ress)

@app.route("/project/<string:project_ID>", methods = ["POST"])
def getproject_worker(project_ID):
    print
    """
    View who works on specific project
    """
    try:
        cur = db.connection.cursor()        
        query = f"select * from workers where project_id = '{project_ID}';"
        cur.execute(query)
        message = "Here is everyone that works on project " + project_ID
        flash(message, "primary")
        column_names = [i[0] for i in cur.description]
        worker = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("project_worker_view.html", worker = worker, pageTitle = "Workers Page")
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/researcher")
def getResearcher():
    """
    Retrieve researchers from database
    """
    try:
        form = ResForm()
        cur = db.connection.cursor()
        cur.execute("select * from researcher;")
        column_names = [i[0] for i in cur.description]
        researcher = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("researcher.html", researcher = researcher,
                                pageTitle = "Researchers Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/researcher/create", methods = ["GET", "POST"]) ## "GET" by default
def createRes():
    """
    Create new student in the database
    """
    form = CreResForm()
           
    cur = db.connection.cursor()
    cur.execute("select id, name from foundation;")
    column_names = [i[0] for i in cur.description]
    fids = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    cur.close()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newResearcher = form.__dict__
        query = "INSERT INTO researcher(id, first_name, last_name, sex, birth_date, foundation_id, foundation_date)\
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(newResearcher['ID'].data, \
                 newResearcher['First_Name'].data, newResearcher['Last_Name'].data, \
                 newResearcher['Sex'].data, newResearcher['Birth_Date'].data,\
                 newResearcher['Foundation_ID'].data, newResearcher['Foundation_Date'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Researcher inserted successfully", "success")
            return redirect(url_for("getResearcher"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("researcher_create.html", pageTitle = "Create Researcher", form = form, fids = fids)

@app.route("/researcher/update/<string:researcherID>", methods = ["POST"])
def updateresearcher(researcherID):
    
    """
    Update a researcher in the database, by id
    """
    
    form = ResForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE researcher SET first_name = '{}', last_name = '{}', sex = '{}', birth_date = '{}',\
             foundation_id = '{}', foundation_date = '{}' WHERE id = '{}';".format(updateData['First_Name'].data,\
             updateData['Last_Name'].data,\
             updateData['Sex'].data, updateData['Birth_Date'].data, updateData['Foundation_ID'].data,\
             updateData['Foundation_Date'].data, researcherID)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Researcher updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getResearcher"))

@app.route("/researcher/delete/<string:researcherID>", methods = ["POST"])
def deleteResearcher(researcherID):
    """
    Delete student by id from database
    """
    query = f"DELETE FROM researcher WHERE id = '{researcherID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Researcher deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getResearcher"))

@app.route("/researcher/Query38")
def getres38():
    """
    Retrieve scientific fields from database
    """
    try:
        cur = db.connection.cursor()
        query = "select * from view38;"
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        res38 = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("researcher_Query38.html", res38 = res38, pageTitle = "Researchers from Query 3.8")
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/workers")
def getworkers():
    """
    Retrieve researchers_works_on_project from database
    """
    try:
        form = WorksForm()
        cur = db.connection.cursor()
        cur.execute("select * from view32a;")
        column_names = [i[0] for i in cur.description]
        workers = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("workers.html", workers = workers,
                                pageTitle = "Workers Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/workers/delete/<string:researcherID>/<string:projectID>", methods = ["POST"])
def deleteWorker(researcherID, projectID):
    """
    Delete student by id from database
    """
    query = f"DELETE FROM researcher_works_on_project WHERE researcher_id = '{researcherID}'\
             and project_id = '{projectID}';"
    try:
        cur = db.connection.cursor()
        print(query)
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Work relation deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getworkers"))

@app.route("/workers/create", methods = ["GET", "POST"]) ## "GET" by default
def createworker():
    """
    Create new Researcher-Project working Relation in the database
    """
    form = WorksForm()
    #Info for the Drop Down Lists.
    cur = db.connection.cursor()
    ###################################################################
    cur.execute("select id,Title from project;")
    column_names = [i[0] for i in cur.description]
    pr = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.execute("select id, first_name, last_name from researcher;")
    column_names = [i[0] for i in cur.description]
    rey = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.close()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newworker = form.__dict__
        query = "INSERT INTO researcher_works_on_project(researcher_id, project_id)\
             VALUES ('{}', '{}');".format(newworker['Researcher_ID'].data, \
                 newworker['Project_ID'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Work Relation inserted successfully", "success")
            return redirect(url_for("getworkers"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("worker_create.html", pageTitle = "Create Work Relation", form = form, pr = pr, rey = rey)

@app.route("/scifi")
def getscifi():
    """
    Retrieve scientific fields from database
    """
    try:
        form = SciForm()
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM scientific_field")
        column_names = [i[0] for i in cur.description]
        scifi = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("scifi.html", scifi = scifi, pageTitle = "Scientific Fields Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/scifi/update/<string:Name1>", methods = ["POST"])
def updatescifi(Name1):
    
    """
    Update a researcher in the database, by id
    """
    print(Name1)
    Name1 = Name1.replace("%20", " ")
    form = SciForm()
    updateData = form.__dict__
    #if(form.validate_on_submit()):
    query = "UPDATE scientific_field SET name = '{}' WHERE name = '{}';".format(updateData['Name'].data, Name1)
    print(query)
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Scientific Field updated successfully", "success")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getscifi"))

@app.route("/scifi/create", methods = ["GET", "POST"]) ## "GET" by default
def createscifi():
    """
    Create new Scientific Field in the database
    """
    form = SciForm()
    print("beep")
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newscifi = form.__dict__
        query = "INSERT INTO scientific_field(name) VALUES ('{}');".format(newscifi['Name'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Scientific Field inserted successfully", "success")
            return redirect(url_for("getscifi"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("scifi_create.html", pageTitle = "Create Scientific Field", form = form)

@app.route("/scifi/<string:Name1>", methods = ["POST"])
def infoscifi(Name1):
    print
    """
    Querry 3.3
    """
    Name1 = Name1.replace("%20", " ")
    try:
        cur = db.connection.cursor()        
        query = f"select * from view33 where scientific_field_name = '{Name1}';"
        #print(cur.description)
        cur.execute(query)
        message = "You want it? I got it! Here is everything about " + Name1
        flash(message, "primary")
        column_names = [i[0] for i in cur.description]
        scifi = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("scifi_info.html", scifi = scifi, pageTitle = "Magic Scientific Fields Page")
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/company")
def getcompany():
    """
    Retrieve company from database
    """
    try:
        form = CompanyForm()
        cur = db.connection.cursor()
        cur.execute("select * from company_v;")
        column_names = [i[0] for i in cur.description]
        company = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("company.html", company = company,
                                pageTitle = "Companies Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/company/update/<string:companyID>", methods = ["POST"])
def updateCompany(companyID):
    
    """
    Update a company in the database, by id
    """
    
    form = CompanyForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query1 = "UPDATE foundation SET name = '{}', abbreviation = '{}', postal_code = '{}', street = '{}',\
             street_number = '{}', city = '{}' WHERE id = '{}';".format(updateData['name'].data,\
             updateData['abbreviation'].data,\
             updateData['postal_code'].data, updateData['street'].data, updateData['street_number'].data,\
             updateData['city'].data, companyID)
        print(query1)
        query2 = "UPDATE company SET equaty_capitals = '{}' WHERE foundation_id = '{}';".\
                format(updateData['equaty_capitals'].data, companyID)
        print(query2)
        try:
            cur = db.connection.cursor()
            cur.execute(query1)
            cur.execute(query2)
            db.connection.commit()
            cur.close()
            flash("Company updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getcompany"))

@app.route("/company/delete/<string:companyID>", methods = ["POST"])
def deleteCompany(companyID):
    """
    Delete company by id from database
    """
    query = f"DELETE FROM foundation WHERE id = '{companyID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Company deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getcompany"))

@app.route("/company/create", methods = ["GET", "POST"]) ## "GET" by default
def createcompany():
    """
    Create new company in the database
    """
    form = CreCompanyForm()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newcompany = form.__dict__
        query1 = "INSERT INTO foundation (name, abbreviation, postal_code, street,\
             street_number, city, Foundation_phone_1, Foundation_phone_2)\
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".\
                 format(newcompany['name'].data, newcompany['abbreviation'].data,\
                        newcompany['postal_code'].data, newcompany['street'].data,\
                        newcompany['street_number'].data, newcompany['city'].data,\
                        newcompany['phone1'].data, newcompany['phone2'].data)
        T = 0
        try:
            cur = db.connection.cursor()
            cur.execute(query1)
            db.connection.commit()
            cur.close()
        except Exception as e: ## OperationalError
            flash(str(e), "danger")
            T = 1
        if T == 0:
            try:
                cur = db.connection.cursor()
                query4 = "select id from foundation where foundation_phone_1 = {};".format(newcompany['phone1'].data)
                cur.execute(query4)
                column_names = [i[0] for i in cur.description]
                IDD = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
                aa = IDD[0]['id']
                cur.close()
            except Exception as e: ## OperationalError
                flash(str(e), "danger")
        
            try:
                cur = db.connection.cursor()
                query2 = "INSERT INTO company (equaty_capitals, foundation_id)\
                 VALUES ('{}', {});".format(newcompany['equaty_capitals'].data, aa)
                cur.execute(query2)
                db.connection.commit()
                cur.close()
                flash("Company inserted successfully", "success")
                return redirect(url_for("getcompany"))
            except Exception as e: ## OperationalError
                flash(str(e), "danger")

    ## else, response for GET request
    return render_template("company_create.html", pageTitle = "Create Researcher", form = form)

@app.route("/<string:foundation>/phone/<string:companyID>", methods = ["GET", "POST"]) ## "GET" by default
def createphone(companyID, foundation):
    """
    Create new Scientific Field in the database
    """
    form = PhoneForm()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newphone = form.__dict__
        query = "INSERT INTO foundation_extra_phones (foundation_id, phone_number) VALUES ('{}', '{}');"\
                .format(companyID, newphone['phone'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Phone inserted successfully", "success")
            string = "get" + foundation
            return redirect(url_for(string))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("phone_create.html", pageTitle = "Create Phone", form = form)

@app.route("/university")
def getuniversity():
    """
    Retrieve university from database
    """
    try:
        form = UniversityForm()
        cur = db.connection.cursor()
        cur.execute("select * from university_v;")
        column_names = [i[0] for i in cur.description]
        university = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("university.html", university = university,
                                pageTitle = "Universities Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/university/update/<string:companyID>", methods = ["POST"])
def updateuniversity(companyID):
    
    """
    Update a company in the database, by id
    """
    
    form = UniversityForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query1 = "UPDATE foundation SET name = '{}', abbreviation = '{}', postal_code = '{}', street = '{}',\
             street_number = '{}', city = '{}' WHERE id = '{}';".format(updateData['name'].data,\
             updateData['abbreviation'].data,\
             updateData['postal_code'].data, updateData['street'].data, updateData['street_number'].data,\
             updateData['city'].data, companyID)
        print(query1)
        query2 = "UPDATE university SET min_edu_budget = '{}' WHERE foundation_id = '{}';".\
                format(updateData['min_edu_budget'].data, companyID)
        print(query2)
        try:
            cur = db.connection.cursor()
            cur.execute(query1)
            cur.execute(query2)
            db.connection.commit()
            cur.close()
            flash("University updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getuniversity"))

@app.route("/university/delete/<string:companyID>", methods = ["POST"])
def deleteuniversity(companyID):
    """
    Delete university by id from database
    """
    query = f"DELETE FROM foundation WHERE id = '{companyID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("University deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getuniversity"))

@app.route("/university/create", methods = ["GET", "POST"]) ## "GET" by default
def createuniversity():
    """
    Create new company in the database
    """
    form = CreUniversityForm()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newcompany = form.__dict__
        query1 = "INSERT INTO foundation (name, abbreviation, postal_code, street,\
             street_number, city, Foundation_phone_1, Foundation_phone_2)\
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".\
                 format(newcompany['name'].data, newcompany['abbreviation'].data,\
                        newcompany['postal_code'].data, newcompany['street'].data,\
                        newcompany['street_number'].data, newcompany['city'].data,\
                        newcompany['phone1'].data, newcompany['phone2'].data)
        T = 0
        try:
            cur = db.connection.cursor()
            cur.execute(query1)
            db.connection.commit()
            cur.close()
        except Exception as e: ## OperationalError
            flash(str(e), "danger")
            T = 1
        if T == 0:
            try:
                cur = db.connection.cursor()
                query4 = "select id from foundation where foundation_phone_1 = {};".format(newcompany['phone1'].data)
                cur.execute(query4)
                column_names = [i[0] for i in cur.description]
                IDD = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
                aa = IDD[0]['id']
                cur.close()
            except Exception as e: ## OperationalError
                flash(str(e), "danger")
        
            try:
                cur = db.connection.cursor()
                query2 = "INSERT INTO university (min_edu_budget, foundation_id)\
                 VALUES ('{}', {});".format(newcompany['min_edu_budget'].data, aa)
                cur.execute(query2)
                db.connection.commit()
                cur.close()
                flash("University inserted successfully", "success")
                return redirect(url_for("getuniversity"))
            except Exception as e: ## OperationalError
                flash(str(e), "danger")

    ## else, response for GET request
    return render_template("university_create.html", pageTitle = "Create University", form = form)

@app.route("/research_center")
def getresearch_center():
    """
    Retrieve research_center from database
    """
    try:
        form = RCForm()
        cur = db.connection.cursor()
        cur.execute("select * from research_center_v;")
        column_names = [i[0] for i in cur.description]
        research_center = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("research_center.html", research_center = research_center,
                                pageTitle = "Research Centers Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/research_center/update/<string:companyID>", methods = ["POST"])
def updateresearch_center(companyID):
    
    """
    Update a research_center in the database, by id
    """
    
    form = RCForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query1 = "UPDATE foundation SET name = '{}', abbreviation = '{}', postal_code = '{}', street = '{}',\
             street_number = '{}', city = '{}' WHERE id = '{}';".format(updateData['name'].data,\
             updateData['abbreviation'].data,\
             updateData['postal_code'].data, updateData['street'].data, updateData['street_number'].data,\
             updateData['city'].data, companyID)
        print(query1)
        query2 = "UPDATE research_center SET min_edu_budget = '{}', private_budget = '{}' WHERE foundation_id = '{}';".\
                format(updateData['min_edu_budget'].data, updateData['private_budget'].data, companyID)
        print(query2)
        try:
            cur = db.connection.cursor()
            cur.execute(query1)
            cur.execute(query2)
            db.connection.commit()
            cur.close()
            flash("Research Center updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getresearch_center"))

@app.route("/research_center/delete/<string:companyID>", methods = ["POST"])
def deleteresearch_center(companyID):
    """
    Delete Research Center by id from database
    """
    query = f"DELETE FROM foundation WHERE id = '{companyID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Research Center deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getresearch_center"))

@app.route("/research_center/create", methods = ["GET", "POST"]) ## "GET" by default
def createresearch_center():
    """
    Create new research_center in the database
    """
    form = CreRCForm()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newcompany = form.__dict__
        query1 = "INSERT INTO foundation (name, abbreviation, postal_code, street,\
             street_number, city, Foundation_phone_1, Foundation_phone_2)\
             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".\
                 format(newcompany['name'].data, newcompany['abbreviation'].data,\
                        newcompany['postal_code'].data, newcompany['street'].data,\
                        newcompany['street_number'].data, newcompany['city'].data,\
                        newcompany['phone1'].data, newcompany['phone2'].data)
        T = 0
        try:
            cur = db.connection.cursor()
            cur.execute(query1)
            db.connection.commit()
            cur.close()
        except Exception as e: ## OperationalError
            flash(str(e), "danger")
            T = 1
        if T == 0:
            try:
                cur = db.connection.cursor()
                query4 = "select id from foundation where foundation_phone_1 = {};".format(newcompany['phone1'].data)
                cur.execute(query4)
                column_names = [i[0] for i in cur.description]
                IDD = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
                aa = IDD[0]['id']
                cur.close()
            except Exception as e: ## OperationalError
                flash(str(e), "danger")
        
            try:
                cur = db.connection.cursor()
                query2 = "INSERT INTO research_center (min_edu_budget, private_budget, foundation_id)\
                 VALUES ('{}', '{}', '{}');".format(newcompany['min_edu_budget'].data, newcompany['private_budget'].data, 
                 aa)
                cur.execute(query2)
                db.connection.commit()
                cur.close()
                flash("Research Center inserted successfully", "success")
                return redirect(url_for("getresearch_center"))
            except Exception as e: ## OperationalError
                flash(str(e), "danger")

    ## else, response for GET request
    return render_template("research_center_create.html", pageTitle = "Create Research Center", form = form)

@app.route("/program")
def getprogram():
    """
    Retrieve programs from database
    """
    try:
        form = programForm()
        cur = db.connection.cursor()
        cur.execute("select * from program;")
        column_names = [i[0] for i in cur.description]
        program = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("program.html", program = program,
                                pageTitle = "Programs Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/program/create", methods = ["GET", "POST"]) ## "GET" by default
def createprogram():
    """
    Create new program in the database
    """
    form = programForm()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newprogram = form.__dict__
        query = "INSERT INTO program(name, elidek_sector) VALUES ('{}', '{}');"\
                .format(newprogram['name'].data, newprogram['ELIDEK_Sector'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Program inserted successfully", "success")
            return redirect(url_for("getprogram"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("program_create.html", pageTitle = "Create Program", form = form)

@app.route("/program/update/<string:programID>", methods = ["POST"])
def updateprogram(programID):
    
    """
    Update a program in the database, by id
    """
    
    form = programForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE program SET name = '{}', ELIDEK_Sector = '{}' WHERE id = '{}';".format(updateData['name'].data,\
             updateData['ELIDEK_Sector'].data, programID)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Program updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getprogram"))

@app.route("/program/delete/<string:programID>", methods = ["POST"])
def deleteprogram(programID):
    """
    Delete program by id from database
    """
    query = f"DELETE FROM program WHERE id = '{programID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Program deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getprogram"))

@app.route("/deliverable")
def getdeliverable():
    """
    Retrieve deliverable from database
    """
    try:
        form = deliverableForm()
        cur = db.connection.cursor()
        cur.execute("select * from deliverable order by project_id ASC, title ASC;")
        column_names = [i[0] for i in cur.description]
        deliverable = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("deliverable.html", deliverable = deliverable,
                                pageTitle = "Deliverable Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/deliverable/create", methods = ["GET", "POST"]) ## "GET" by default
def createdeliverable():
    """
    Create new deliverable in the database
    """
    form = CredeliverableForm()
    #Info for the Drop Down Lists.
    cur = db.connection.cursor()
    ###################################################################
    cur.execute("select ID,TITLE as u from Project;")
    column_names = [i[0] for i in cur.description]
    projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    print("Query 1")
    cur.close()
    
    if(request.method == "POST" and form.validate_on_submit()):
        newdeliverable = form.__dict__
        query = "INSERT INTO deliverable(title, summary, submission_date, project_id) VALUES ('{}', '{}','{}', '{}');"\
                .format(newdeliverable['title'].data, newdeliverable['summary'].data
                       ,newdeliverable['submission_date'].data, newdeliverable['project_id'].data)
        print("2 " + query)
        try:
            print("I am in try")
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Deliverable inserted successfully", "success")
            return redirect(url_for("getdeliverable"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("deliverable_create.html", pageTitle = "Create Deliverable", form = form, projects = projects)

@app.route("/deliverable/update/<string:deliverableID>", methods = ["POST"])
def updatedeliverable(deliverableID):
    
    """
    Update a deliverable in the database, by id
    """
    
    form = deliverableForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE deliverable SET title = '{}', summary = '{}', submission_date = '{}' WHERE id = '{}';".format(updateData['title'].data,\
             updateData['summary'].data,updateData['submission_date'].data, deliverableID)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Deliverable updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getdeliverable"))

@app.route("/deliverable/delete/<string:deliverableID>", methods = ["POST"])
def deletedeliverable(deliverableID):
    """
    Delete deliverable by id from database
    """
    query = f"DELETE FROM deliverable WHERE id = '{deliverableID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Deliverable deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getdeliverable"))

@app.route("/executive")
def getexecutive():
    """
    Retrieve executive from database
    """
    try:
        form = ExForm()
        cur = db.connection.cursor()
        cur.execute("select * from executive;")
        column_names = [i[0] for i in cur.description]
        executive = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("executive.html", executive = executive,
                                pageTitle = "Executives Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/executive/create", methods = ["GET", "POST"]) ## "GET" by default
def createexecutive():
    """
    Create new executive in the database
    """
    form = CreExForm()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newexecutive = form.__dict__
        query = "INSERT INTO executive(id, first_name, last_name)\
             VALUES ('{}', '{}', '{}');".format(newexecutive['ID'].data, \
                 newexecutive['First_Name'].data, newexecutive['Last_Name'].data)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Executive inserted successfully", "success")
            return redirect(url_for("getexecutive"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("executive_create.html", pageTitle = "Create Executive", form = form)

@app.route("/executive/update/<string:executiveID>", methods = ["POST"])
def updateexecutive(executiveID):
    
    """
    Update a executive in the database, by id
    """
    
    form = ExForm()
    updateData = form.__dict__
    if(form.validate_on_submit()):
        query = "UPDATE executive SET first_name = '{}', last_name = '{}' WHERE id = '{}';".\
            format(updateData['First_Name'].data,\
             updateData['Last_Name'].data, executiveID)
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Executive updated successfully", "success")
        except Exception as e:
            flash(str(e), "danger")
    else:
        for category in form.errors.values():
            for error in category:
                flash(error, "danger")
    return redirect(url_for("getexecutive"))

@app.route("/executive/delete/<string:executiveID>", methods = ["POST"])
def deleteexecutive(executiveID):
    """
    Delete executive by id from database
    """
    query = f"DELETE FROM executive WHERE id = '{executiveID}';"
    try:
        cur = db.connection.cursor()
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Executive deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getexecutive"))

@app.route("/psf")
def getpsf():
    """
    Retrieve researchers_works_on_project from database
    """
    try:
        form = psfForm()
        cur = db.connection.cursor()
        cur.execute("select * from project_scientific_field;")
        column_names = [i[0] for i in cur.description]
        psfs = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()
        return render_template("psf.html", psfs = psfs,
                                pageTitle = "Scientific Fields Per Project Page", form = form)
    except Exception as e:
        ## if the connection to the database fails, return HTTP response 500
        flash(str(e), "danger")
        abort(500)

@app.route("/psf/delete/<string:sfn>/<string:projectID>", methods = ["POST"])
def deletepsf(sfn, projectID):
    """
    Delete student by id from database
    """
    query = f"DELETE FROM project_scientific_field WHERE scientific_field_name = '{projectID}'\
             and project_id = '{sfn}';"
    try:
        cur = db.connection.cursor()
        print(query)
        cur.execute(query)
        db.connection.commit()
        cur.close()
        flash("Scientific Field - Project relation deleted successfully", "primary")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for("getpsf"))

@app.route("/psf/create", methods = ["GET", "POST"]) ## "GET" by default
def createpsf():
    """
    Create new Project-Scientific Field relation in the database
    """
    sfns = ""
    form = psfForm()        
    cur = db.connection.cursor()
    cur.execute("select * from scientific_field;")
    column_names = [i[0] for i in cur.description]
    sfns = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.execute("select id, title from project;")
    column_names = [i[0] for i in cur.description]
    projects = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
    ###################################################################
    cur.close()
    ## when the form is submitted
    if(request.method == "POST" and form.validate_on_submit()):
        newworker = form.__dict__
        query = "INSERT INTO project_scientific_field (scientific_field_name, project_id)\
             VALUES ('{}', '{}');".format(newworker['Scientific_Field_Name'].data, \
                 newworker['Project_ID'].data)
        
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            flash("Scientific Field - Project relation inserted successfully", "success")
            return redirect(url_for("getpsf"))
        except Exception as e: ## OperationalError
            flash(str(e), "danger")

    ## else, response for GET request
    return render_template("psf_create.html", pageTitle = "Create Scientific Field - Project relation",\
        projects = projects, form = form, sfns = sfns)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"), 500
