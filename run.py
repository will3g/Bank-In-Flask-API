''''Não se esqueça do POG que faz import ciclico'''
from flask import Flask
from my_app.views import conta_bp
from my_api import api
from database import db

def create_app():

    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    app.template_folder = 'my_app/template'
    app.static_url_path = 'my_app/static'

    app.register_blueprint(conta_bp)
    app.register_blueprint(api)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    setup_database(app)
    app.run()