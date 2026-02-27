import os
from flask import Flask
from .models import db
from flask_migrate import Migrate
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
# Database settings
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
    db.init_app(app)
    migrate = Migrate(app, db)
if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
# Register views
    from .home import views as home_views
    app.register_blueprint(home_views.bp)
    return app
