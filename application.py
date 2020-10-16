from flask import Flask
from flask import render_template
from datetime import datetime
from helpers.stats_helper import StatsHelper

app = Flask(__name__)
stats_helper = StatsHelper()

@app.route('/')
def homepage():
    # HINT: Pass variables through to the HTML using Flask - https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    title = '1 Star Reviews VS Beer abv (%)'
    labels = stats_helper.get_1star_reviews_name()
    values = stats_helper.get_1star_reviews_abv()
    return render_template('index.html', todays_date=datetime.now(), title= title, labels=labels, values=values)

# HINT: This could be your first statistic!
def get_average_overall_rating():
    return stats_helper.caculate_ave_overall_rating()