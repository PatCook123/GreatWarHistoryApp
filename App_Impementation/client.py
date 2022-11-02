import json, requests

def getevents(month, day):
    data = { "month": month, "day": day }
    response = requests.get('http://localhost:5100/events', json=data)
    response = response.json()
    for i in response['events']:
        print(i['event'], i['theater_front_campaign'], i['year'])

getevents(10, 26)