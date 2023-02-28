from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from spectree import SpecTree


from config import Config

db = SQLAlchemy()
migrate = Migrate()
api = SpecTree("flask", title="Api Municípios", version="v.1.0", path="docs")

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from models import Estado, Municipio

    migrate.init_app(app, db)

    from controllers import estado_controller, municipio_controller
    app.register_blueprint(estado_controller)
    app.register_blueprint(municipio_controller)

    api.register(app)
    
    return app