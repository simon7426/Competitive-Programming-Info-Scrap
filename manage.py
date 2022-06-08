from flask.cli import FlaskGroup
from werkzeug.middleware.proxy_fix import ProxyFix

from project import create_app

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
