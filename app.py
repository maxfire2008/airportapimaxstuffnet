import flask
import os
import waitress
import json
from flask import request
from flask_cors import CORS
from flask import send_file, send_from_directory, safe_join, abort

from hobartairport_com_au import HobartAirport as YMHB

app = flask.Flask(__name__)
CORS(app)

airports = {
        "YMHB":[YMHB(),"Hobart International Airport"],
    }

@app.route('/')
def index():
    airport_requested = request.args.get("airport")
    if airport_requested in airports:
        airport = airports[airport_requested][0]
        flights = []
        for flight in airport.flights():
            flights.append(flight.todict())
        return json.dumps(flights, indent=4)
    else:
        airport_list = []
        for airport in airports:
            airport_list.append([airport,airports[airport][1]])
        return json.dumps(airport_list)

@app.route("/status.jpeg")
def status():
    return send_file("status.jpeg")


if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 5000))
     waitress.serve(app, port=port)
