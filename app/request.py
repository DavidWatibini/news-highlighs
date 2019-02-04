from app import app
import urllib.request,json
from .models import newsSource

NewsSource = newsSource.NewsSource

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(source):

    get_news_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_url) as url:

        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:

            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):

    news_results = []

    for news_item in news_list:

        name = news_item.get('name')
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if url:

            news_object = (name,title,author,description,url,publishedAt,content)
            movie_results.append(news_object)

    return news_object
