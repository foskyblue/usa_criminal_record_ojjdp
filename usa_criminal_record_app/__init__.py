from flask import Flask

app = Flask(__name__)

from usa_criminal_record_app import routes
