import flask
import os
import waitress
import json
from flask import request
from hobartairport_com_au import HobartAirport as YMHB
app = flask.Flask(__name__)

@app.route('/')
def index():
    airport_requested = request.args.get("airport")
    if airport_requested == "YMHB":
        airport = YMHB()
        flights = []
        for flight in airport.flights():
            flights.append(flight.todict())
        return json.dumps(flights, indent=4)
    else:
        return "[]"

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 5000))
     waitress.serve(app, port=port)
