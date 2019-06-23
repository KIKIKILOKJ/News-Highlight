from flask import render_template
from app import app
from .request import get_news_sources,get_business_headlines,get_everything_news,search_articles,get_news_headlines

#View
@app.route('/')
def index():
    """
    View root function returns data in the index page
    """
    all_news_sources = get_news_sources()
    everything_news_items = get_everything_news()
    business_headlines = get_business_headlines()
    title = 'HOME - WELCOME TO WHERE KNOWLEDGE IS POWER'
    return render_template('index.html',title = title,sources = all_news_sources,featured = everything_news_items,business = business_headlines)



@app.route("/source/<source>")
def headlines(source):
    """
    View source function returns details in the news details page
    """
    news_headlines = get_news_headlines(source)
    title = 'HAVEN OF NEWS WORLDWIDE'
    return render_template('news.html',title = title, headlines = news_headlines)