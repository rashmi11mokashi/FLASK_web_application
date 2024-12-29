from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_migrate import Migrate

db = SQLAlchemy()
DB_Name = "database.db"
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfghjkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'
    print(app.config['SQLALCHEMY_DATABASE_URI'])  # Check the database URI
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    from .models import User, Note
    
    create_database(app)

    return app 

def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_Name):
            db.create_all()
            print(f'DB created!', DB_Name)