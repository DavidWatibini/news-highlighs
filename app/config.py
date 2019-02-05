class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'




class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True
