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
    
def get_news_sources():
    '''
    Function that gets the json response to our url request which is all news available
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

def get_news_headlines(source):
    """
    Function will fetch all the news headlines available
    """
    top_headlines_url = top_headlines_url.format(source, api_key )

    with urllib.request.urlopen(top_headlines_url) as url:
        headline_data = url.read()
        headlines_response = json.loads(headline_data)
        headlines_results = None
        if headlines_response['articles']:
            """
            Searches for empty sources
            """
            headlines_items = headlines_response['articles']
            headlines_results = process_headlines_sources(headlines_items)

    return headlines_results

def process_headlines_sources(headlines_list):
    """
    Function is responsible for processing data to Top Headlines available
    """
    headlines_results = []
    for item in headlines_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        news_headlines = headlines_list(author, title, description, url, urlToImage, publishedAt)
        headlines_results.append(news_headlines)

    return headlines_results

def get_everything_news():
    """
    Function that fetches all the news available for display
    """
    everything_complete_url = everything_news_url.format(api_key)

    with urllib.request.urlopen(everything_complete_url) as url:
        everything_data = url.read()
        everything_response = json.loads(everything_data)
        everything_results = None

        if everything_response['articles']:
            everything_results_list = everything_response['articles']
            everything_results = process_everything_results(everything_results_list)

    return everything_results

def process_everything_results(everything_results_list):
    """
    Function processes data given to produce the news available for display
    """
    everything_results = []
    for item in everything_results_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')

        everything_object = everything_results_list(author, title, description, url, urlToImage, publishedAt)
        everything_results.append(everything_object)
        
    return everything_results

def get_business_headlines():
    """
    Function will fetch business headlines and related news for viewing
    """
    business_headlines_complete_url = business_headlines_url.format(api_key)
    with urllib.request.urlopen(business_headlines_complete_url) as url:
        business_headlines_data = url.read()
        business_headlines_response = json.loads(business_headlines_data)
        business_headlines_results = None

        if business_headlines_response['articles']:
            business_headlines_results_list = business_headlines_response['articles']
            business_headlines_results = process_business_headlines_results(business_headlines_results_list)

    return business_headlines_results

def process_business_headlines_results(business_headlines_results_list):
    """
    Function is responsible for processing data to news to the world of business
    """
    business_headlines_results = []
    for item in business_headlines_results_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')

        business_headlines_object = business_headlines_results_list(author, title, description, url, urlToImage, publishedAt)
        business_headlines_results.append(business_headlines_object)
        
    return business_headlines_results

def search_articles(source):
    """
    Function allows the user to search for articles
    """
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(source, api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)
        search_article_results = None
        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_business_headlines_results(search_article_list)
    return search_article_results