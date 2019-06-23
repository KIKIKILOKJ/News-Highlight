from flask import render_template
from app import app
from .request import get_news_sources,get_business_headlines,get_everything_news,search_articles,get_news_headlines

#View
@app.route('/')
def index():
    """
    View root function returns data in the index page
    """
    
    title = 'HOME - WELCOME TO WHERE KNOWLEDGE IS POWER'
    return render_template('index.html',title = title,)



@app.route("/news/<news_id>")
def news(news_id):
    """
    View news function returns details in the news details page
    """
    title = 'HAVEN OF NEWS WORLDWIDE'
    return render_template('news.html',id = news_id,title = title)