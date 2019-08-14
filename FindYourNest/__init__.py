#init modules

from flask import Flask
from flask_login import LoginManager
import sqlite3

app = Flask(__name__)
app.config.from_object('config.Config')

login_manager = LoginManager()
login_manager.init_app(app)

import FindYourNest.views
