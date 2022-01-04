"""
    Configuration
    _______________
    This is module for storing all configuration for various environments
"""
import os
from app.config import error

basedir = os.path.abspath(os.path.dirname("data"))

class Config:
    """ This is base class for configuration """
    # DEBUG = False

    # UPLOAD_FOLDER = basedir + "/data/images/"
    # ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    JSON_SORT_KEYS = False
    
    DATABASE = {
        "DRIVER"   : os.getenv('DB_DRIVER') or "postgresql://", # sqlite // postgresql // mysql
        "USERNAME" : os.getenv('DB_USERNAME') or "pacmann",
        "PASSWORD" : os.getenv('DB_PASSWORD') or "cangcimen",
        "HOST_NAME": os.getenv('DB_HOSTNAME') or "localhost",
        "DB_NAME"  : os.getenv('DB_NAME') or "db_middleware_api",
    }

    SENTRY_CONFIG = {}

    JWT_CONFIG = {
        "EXPIRE" : {
            "ACCESS_TOKEN" : os.getenv('JWT_ACCESS_TOKEN_EXPIRES') or 3600, #15*60
            "REFRESH_TOKEN" : os.getenv('JWT_REFRESH_TOKEN_EXPIRES') or 2592000 #3600*24*30
        },
        "SECRET" : os.getenv('JWT_SECRET') or "asdfasdas",
        "ALGORITHM" : "HS256",
    }

    ERROR = error

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

#end class


class DevelopmentConfig(Config):
    """ This is class for development configuration """
    DEBUG = True

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
            DATABASE["DB_NAME"] + "_dev"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
#end class


class TestingConfig(Config):
    """ This is class for testing configuration """
    DEBUG = True
    TESTING = True

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
            DATABASE["DB_NAME"] + "_testing"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SENTRY_CONFIG = {}
#end class


class ProductionConfig(Config):
    """ This is class for production configuration """
    DEBUG = False

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
            DATABASE["DB_NAME"] + "_prod"
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    SENTRY_CONFIG = Config.SENTRY_CONFIG
    SENTRY_CONFIG["dsn"] = os.environ.get("SENTRY_DSN")
#end class

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)