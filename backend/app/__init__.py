import os
from datetime import timedelta
from functools import update_wrapper
from flask import Flask, current_app, send_file, make_response
from flask_cors import CORS

from .api import api_bp
from .client import client_bp

app = Flask(__name__)
CORS(app, origins=['https://frontend.smartcheck.ml'])
app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))