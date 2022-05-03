import os

class Config:
    '''
    The main configuration class for the application
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q={}&from=2018-10-09&sortBy=publishedAt&language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
 


class ProdConfig(Config):
    '''
    Class that forms the subclass of the Config class and Debug-effective in the production environment

    Args:
        Config class
    '''
    pass


class DevConfig(Config):
    '''
    Class that is a subclass of the Config class and Debug-effective in the development phase/environment

    Args:
        Config class
    '''
    DEBUG=True


config_options={
    'development': DevConfig,
    'production': ProdConfig
}
