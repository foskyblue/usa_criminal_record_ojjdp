import json
import plotly
from flask import render_template
from data_wrangling_scripts.data_wrangling import return_figures

from usa_criminal_record_app import app


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')