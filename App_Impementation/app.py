from flask import Flask, render_template, request, make_response
from nations import nation_keys, get_nations_info
from flask_bootstrap import Bootstrap4
import json
import requests

from flask_api.status import HTTP_400_BAD_REQUEST
from flask_api.status import HTTP_200_OK
from flask_api.status import HTTP_500_INTERNAL_SERVER_ERROR

from App_Impementation.service.date_parser import DateParser

from service.events_service import EventsService

# constants
DAY = "day"
MONTH = "month"
GET = "GET"

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
    req = {"month": month, "day": day}

    try:
        events = EventsService(DateParser()).get_events(req[DAY], req[MONTH])
    except ValueError:
        return make_response(
            { "Error": "Request object contains 1 or more misconfigured attribute values" },
            HTTP_400_BAD_REQUEST
        )
    except Exception:
        return make_response(
            { "Error": "An internal server error has occurred" },
            HTTP_500_INTERNAL_SERVER_ERROR
        )

    events["items"] = len(events["events"])
    return json.dumps(events)


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
        return render_template('nation_info_base.html', nation_dropdown=nation_keys())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
