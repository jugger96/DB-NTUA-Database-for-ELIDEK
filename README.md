# Databases - ΕΛΙΔΕΚ DB

The UI of the webapp was inspired by [Christos Hadjichristofi](https://github.com/ChristosHadjichristofi) and [Dimitrios Kyriakidis](https://github.com/DimK19).

## Dependencies

 - [MySQL](https://www.mysql.com/) for Windows
 - [Python](https://www.python.org/downloads/), with the additional libraries:
    - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)
    - [faker](https://faker.readthedocs.io/en/master/) (for data generation)
    - [Flask-WTForms](https://flask-wtf.readthedocs.io/en/1.0.x/) and [email-validator](https://pypi.org/project/email-validator/) (a more involved method of input validation)

## What does Flask do

Flask is a micro web framework used to create web applications. It uses [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) as its templating engine, to generate static template files at runtime, and [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) as its WSGI toolkit, to facilitate the communication between web server and application. When writing an app locally, Flask will launch a simple "development" server on which to run it.

## How to Execute SQL Queries with Python and Flask

In order to send queries to a database from a Python program, a connection between it and the databases' server must be established first. That is accomplished by a cursor object from the `Flask-MySQLdb` library, and using the appropriate methods (`execute`, `commit`).

## Flask-WTForms

This package integrates the [WTForms](https://wtforms.readthedocs.io/en/3.0.x/) library with Flask. WTForms is used for secure input (form) validation and form rendering inside the templates. It provides security features such as [CSRF protection](https://en.wikipedia.org/wiki/Cross-site_request_forgery). Each field of a `FlaskForm` class is essentially rendered as the corresponding input tag in HTML.

## Installation Guide

Αρχικά κατεβάζουμε το anaconda από το εδώ και το εγκαθιστούμε https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe.

Από το command promt του ανακόντα με χρήση του cd μπαίνουμε στο directory του folder που κατεβάσαμε από το github.

Έπειτα πληκτρολογούμε και τρέχουμε την εντολή “pip install requirements.txt” ώστε να εγκαταστήσουμε όλα τα απαραίτητα πακέτα για το framework  του webapp και για τη σύνδεση της βάσης  με αυτό.

Στη συνέχεια ,και αφού έχουμε κατοχυρώσει και επιβεβαιώσει σύνδεση κάνοντας χρήση του xampp (“run as administrator”), εκτελούμε τα αρχεία “schema.sql”, “triggers.sql”, “views.sql” και “data.sql” με την σειρά που αναγράφονται, ενδεικτικά μέσω του MySQL wokbench, έτσι ώστε να φτιάξουμε τη βάση μας, με όλα τα tables, triggers και views που είναι απαραίτητα για την ορθή λειτουργεία της, και να τη γεμίσουμε με δεδομένα.

Ανοίγουμε ολόκληρο το folder που κατεβάσαμε από το github με κάποιο idee,  επιβεβαιώνουμε ότι έχουμε ορίσει ως python interptreter τον anaconda3.Για το κάνουμε αυτό ενδεικτικά θα μπορούσαμε να χρησιμοποιήσουμε ως idee το “Visual Studio Code”, ανοίγοντάς το από τον “Anaconda Navigator”.

Μέσω του idee, βάζουμε στο αρχείο  “__init__.py” τα στοιχεία της βάσης και του “user”, προσοχή αν έχετε κωδικό για τον root user βγάλτε το πεδίο “app.config[MYSQL_PASSWORD]” από σχόλιο και πληκτρολογήστε σε αυτό τον κωδικό που έχετε ορίσει. 

Τέλος εκτελούμε το αρχείο “run.py” και μπορούμε να ανοίξουμε τη βάση στο browser στη διεύθυνση που ορίζει ο host (by default: http://localhost:3000). 

```dghjf```

