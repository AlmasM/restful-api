from flask import Flask
from rest_http_functions.controllers.device import device

app = Flask(__name__)
app.register_blueprint(device, url_prefix='/')
