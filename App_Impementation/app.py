from flask import Flask, render_template, request, jsonify
import json
from flask_bootstrap import Bootstrap4
import requests

app = Flask(__name__)

bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/tdih')
def tdih():
    return render_template('tdih.html')

@app.route('/countries')
def countries():
    return render_template('countries.html')

# Sent by calendar input form on TDIH page. Provides month and day,
# receives json object in return containing events on that day from
# microservice.
@app.route('/events', methods=['POST'])
def get_events():
    month = int(request.form['inputMonth'])
    day = int(request.form['inputDay'])
    data = {"month": month, "day": day}
    response = requests.get('http://localhost:5100/events', json=data)
    response = json.loads(response.text)
    response["items"] = len(response["events"])
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)