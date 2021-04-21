import json
import plotly
from flask import render_template, request
from usa_criminal_record_app.figures import get_figures
from usa_criminal_record_app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['POST'])
def index():

    year = 2019
    offense = 'All offenses'

    # get form values
    if request.method == 'POST':
        year = request.form.get('year')
        offense = request.form.get('offense')
    # get figures
    figures = get_figures(year, offense)

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figures_json = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', ids=ids, figuresJSON=figures_json)