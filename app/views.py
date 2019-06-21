from flask import render_template
from app import app

#View
@app.route('/')
def index():
    """
    View root function returns data in the index page
    """
    title = 'HOME - WELCOME TO WHERE KNOWLEDGE IS POWER'
    return render_template('index.html',title = title)



@app.route("/news/<int:news_id>")
def news(news_id):
    """
    View news function returns details in the news details page
    """
    return render_template('news.html',id = news_id)