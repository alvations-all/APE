
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/instance')

def index():
    return render_template('index.html')

def instance():
    return render_template('instance.html')
