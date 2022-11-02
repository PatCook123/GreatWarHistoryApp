from flask import Flask, render_template, request, jsonify
import json
from flask_bootstrap import Bootstrap4
import requests

app = Flask(__name__)

bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('homepage.j2')


@app.route('/tdih')
def tdih():
    return render_template('tdih.html')

@app.route('/events')
def getevents():
    month = request.args.get("inputMonth")
    day = request.args.get("inputDay")
    data = json.dumps({"month": month, "day": day})
    print(data)
    response = requests.get('http://localhost:5100/events', json=data)
    print(response)
    return response.text

@app.route('/events2', methods=['POST'])
def getevents2():
    month = int(request.form['inputMonth'])
    day = int(request.form['inputDay'])
    data = {"month": month, "day": day}
    response = requests.get('http://localhost:5100/events', json=data)
    response = json.loads(response.text)
    response["items"] = len(response["events"])
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)