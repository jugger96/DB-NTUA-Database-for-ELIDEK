from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

## when passed as a parameter to a template, an object of this class will be rendered as a regular HTML form
## with the additional restrictions specified for each field


class CreResForm(FlaskForm):

    ID = StringField(label = "SSN", validators = [DataRequired(message = "SSN is a required field.")])

    First_Name = StringField(label = "First Name", validators = [DataRequired(message = "First Name is a required field.")])

    Last_Name = StringField(label = "Last Name", validators = [DataRequired(message = "Last Name is a required field.")])

    Sex = StringField(label = "Sex", validators = [DataRequired(message = "Sex is a required field.")])

    Birth_Date = StringField(label = "Birth Date", validators = [DataRequired(message = "Birth Date is a required field.")])

    Foundation_ID = StringField(label = "Foundation Id", validators = [DataRequired(message = "Foundation Id is a required field.")])

    Foundation_Date = StringField(label = "Foundation Date", validators = [DataRequired(message = "Foundation Date is a required field.")])

    submit = SubmitField("Create")

class ResForm(FlaskForm):

    First_Name = StringField(label = "First Name", validators = [DataRequired(message = "Surname is a required field.")])

    Last_Name = StringField(label = "Last Name", validators = [DataRequired(message = "Email is a required field.")])

    Sex = StringField(label = "Sex", validators = [DataRequired(message = "Email is a required field.")])

    Birth_Date = StringField(label = "Birth Date", validators = [DataRequired(message = "Email is a required field.")])

    Foundation_ID = StringField(label = "Foundation Id", validators = [DataRequired(message = "Email is a required field.")])

    Foundation_Date = StringField(label = "Foundation Date", validators = [DataRequired(message = "Email is a required field.")])

    submit = SubmitField("Create")

class WorksForm(FlaskForm):

    Project_ID = StringField(label = "Project ID", validators = [DataRequired(message = "Project_ID is a required field.")])

    Researcher_ID = StringField(label = "Researcher SSN", validators = [DataRequired(message = "Researcher_ID is a required field.")])

    submit = SubmitField("Create")

class ProjForm(FlaskForm):

    ID = StringField(label = "ID", validators = [DataRequired(message = "Surname is a required field.")])

    Title = StringField(label = "Title", validators = [DataRequired(message = "Email is a required field.")])

    Start_Date = StringField(label = "Start_Date", validators = [DataRequired(message = "Email is a required field.")])

    End_Date = StringField(label = "End_Date", validators = [DataRequired(message = "Email is a required field.")])

    Summary = StringField(label = "Summary", validators = [DataRequired(message = "Email is a required field.")])

    Funding = StringField(label = "Funding", validators = [DataRequired(message = "Email is a required field.")])

    Executive_ID = StringField(label = "Executive_ID", validators = [DataRequired(message = "Email is a required field.")])

    Program_ID = StringField(label = "Program_ID", validators = [DataRequired(message = "Email is a required field.")])

    Foundation_ID = StringField(label = "Foundation_ID", validators = [DataRequired(message = "Email is a required field.")])

    Researcher_ID_Boss = StringField(label = "Researcher_ID_Boss", validators = [DataRequired(message = "Email is a required field.")])

    Researcher_ID_eval = StringField(label = "Researcher_ID_eval", validators = [DataRequired(message = "Email is a required field.")])


    Evaluation_Date = StringField(label = "Evaluation_Date", validators = [DataRequired(message = "Email is a required field.")])

    Evaluation_Grade = StringField(label = "Evaluation_Grade", validators = [DataRequired(message = "Email is a required field.")])

    Scientific_Field_Name = StringField(label = "Scientific_Field_Name", validators = [DataRequired(message = "Email is a required field.")])

    submit = SubmitField("Create")

class UpProjForm(FlaskForm):

    #ID = StringField(label = "ID", validators = [DataRequired(message = "Surname is a required field.")])

    Title = StringField(label = "Title", validators = [DataRequired(message = "Email is a required field.")])

    Start_Date = StringField(label = "Start_Date", validators = [DataRequired(message = "Email is a required field.")])

    End_Date = StringField(label = "End_Date", validators = [DataRequired(message = "Email is a required field.")])

    Summary = StringField(label = "Summary", validators = [DataRequired(message = "Email is a required field.")])

    Funding = StringField(label = "Funding", validators = [DataRequired(message = "Email is a required field.")])

    Executive_ID = StringField(label = "Executive_ID", validators = [DataRequired(message = "Email is a required field.")])

    Program_ID = StringField(label = "Program_ID", validators = [DataRequired(message = "Email is a required field.")])

    Foundation_ID = StringField(label = "Foundation_ID", validators = [DataRequired(message = "Email is a required field.")])

    Researcher_ID_Boss = StringField(label = "Researcher_ID_Boss", validators = [DataRequired(message = "Email is a required field.")])

    Researcher_ID_eval = StringField(label = "Researcher_ID_eval", validators = [DataRequired(message = "Email is a required field.")])


    Evaluation_Date = StringField(label = "Evaluation_Date", validators = [DataRequired(message = "Email is a required field.")])

    Evaluation_Grade = StringField(label = "Evaluation_Grade", validators = [DataRequired(message = "Email is a required field.")])

    #Scientific_Field_Name = StringField(label = "Scientific_Field_Name", validators = [DataRequired(message = "Email is a required field.")])

    submit = SubmitField("Create")

class CreProjForm(FlaskForm):

    #ID = StringField(label = "ID", validators = [DataRequired(message = "Surname is a required field.")])

    Title = StringField(label = "Title", validators = [DataRequired(message = "Email is a required field.")])

    Start_Date = StringField(label = "Start_Date", validators = [DataRequired(message = "Email is a required field.")])

    End_Date = StringField(label = "End_Date", validators = [DataRequired(message = "Email is a required field.")])

    Summary = StringField(label = "Summary", validators = [DataRequired(message = "Email is a required field.")])

    Funding = StringField(label = "Funding", validators = [DataRequired(message = "Email is a required field.")])

    Executive_ID = StringField(label = "Executive_ID", validators = [DataRequired(message = "Email is a required field.")])

    Program_ID = StringField(label = "Program_ID", validators = [DataRequired(message = "Email is a required field.")])

    Foundation_ID = StringField(label = "Foundation_ID", validators = [DataRequired(message = "Email is a required field.")])

    Researcher_ID_Boss = StringField(label = "Researcher_ID_Boss", validators = [DataRequired(message = "Email is a required field.")])

    Researcher_ID_eval = StringField(label = "Researcher_ID_eval", validators = [DataRequired(message = "Email is a required field.")])


    Evaluation_Date = StringField(label = "Evaluation_Date", validators = [DataRequired(message = "Email is a required field.")])

    Evaluation_Grade = StringField(label = "Evaluation_Grade", validators = [DataRequired(message = "Email is a required field.")])

    Scientific_Field_Name = StringField(label = "Scientific_Field_Name", validators = [DataRequired(message = "Email is a required field.")])

    submit = SubmitField("Create")

class project_worker(FlaskForm):
    researcher_id = StringField(label = "Researcher Id", validators = [DataRequired(message = "Researcher ID is a required field.")])
    submit = SubmitField("Create")

class SciForm(FlaskForm):
    Name = StringField(label = "Name", validators = [DataRequired(message = "Email is a required field.")])
    submit = SubmitField("Create")

class CompanyForm(FlaskForm):

    name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    abbreviation = StringField(label = "Abbreviation", validators = [DataRequired(message = "Abbreviation is a required field.")])

    postal_code = StringField(label = "Postal Code", validators = [DataRequired(message = "Postal Code is a required field.")])

    street = StringField(label = "Street", validators = [DataRequired(message = "Street is a required field.")])

    street_number = StringField(label = "Street Number", validators = [DataRequired(message = "Street Number is a required field.")])

    city = StringField(label = "City", validators = [DataRequired(message = "City is a required field.")])

    equaty_capitals = StringField(label = "Equaty Capitals", validators = [DataRequired(message = "Equaty Capitals is a required field.")])

    submit = SubmitField("Create")

class CreCompanyForm(FlaskForm):

    name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    abbreviation = StringField(label = "Abbreviation", validators = [DataRequired(message = "Abbreviation is a required field.")])

    postal_code = StringField(label = "Postal Code", validators = [DataRequired(message = "Postal Code is a required field.")])

    street = StringField(label = "Street", validators = [DataRequired(message = "Street is a required field.")])

    street_number = StringField(label = "Street Number", validators = [DataRequired(message = "Street Number is a required field.")])

    city = StringField(label = "City", validators = [DataRequired(message = "City is a required field.")])

    equaty_capitals = StringField(label = "Equaty Capitals", validators = [DataRequired(message = "Equaty Capitals is a required field.")])

    phone1 = StringField(label = "Phone Number 1", validators = [DataRequired(message = "phone1 is a required field.")])

    phone2 = StringField(label = "Phone Number 2", validators = [DataRequired(message = "phone2 is a required field.")])

    submit = SubmitField("Create")

class UniversityForm(FlaskForm):

    name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    abbreviation = StringField(label = "Abbreviation", validators = [DataRequired(message = "Abbreviation is a required field.")])

    postal_code = StringField(label = "Postal Code", validators = [DataRequired(message = "Postal Code is a required field.")])

    street = StringField(label = "Street", validators = [DataRequired(message = "Street is a required field.")])

    street_number = StringField(label = "Street Number", validators = [DataRequired(message = "Street Number is a required field.")])

    city = StringField(label = "City", validators = [DataRequired(message = "City is a required field.")])

    min_edu_budget = StringField(label = "MinEdu Budget", validators = [DataRequired(message = "MinEdu Budget is a required field.")])

    submit = SubmitField("Create")

class CreUniversityForm(FlaskForm):

    name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    abbreviation = StringField(label = "Abbreviation", validators = [DataRequired(message = "Abbreviation is a required field.")])

    postal_code = StringField(label = "Postal Code", validators = [DataRequired(message = "Postal Code is a required field.")])

    street = StringField(label = "Street", validators = [DataRequired(message = "Street is a required field.")])

    street_number = StringField(label = "Street Number", validators = [DataRequired(message = "Street Number is a required field.")])

    city = StringField(label = "City", validators = [DataRequired(message = "City is a required field.")])

    min_edu_budget = StringField(label = "MinEdu Budget", validators = [DataRequired(message = "MinEdu Budget is a required field.")])

    phone1 = StringField(label = "Phone Number 1", validators = [DataRequired(message = "phone1 is a required field.")])

    phone2 = StringField(label = "Phone Number 2", validators = [DataRequired(message = "phone2 is a required field.")])

    submit = SubmitField("Create")

class RCForm(FlaskForm):

    name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    abbreviation = StringField(label = "Abbreviation", validators = [DataRequired(message = "Abbreviation is a required field.")])

    postal_code = StringField(label = "Postal Code", validators = [DataRequired(message = "Postal Code is a required field.")])

    street = StringField(label = "Street", validators = [DataRequired(message = "Street is a required field.")])

    street_number = StringField(label = "Street Number", validators = [DataRequired(message = "Street Number is a required field.")])

    city = StringField(label = "City", validators = [DataRequired(message = "City is a required field.")])

    min_edu_budget = StringField(label = "MinEdu Budget", validators = [DataRequired(message = "MinEdu Budget is a required field.")])

    private_budget = StringField(label = "Private Budget", validators = [DataRequired(message = "Private Budget is a required field.")])

    submit = SubmitField("Create")

class CreRCForm(FlaskForm):

    name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    abbreviation = StringField(label = "Abbreviation", validators = [DataRequired(message = "Abbreviation is a required field.")])

    postal_code = StringField(label = "Postal Code", validators = [DataRequired(message = "Postal Code is a required field.")])

    street = StringField(label = "Street", validators = [DataRequired(message = "Street is a required field.")])

    street_number = StringField(label = "Street Number", validators = [DataRequired(message = "Street Number is a required field.")])

    city = StringField(label = "City", validators = [DataRequired(message = "City is a required field.")])

    min_edu_budget = StringField(label = "MinEdu Budget", validators = [DataRequired(message = "MinEdu Budget is a required field.")])

    private_budget = StringField(label = "Private Budget", validators = [DataRequired(message = "Private Budget is a required field.")])

    phone1 = StringField(label = "Phone Number 1", validators = [DataRequired(message = "phone1 is a required field.")])

    phone2 = StringField(label = "Phone Number 2", validators = [DataRequired(message = "phone2 is a required field.")])

    submit = SubmitField("Create")

class PhoneForm(FlaskForm):
    phone = StringField(label = "Phone Number", validators = [DataRequired(message = "Phone Number is a required field.")])
    submit = SubmitField("Create")

class programForm(FlaskForm):

    #id = StringField(label = "ID", validators = [DataRequired(message = "ID is a required field.")])

    name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    ELIDEK_Sector = StringField(label = "ELIDEK Sector", validators = [DataRequired(message = "Sector is a required field.")])

    submit = SubmitField("Create")

class deliverableForm(FlaskForm):
    #id = StringField(label = "ID", validators = [DataRequired(message = "ID is a required field.")])

    title = StringField(label = "Title", validators = [DataRequired(message = "Title is a required field.")])

    summary = StringField(label = "Summary", validators = [DataRequired(message = "Summary is a required field.")])

    submission_date = StringField(label = "submission Date", validators = [DataRequired(message = "Submission Date is a required field.")])

    #project_id = StringField(label = "Project ID", validators = [DataRequired(message = "Project ID is a required field.")])

    submit = SubmitField("Create")

class CredeliverableForm(FlaskForm):
    #id = StringField(label = "ID", validators = [DataRequired(message = "ID is a required field.")])

    title = StringField(label = "Title", validators = [DataRequired(message = "Title is a required field.")])

    summary = StringField(label = "Summary", validators = [DataRequired(message = "Summary is a required field.")])

    submission_date = StringField(label = "submission Date", validators = [DataRequired(message = "Submission Date is a required field.")])

    project_id = StringField(label = "Project ID", validators = [DataRequired(message = "Project ID is a required field.")])

    submit = SubmitField("Create")

class CreResForm(FlaskForm):

    ID = StringField(label = "SSN", validators = [DataRequired(message = "SSN is a required field.")])

    First_Name = StringField(label = "First Name", validators = [DataRequired(message = "First Name is a required field.")])

    Last_Name = StringField(label = "Last Name", validators = [DataRequired(message = "Last Name is a required field.")])

    Sex = StringField(label = "Sex", validators = [DataRequired(message = "Sex is a required field.")])

    Birth_Date = StringField(label = "Birth Date", validators = [DataRequired(message = "Birth Date is a required field.")])

    Foundation_ID = StringField(label = "Foundation Id", validators = [DataRequired(message = "Foundation Id is a required field.")])

    Foundation_Date = StringField(label = "Foundation Date", validators = [DataRequired(message = "Foundation Date is a required field.")])

    submit = SubmitField("Create")

class ResForm(FlaskForm):

    First_Name = StringField(label = "First Name", validators = [DataRequired(message = "Surname is a required field.")])

    Last_Name = StringField(label = "Last Name", validators = [DataRequired(message = "Email is a required field.")])

    Sex = StringField(label = "Sex", validators = [DataRequired(message = "Email is a required field.")])

    Birth_Date = StringField(label = "Birth Date", validators = [DataRequired(message = "Email is a required field.")])

    Foundation_ID = StringField(label = "Foundation Id", validators = [DataRequired(message = "Email is a required field.")])

    Foundation_Date = StringField(label = "Foundation Date", validators = [DataRequired(message = "Email is a required field.")])

    submit = SubmitField("Create")

class CreExForm(FlaskForm):

    ID = StringField(label = "SSN", validators = [DataRequired(message = "SSN is a required field.")])

    First_Name = StringField(label = "First Name", validators = [DataRequired(message = "First Name is a required field.")])

    Last_Name = StringField(label = "Last Name", validators = [DataRequired(message = "Last Name is a required field.")])

    submit = SubmitField("Create")

class ExForm(FlaskForm):

    First_Name = StringField(label = "First Name", validators = [DataRequired(message = "Surname is a required field.")])

    Last_Name = StringField(label = "Last Name", validators = [DataRequired(message = "Email is a required field.")])

    submit = SubmitField("Create")

class psfForm(FlaskForm):

    Project_ID = StringField(label = "Project ID", validators = [DataRequired(message = "Project ID is a required field.")])

    Scientific_Field_Name = StringField(label = "Scientific Field Name", validators = [DataRequired(message = "Scientific Field Name is a required field.")])

    submit = SubmitField("Create")


