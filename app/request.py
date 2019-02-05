from app import app
import urllib.request,json
from .models import news,article

News = news.News
Article = article.Article

api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
articles_base_url = app.config['ARTICLES_API_BASE_URL']


def get_article(id):

    get_article_url = articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:

        get_article_data = url.read()

        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:

            article_results_list = get_article_response['articles']

            article_results = process_article_results(article_results_list)

    return article_results

def process_article_results(article_list):

    article_results = []

    for article_item in article_list:

        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')


        article_object = Article(source,author,title,description,publishedAt)
        article_results.append(article_object)

    return article_results


def get_news(category):

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:


        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:

            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):

    news_results = []

    for news_item in news_list:

        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        news_object = News(id,name,description,url,category)
        news_results.append(news_object)

    return news_results
