from flask import render_template
from app import app

#View
@app.route('/')
def index():
    """
    View root function returns data in the index page
    """
    return render_template('index.html')