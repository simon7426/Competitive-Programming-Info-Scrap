import logging
import os

from flask import Flask
from flask_caching import Cache
from flask_cors import CORS

cors = CORS()
cache = Cache()


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)

    app_settings = os.environ.get("APP_SETTINGS", "project.config.DevelopmentConfig")
    app.config.from_object(app_settings)

    cors.init_app(app)
    cache.init_app(app)

    from project.apis import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():  # pragma: no cover
        return {"app": app}

    return app
