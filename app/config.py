class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}country=us&apiKey={}'


    pass



class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True
