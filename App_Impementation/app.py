from flask import Flask, render_template, request
from nations import nation_keys, get_nations_info
from flask_bootstrap import Bootstrap4
import json
import requests

# Initialize App
app = Flask(__name__)
bootstrap = Bootstrap4(app)


# App homepage
@app.route('/')
def home():
    return render_template('homepage.html')


# This day in history page
@app.route('/tdih')
def tdih():
    return render_template('tdih.html')


# Called by this day in history page
@app.route('/events', methods=['POST'])
def get_events():
    # Form only includes month and day, both are sent to microservice
    month = int(request.form['inputMonth'])
    day = int(request.form['inputDay'])
    data = {"month": month, "day": day}
    response = requests.get('http://localhost:5100/events', json=data)

    # Response handled and appended with number of items it contains
    response = json.loads(response.text)
    response["items"] = len(response["events"])
    return json.dumps(response)


# Receives request from more_info page dropdown form, returns dict object
# from nations.py
@app.route('/more_info', methods=['POST', 'GET'])
def countries():
    if request.method == 'POST':
        if request.form.get("Select_Nation"):
            nation = request.form["nationDropdown"]
            # Return chosen nation dict object and list of nations for dropdown
            return render_template('nation_info.j2',
                                   nation=get_nations_info(nation),
                                   nation_dropdown=nation_keys())

            # Return list of nations for dropdown form on page
    if request.method == 'GET':
        return render_template('more_info.html', nation_dropdown=nation_keys())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
