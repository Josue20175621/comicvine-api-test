from flask import Flask, render_template, request
from helpers import format_date
import urllib.request, json

app = Flask(__name__)

offset, limit = 0, 25

# API KEY
api_key = "94735a770cdac75959d1b58b72abd2dbb842add1"

@app.route("/")
def index():
    # Get latest issues
    request_url = f"https://comicvine.gamespot.com/api/issues/?api_key={api_key}&format=json&offset={offset}&field_list=cover_date,image,api_detail_url,name&limit={limit}&sort=cover_date:desc"
    with urllib.request.urlopen(request_url) as url:
        res = json.load(url)
        # Returns a dictionary
        data = res['results'] 
    
    # Pass dictionary to the template engine
    return render_template("index.html", data=data, format_date=format_date)

@app.route('/issue')
def issue_detail():
    api_detail_url = request.args.get("url")
    # Get issue details
    parameters = f"?api_key={api_key}&format=json&field_list=image,character_credits,team_credits,api_detail_url,name"
    request_url = api_detail_url + parameters

    # Character credits, team credits and location credits
    req = [('Characters', 'character_credits'),
            ('Teams', 'team_credits'),
            ('Locations', 'location_credits')]

    with urllib.request.urlopen(request_url) as u:
        res = json.load(u)
        # Returns dictionary
        data = res['results']
    
    # Pass dictionary to the template engine
    return render_template("issue_detail.html", data=data, req=req)

