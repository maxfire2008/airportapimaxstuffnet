from bs4 import BeautifulSoup
##import bs4
import requests
##import time
import json
##from pprint import pprint
from flight import Flight
class HobartAirport:
    def __init__(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get("https://hobartairport.com.au/flights/",headers=headers)
        pagecontent=page.content
##        pagecontent = open("hbatestsoup.txt","rb").read().decode()
        soup = BeautifulSoup(pagecontent, 'html.parser')
        self._soup = soup
        rows = list(soup.find(attrs={"id":"flights__data"}).find("tbody").children)
        self._rows=rows
        arrivals = json.loads(str(soup.findAll("script")[7]).split("\n")[3][32:-1])
        self._arrivals=arrivals
        departures = json.loads(str(soup.findAll("script")[7]).split("\n")[4][32:-1])
        self._departures=departures
        self._flights = []
        airline_mapping = {"QF":"Qantas",
                           "VA":"Virgin Australia",
                           "SH":"Sharp Airlines",
                           "JQ":"Jetstar Airways",
                           "FC":"Link Airways",
                           "NZ":"Air New Zealand",
                           "CX":"Cathay Pacific",
                           "DL":"Delta Air Lines"}
        aircraft_mapping = {"SWM":"Fairchild Swearingen Metroliner",
                            "717":"Boeing 717",
                            "321":"Airbus A321",
                            "320":"Airbus A320",
                            "73H":"Boeing 737-800",
                            "SF3":"SAAB340B"}
        self._error_flights = []
        for arr in arrivals:
            if arr["airline"] in airline_mapping:
                airline_full_name = airline_mapping[arr["airline"]]
            else:
                airline_full_name = arr["airline"]
                print("Airline not recognised:",arr["airline"],arr["flight_number"])
                self._error_flights.append(arr)
            if arr["aircraft_type"] in aircraft_mapping:
                aircraft_full_name = aircraft_mapping[arr["aircraft_type"]]
            else:
                aircraft_full_name = arr["aircraft_type"]
                print("Aircraft not recognised:",arr["aircraft_type"],arr["flight_number"])
                self._error_flights.append(arr)
            if "codeshare_flights" in arr:
                codeshare_flights = arr["codeshare_flights"]
            else:
                codeshare_flights = []
            self._flights.append(Flight(arr["scheduled_time_timestamp"],
                                 arr["estimated_time_timestamp"],
                                 "a",
                                 aircraft_full_name,
                                 airline_full_name,
                                 arr["source"],
                                 arr["flight_number"],
                                 codeshare_flights,
                                 arr["primary_remark"] == "Delayed"
                                 ))
        for arr in departures:
            if arr["airline"] in airline_mapping:
                airline_full_name = airline_mapping[arr["airline"]]
            else:
                airline_full_name = arr["airline"]
                print("Airline not recognised:",arr["airline"],arr["flight_number"])
                self._error_flights.append(arr)
            if arr["aircraft_type"] in aircraft_mapping:
                aircraft_full_name = aircraft_mapping[arr["aircraft_type"]]
            else:
                aircraft_full_name = arr["aircraft_type"]
                print("Aircraft not recognised:",arr["aircraft_type"],arr["flight_number"])
                self._error_flights.append(arr)
            if "codeshare_flights" in arr:
                codeshare_flights = arr["codeshare_flights"]
            else:
                codeshare_flights = []
            self._flights.append(Flight(arr["scheduled_time_timestamp"],
                                 arr["estimated_time_timestamp"],
                                 "d",
                                 aircraft_full_name,
                                 airline_full_name,
                                 arr["source"],
                                 arr["flight_number"],
                                 codeshare_flights,
                                 arr["primary_remark"] == "Delayed"
                                 ))
    def flights(self):
        return self._flights

if __name__ == "__main__":
    hba = HobartAirport()
##    print(hba.flights)
