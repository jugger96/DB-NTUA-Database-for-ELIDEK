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




