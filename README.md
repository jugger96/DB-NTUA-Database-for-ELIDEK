# Databases - ΕΛΙΔΕΚ DB

Adapted from [Databases-Java-Demo](https://github.com/ChristosHadjichristofi/Databases-Java-Demo) and [Databases-NodeJS-Demo](https://github.com/ChristosHadjichristofi/Databases-NodeJS-Demo), originally by [Christos Hadjichristofi](https://github.com/ChristosHadjichristofi).

Implementation in PHP [here](https://github.com/cpefkianakis/Databases-PHP-Demo).

## Dependencies

 - [MySQL](https://www.mysql.com/) for Windows
 - [Python](https://www.python.org/downloads/), with the additional libraries:
    - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)
    - [faker](https://faker.readthedocs.io/en/master/) (for data generation)
    - [Flask-WTForms](https://flask-wtf.readthedocs.io/en/1.0.x/) and [email-validator](https://pypi.org/project/email-validator/) (a more involved method of input validation)

Use `pip3 install <package_name>` to install each individual Python package (library) directly for the entire system, or create a virtual environment with the [`venv`](https://docs.python.org/3/library/venv.html) module. The necessary packages for this app are listed in `requirements.txt` and can be installed all together via `pip install -r requirements.txt`.

## What does Flask do

Flask is a micro web framework used to create web applications. It uses [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) as its templating engine, to generate static template files at runtime, and [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) as its WSGI toolkit, to facilitate the communication between web server and application. When writing an app locally, Flask will launch a simple "development" server on which to run it.

## How to Execute SQL Queries with Python and Flask

In order to send queries to a database from a Python program, a connection between it and the databases' server must be established first. That is accomplished by a cursor object from the `Flask-MySQLdb` library, and using the appropriate methods (`execute`, `commit`).

## Flask-WTForms

This package integrates the [WTForms](https://wtforms.readthedocs.io/en/3.0.x/) library with Flask. WTForms is used for secure input (form) validation and form rendering inside the templates. It provides security features such as [CSRF protection](https://en.wikipedia.org/wiki/Cross-site_request_forgery). Each field of a `FlaskForm` class is essentially rendered as the corresponding input tag in HTML.

## Project Structure

Generally, Flask allows some freedom of choice regarding the layout of the application's components. This demo follows the structure recommended by the [official documentation](https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/), whereby a package, arbitrarily named "`dbdemo`", contains the application's code and files, separated into folders for each category (models, controllers, HTML templates - views, static files such as css or images).

 - `__init__.py` configures the application, including the necessary information and credentials for the database
 - `routes.py` currently contains all the endpoints and corresponding controllers
 - `run.py` launches the simple, built-in server and runs the app on it

Run via the `flask run` command (set the environment variable `FLASK_APP` to `run.py`) or directly with `run.py`.


