from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_admin import Admin
from flask import Flask
from flask_babel import Babel


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()
babel = Babel()

def create_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = '\xbf\x05E\xe7\xc0W\x86nU8\xf9U\x9e8\xe5\xeb'
    application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u2479897_samurai:samuraishop123456789@localhost/u2479897_shop'
    
    db.init_app(application)
    bcrypt.init_app(application)
    login_manager.init_app(application)
    migrate.init_app(application, db)
    babel.init_app(application)

    
    return application
