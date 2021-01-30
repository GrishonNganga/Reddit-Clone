from flask import Flask, request, render_template, redirect
from flask_migrate import Migrate

from config import config

migrate = Migrate()

from datetime import datetime

def create_app(config_type):
        
    app = Flask(__name__)
    
    app.config.from_object(config[config_type])

    from models import mysql
    mysql.init_app(app)
    migrate.init_app(app, mysql)

    from routes import main
    app.register_blueprint(main)

    return app
