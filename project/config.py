import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")


class DevelopmentConfig(BaseConfig):
    RESTX_ERROR_404_HELP = False


class TestingConfig(BaseConfig):
    TESTING = True
    RESTX_ERROR_404_HELP = False


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv("SECRET_KEY")
