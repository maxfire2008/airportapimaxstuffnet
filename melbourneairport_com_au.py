from bs4 import BeautifulSoup
import requests
import json
import datetime
import time
from pprint import pprint
from flight import Flight

from honeybadger import honeybadger
honeybadger.configure(api_key='bb40a454')

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
        airline_mapping = {
                "SQ":"Singapore Airlines",
                "QR":"Qatar Airways",
                "EY":"Etihad Airways",
                "EK":"Emirates",
                "JQ":"Jetstar Airways",
                "QF":"Qantas",
                "VA":"Virgin Australia",
                "BI":"Royal Brunei",
                "TR":"Scoot",
                "ZL":"Rex",
                "CX":"Cathay Pacific",
                "CZ":"China Southern",
                "GA":"Garuda Indonesia"
            }
        #This required an...... um.... unothordox approach
##        aircraft_mapping = json.loads(open("melbourneairportaircraftmapping.json").read())
        aircraft_mapping = {}
        self._error_flights = []
        for arr in arrivals:
            if arr["flightNumber"][0:2] in airline_mapping:
                airline_full_name = airline_mapping[arr["flightNumber"][0:2]]
            else:
                airline_full_name = arr["flightNumber"][0:2]
                print("[YMML] Airline not recognised:",arr["flightNumber"][0:2],arr["flightNumber"])
                honeybadger.notify(exception=f"[YMML] Airline not recognised: {arr['flightNumber'][0:2]} {arr['flightNumber']}")
                self._error_flights.append(arr)
            if arr["flightNumber"] in aircraft_mapping:
                aircraft_full_name = aircraft_mapping[arr["flightNumber"]]
            else:
                aircraft_full_name = f"{airline_full_name} aircraft"
##                print("[YMML] Aircraft not recognised:",arr["flightNumber"],arr["flightNumber"])
                self._error_flights.append(arr)
            codeshare_flights = []
            for csf in arr["flightCodeshares"]:
                codeshare_flights.append(csf['flightCodeshareNumber'])
            if timenow.month > 10 and datetime.datetime.strptime(arr["date"],"%d/%m").month >= 1:
                actualschedtime = datetime.datetime.strptime(arr["scheduledTime"]+arr["date"]+str(timenow.year+1),"%H:%M%d/%m%Y")
            else:
                actualschedtime = datetime.datetime.strptime(arr["scheduledTime"]+arr["date"]+str(timenow.year),"%H:%M%d/%m%Y")
            if arr["estimatedTime"] == "":
                arr["estimatedTime"] = arr["scheduledTime"]
            if timenow.month > 10 and datetime.datetime.strptime(arr["date"],"%d/%m").month >= 1:
                actualesttime = datetime.datetime.strptime(arr["estimatedTime"]+arr["date"]+str(timenow.year+1),"%H:%M%d/%m%Y")
            else:
                actualesttime = datetime.datetime.strptime(arr["estimatedTime"]+arr["date"]+str(timenow.year),"%H:%M%d/%m%Y")
            self._flights.append(Flight(int(actualschedtime.timestamp()),
                                 int(actualesttime.timestamp()),
                                 "a",
                                 aircraft_full_name,
                                 airline_full_name,
                                 arr["airportNamesDisplay"],
                                 arr["flightNumber"],
                                 codeshare_flights,
                                 arr['statusName'] == 'CANCELLED',
                                 "Melbourne"
                                 ))
        for arr in departures:
            if arr["flightNumber"][0:2] in airline_mapping:
                airline_full_name = airline_mapping[arr["flightNumber"][0:2]]
            else:
                airline_full_name = arr["flightNumber"][0:2]
                print("[YMML] Airline not recognised:",arr["flightNumber"][0:2],arr["flightNumber"])
                honeybadger.notify(exception=f"[YMML] Airline not recognised: {arr['flightNumber'][0:2]} {arr['flightNumber']}")
                self._error_flights.append(arr)
            if arr["flightNumber"] in aircraft_mapping:
                aircraft_full_name = aircraft_mapping[arr["flightNumber"]]
            else:
                aircraft_full_name = f"{airline_full_name} aircraft"
##                print("[YMML] Aircraft not recognised:",arr["flightNumber"],arr["flightNumber"])
                self._error_flights.append(arr)
            codeshare_flights = []
            for csf in arr["flightCodeshares"]:
                codeshare_flights.append(csf['flightCodeshareNumber'])
            if timenow.month > 10 and datetime.datetime.strptime(arr["date"],"%d/%m").month >= 1:
                actualschedtime = datetime.datetime.strptime(arr["scheduledTime"]+arr["date"]+str(timenow.year+1),"%H:%M%d/%m%Y")
            else:
                actualschedtime = datetime.datetime.strptime(arr["scheduledTime"]+arr["date"]+str(timenow.year),"%H:%M%d/%m%Y")
            if arr["estimatedTime"] == "":
                arr["estimatedTime"] = arr["scheduledTime"]
            if timenow.month > 10 and datetime.datetime.strptime(arr["date"],"%d/%m").month >= 1:
                actualesttime = datetime.datetime.strptime(arr["estimatedTime"]+arr["date"]+str(timenow.year+1),"%H:%M%d/%m%Y")
            else:
                actualesttime = datetime.datetime.strptime(arr["estimatedTime"]+arr["date"]+str(timenow.year),"%H:%M%d/%m%Y")
            self._flights.append(Flight(int(actualschedtime.timestamp()),
                                 int(actualesttime.timestamp()),
                                 "d",
                                 aircraft_full_name,
                                 airline_full_name,
                                 arr["airportNamesDisplay"],
                                 arr["flightNumber"],
                                 codeshare_flights,
                                 arr['statusName'] == 'CANCELLED',
                                 "Melbourne"
                                 ))
        
    def flights(self):
        return self._flights

if __name__ == "__main__":
    startTime=time.time()
    YMML = MelbourneAirport()
    endTime=time.time()
    print("Loaded in",endTime-startTime,"seconds.")
