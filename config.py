class Config:
    DEBUG = True
    TESTING = False


class DevConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/reddit"
    SECRET_KEY = "verysecretkeyforthisapp"


class ProdConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "mysql://prod:1strongpassword@localhost/reddit"


class TestConfig(Config):
    TESTING = True

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}