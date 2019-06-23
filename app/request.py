from app import app
import urllib.request,json
from .models import news


#getting api key
api_key = None
#getting the news source url
sources_url = None
#getting news headlines urls
business_top_headlines = None
everything_news_url = None
top_headlines_url = None

def configure_request(app):
    global api_key,sources_url,business_top_headlines,everything_news_url,top_headlines_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config('SOURCES_BASE_API_URL')
    business_top_headlines_url = app.config['BUSINESS_TOP_HEADLINES']
    everything_news_url = app.config['EVERYTHING_BASE_API_URL']
    top_headlines_news_url = app.config['TOP_HEADLINES_BASE_API_URL']
    
def get_news():
    '''
    Function that gets the json response to our url request which is all news available on the particular headline
    '''
    complete_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(complete_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_response['sources']:
            sources_news = sources_response['sources']
            sources_results = process_news_sources(sources_news)


    return sources_results


def process_news_sources(news_list):
    '''
    Function  that processes the news result and transform them to a list of Object news

    Returns :
        sources_results: News from various parts of the world
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item('publishedAt')

    return news_results