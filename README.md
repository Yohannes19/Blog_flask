# Blog_flask
Simple blog system using flask web framework using the scalable blueprint functions of flask

In this application i created the following blueprints for management :

main: the main blueprint for main routes, such as the home page.
posts: the posts blueprint for managing blog posts.
questions: the questions blueprint for managing questions and answers.
models: the directory that will contain Flask-SQLAlchemy models.
templates: the templates directory that will contain files for the main blueprint and a directory for each blueprint.

#How to run this application

Step 1 — Installing Flask and Flask-SQLAlchemy
In this step, you’ll install the necessary packages for your application.

$ my_env/bin/activate

With your virtual environment activated, use pip to install Flask and Flask-SQLAlchemy

$pip install Flask Flask-SQLAlchemy

Step 2 — Creating a Configuration File
In this step, you’ll create a configuration file for your Flask application, separating your application settings from the rest of the application and making changing settings easier


Finally ! do not forget to create .ENV enviroment variable that have the url for the database connection

Then use Flask run command to run the application
