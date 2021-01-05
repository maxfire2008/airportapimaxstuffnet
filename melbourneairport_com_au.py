from bs4 import BeautifulSoup
import requests
import json
import datetime
import time
from pprint import pprint
from flight import Flight

class MelbourneAirport:
    def __init__(self):
        timenow = datetime.datetime.now()
        arrivals = []
        for day in range(3):
            daytoprocess = datetime.datetime.fromtimestamp(timenow.timestamp()+((24*60*60)*day))
            morearrivals = True
            currentarrival = 0
            while morearrivals:
                print(f"[YMML] Fetching arrival {currentarrival}/{day}")
                data={
                    "FlightType":"0",
                    "Keywords":"",
                    "AirlineCode":"",
                    "Date":datetime.datetime.strftime(daytoprocess,"%d/%m/%Y"),
                    "PartofDay":"",
                    "Page":currentarrival
                    }
                request=requests.post("https://www.melbourneairport.com.au/api/flight/GetFlights",data=data)
                self._json_body_arrivals=json.loads(request.content)
                if self._json_body_arrivals["flights"]:
                    arrivals+=self._json_body_arrivals["flights"]
                morearrivals = self._json_body_arrivals['hasNextPage']
                currentarrival+=1
        departures = []
        for day in range(3):
            daytoprocess = datetime.datetime.fromtimestamp(timenow.timestamp()+((24*60*60)*day))
            moredepartures = True
            currentdeparture = 0
            while moredepartures:
                print(f"[YMML] Fetching departure {currentdeparture}/{day}")
                data={
                    "FlightType":"1",
                    "Keywords":"",
                    "AirlineCode":"",
                    "Date":datetime.datetime.strftime(daytoprocess,"%d/%m/%Y"),
                    "PartofDay":"",
                    "Page":currentdeparture
                    }
                request=requests.post("https://www.melbourneairport.com.au/api/flight/GetFlights",data=data)
                self._json_body_departures=json.loads(request.content)
                if self._json_body_departures["flights"]:
                    departures+=self._json_body_departures["flights"]
                moredepartures = self._json_body_departures['hasNextPage']
                currentdeparture+=1
        self._arrivals=arrivals
        self._departures=departures
        self._flights = []
        airline_mapping = {}
        aircraft_mapping = {}
        self._error_flights = []
        for arr in arrivals:
            if arr["airline"] in airline_mapping:
                airline_full_name = airline_mapping[arr["flightNumber"][0:2]]
            else:
                airline_full_name = arr["flightNumber"][0:2]
                print("[YMML] Airline not recognised:",arr["flightNumber"][0:2],arr["flightNumber"])
                self._error_flights.append(arr)
            if arr["flightNumber"] in aircraft_mapping:
                aircraft_full_name = aircraft_mapping[arr["flightNumber"]]
            else:
                aircraft_full_name = "other"
                print("[YMML] Aircraft not recognised:",arr["flightNumber"],arr["flightNumber"])
                self._error_flights.append(arr)
            codeshare_flights = []
            for csf in arr["flightCodeshares"]:
                codeshare_flights.append(csf['flightCodeshareNumber'])
            self._flights.append(Flight(arr["scheduled_time_timestamp"],
                                 arr["estimated_time_timestamp"],
                                 "a",
                                 aircraft_full_name,
                                 airline_full_name,
                                 arr["source"],
                                 arr["flight_number"],
                                 codeshare_flights,
                                 arr['statusName'] == "Delayed",
                                 "Melbourne"
                                 ))
        for arr in departures:
            if arr["airline"] in airline_mapping:
                airline_full_name = airline_mapping[arr["airline"]]
            else:
                airline_full_name = arr["airline"]
                print("[YMML] Airline not recognised:",arr["airline"],arr["flight_number"])
                self._error_flights.append(arr)
            if arr["aircraft_type"] in aircraft_mapping:
                aircraft_full_name = aircraft_mapping[arr["aircraft_type"]]
            else:
                aircraft_full_name = arr["aircraft_type"]
                print("[YMML] Aircraft not recognised:",arr["aircraft_type"],arr["flight_number"])
                self._error_flights.append(arr)
            if "codeshare_flights" in arr:
                codeshare_flights = arr["codeshare_flights"]
            else:
                codeshare_flights = []
            if arr["aircraft_type"] != "143":
                self._flights.append(Flight(arr["scheduled_time_timestamp"],
                                     arr["estimated_time_timestamp"],
                                     "d",
                                     aircraft_full_name,
                                     airline_full_name,
                                     arr["source"],
                                     arr["flight_number"],
                                     codeshare_flights,
                                     arr["primary_remark"] == "Delayed",
                                     "Hobart"
                                     ))
        
    def flights(self):
        return self._flights

if __name__ == "__main__":
    startTime=time.time()
    YMML = MelbourneAirport()
    endTime=time.time()
    print(endTime-startTime)
