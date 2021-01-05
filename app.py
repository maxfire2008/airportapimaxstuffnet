import flask
import os
import waitress
import json
import time
from flask import request
from flask_cors import CORS
from hobartairport_com_au import HobartAirport as YMHB
from melbourneairport_com_au import MelbourneAirport as YMML

app = flask.Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

CACHE_TIME = 600

airports = {
#       ICAO    ICAO (class)    NAME          CACHE_TIME
        "YMHB":[YMHB,"Hobart International Airport",CACHE_TIME],
        "YMML":[YMML,"Melbourne Airport",CACHE_TIME]
    }

cache = {}

def retreive_flights(airport):
    global cache
    global airports
    if airport in cache and cache[airport][1] >= time.time():
        return cache[airport][0]
    else:
        print("getting cache")
        airport_item = airports[airport]
        airport_c = airport_item[0]()
        flights = []
        for flight in airport_c.flights():
            flights.append(flight.todict())
        cache[airport] = [
            json.dumps(flights, indent=4),
            time.time()+airport_item[2]
        ]
        return cache[airport][0]
    

@app.route('/')
def index():
    airport_requested = request.args.get("airport")
    if airport_requested in airports:
        return retreive_flights(airport_requested)
    else:
        airport_list = []
        for airport in airports:
            airport_list.append([airport]+airports[airport][1:])
        return json.dumps(airport_list)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


##if __name__ == "__main__":
##     app.debug = False
##     port = int(os.environ.get('PORT', 5000))
##     waitress.serve(app, port=port)
