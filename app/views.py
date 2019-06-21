from flask import render_template
from app import app

#View
@app.route('/')
def index():
    """
    View root function returns data in the index page
    """
    message = 'NEWS'
    return render_template('index.html',message = message)



@app.route("/news/<int:news_id>")
def news(news_id):
    """
    View news function returns details in the news details page
    """
    return render_template(news.html,id = news_id)