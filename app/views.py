from flask import render_template, flash, redirect
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
