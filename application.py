from flask import Flask
from flask import render_template
from datetime import datetime
from helpers.stats_helper import StatsHelper

app = Flask(__name__)
stats_helper = StatsHelper()

@app.route('/')
def homepage():
    # HINT: Pass variables through to the HTML using Flask - https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    return render_template('index.html', todays_date=datetime.now(),
                           overall_rating=get_average_overall_rating(), top5=get_top_five(),
                           low5=get_low5(), allRes = allResult(), top3Avg = top_3_Avg())

# Average Overall Rating
def get_average_overall_rating():
    return stats_helper.calculate_ave_overall_rating()

# Get Top 5
def get_top_five():
    return stats_helper.get_top5()

def get_low5():
    return stats_helper.get_low5_ave_taste()

def low5_first():
    return stats_helper.low5_first_val()

def allResult():
    return stats_helper.all_results()

def top_3_Avg():
    return stats_helper.get_top3_ave_overall_rating_brewerys()