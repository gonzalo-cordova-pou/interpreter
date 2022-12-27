from flask import Flask
from flask_bootstrap import Bootstrap
from views import shell, report

class Config(object):
    SECRET_KEY = 'secret'

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    
    app.config.from_object(Config)
    
    return app

app = create_app()

if __name__ == '__main__':
    # list of routes
    app.add_url_rule('/', 'shell', shell)
    app.add_url_rule('/report', 'report', report)
    app.run()
