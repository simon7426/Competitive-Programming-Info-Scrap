import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    CACHE_TYPE = "redis"
    CACHE_REDIS_HOST = os.getenv("REDIS_SERVER", "localhost")
    CACHE_REDIS_POST = 6379
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = "redis://" + CACHE_REDIS_HOST + ":6379/0"
    CACHE_DEFAULT_TIMEOUT = 86400


class DevelopmentConfig(BaseConfig):
    RESTX_ERROR_404_HELP = False


class TestingConfig(BaseConfig):
    TESTING = True
    RESTX_ERROR_404_HELP = False


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv("SECRET_KEY")
