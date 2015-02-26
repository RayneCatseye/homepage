from flask import render_template, send_from_directory
from app import app

# Create URL mappings; note that order is important.
# Mappings must be followed by the function to display
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",
        title = 'Home')

# 
@app.route('/resume/')
def resume():
    return render_template('resume.html',
        title = 'Resume')

@app.route('/projects/')
def projects():
    return render_template('projects.html',
        title = 'Projects')

@app.route('/contact/')
def about():
    return render_template('contact.html',
        title = 'Contact Me')

@app.route('/bootstrap.css/')
def publickey():
    return render_template('css/bootstrap.css')

@app.route('/keybase.txt')
def keybase():
    return render_template('keybase.txt')
