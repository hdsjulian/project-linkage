from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

app = Flask(__name__, static_url_path='html', static_folder='DAS_framework/prototype/')
app.config.from_object(Config)
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
csrf.init_app(app)

#das muss hier unten stehen
from app import routes, models

