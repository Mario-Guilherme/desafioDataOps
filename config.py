import os
from abc import ABC

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(ABC):
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    TESTING = False
    DATABASE_URI = "mongodb://root:example@localhost:27017/"
    TIME_OUT = 5000
