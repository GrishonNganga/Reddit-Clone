from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from routes import main
from config import DevConfig

mysql = SQLAlchemy()
migrate = Migrate()

from datetime import datetime

def create_app(config_value):
        
    app = Flask(__name__)
    
    app.config.from_object(DevConfig)

    mysql.init_app(app)
    migrate.init_app(app, mysql)

    app.register_blueprint(main)

    return app
