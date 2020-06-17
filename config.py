import os


class Config:
    '''
    General configuration parent class
    '''
    QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'

    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/crystal/atompython/blogtrial/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_PUCE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
