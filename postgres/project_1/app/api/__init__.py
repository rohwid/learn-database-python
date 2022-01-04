import os

import redis

import pyorient
from flask  import Flask

from app.config import config

from flask_marshmallow  import Marshmallow

from pyorient.ogm import Graph, Config

from flasgger import Swagger

from app.api.model import db


db_graph = Graph(Config.from_url(os.getenv('DB_GRAPH_URL') or "localhost/graph", 
                                os.getenv('DB_GRAPH_USERNAME') or "root", 
                                os.getenv('DB_GRAPH_PASSWORD') or "root",
                                initial_drop=False))

ma = Marshmallow()

#Swagger Template
template = {
  "info": {
    "title": "Midleware API",
    "description": "API for middleware Insight-AI and Graph-AI ",
    "version": "0.0.1"
  },
    "securityDefinitions":{
        "Bearer":{
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}


def create_app(config_name):
    """
        Create flask instance using application factory pattern
        args :
            config_name -- Configuration key used (DEV/PROD/TESTING)
    """
    app = Flask(__name__)
    app.config.from_object(config.CONFIG_BY_NAME[config_name])

    if app.debug or app.testing:
        swagger = Swagger(app, template=template)

    with app.app_context():
        db.init_app(app)
        db_graph
        # db_redis
        config_oauth(app)

        

    # if not app.debug and not app.testing:
    #     sentry.init_app(app)

    return app