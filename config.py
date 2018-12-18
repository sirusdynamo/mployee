class Config(object):
    """
    common configurations
    """
    DEBUG = False
    TESTING = False

    #put any configuration here that is common to all environments


class DevelopmentConfig(Config):
    """
    Develpoment configurations
    """
    DEBUG =True
    SQLALCHEMY_ECHO=True



class ProductionConfig(Config):
    """ 
    Production configurations
    """
    DEBUG=False


app_config={
        'development':DevelopmentConfig,
        'production':ProductionConfig
    }