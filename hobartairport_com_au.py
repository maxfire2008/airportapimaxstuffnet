from bs4 import BeautifulSoup
##import bs4
import requests
import time
import json
from pprint import pprint
from flight import Flight

from honeybadger import honeybadger
honeybadger.configure(api_key='bb40a454')

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
                           "DL":"Delta Air Lines",
                           "LA":"LATAM Airlines"}
        aircraft_mapping = {"SWM":"Fairchild Swearingen Metroliner",
                            "717":"Boeing 717",
                            "321":"Airbus A321",
                            "320":"Airbus A320",
                            "73H":"Boeing 737",
                            "SF3":"SAAB 340B",
                            "SW4":"Fairchild Swearingen Metroliner"}
        self._error_flights = []
        for arr in arrivals:
            if arr["airline"] in airline_mapping:
                airline_full_name = airline_mapping[arr["airline"]]
            else:
                airline_full_name = arr["airline"]
                print("[YMHB] Airline not recognised:",arr["airline"],arr["flight_number"])
                honeybadger.notify(exception=f'[YMHB] Airline not recognised: {arr["airline"]} {arr["flight_number"]}')
                self._error_flights.append(arr)
            pprint(arr)
            if "aircraft_type" in arr:
                if arr["aircraft_type"] in aircraft_mapping:
                    aircraft_full_name = aircraft_mapping[arr["aircraft_type"]]
                else:
                    aircraft_full_name = arr["aircraft_type"]
                    print("[YMHB] Aircraft not recognised:",arr["aircraft_type"],arr["flight_number"])
                    honeybadger.notify(exception=f'[YMHB] Aircraft not recognised: {arr["aircraft_type"]} {arr["flight_number"]}')
                    self._error_flights.append(arr)
            else:
                aircraft_full_name = airline_full_name
                print("[YMHB] Attribute \"aircraft_type\" non-existent:",arr["flight_number"])
                honeybadger.notify(exception=f'[YMHB] Attribute \"aircraft_type\" non-existent: {arr["flight_number"]}')
                self._error_flights.append(arr)
            if "codeshare_flights" in arr:
                codeshare_flights = arr["codeshare_flights"]
            else:
                codeshare_flights = []
            if "aircraft_type" not in arr or arr["aircraft_type"] != "143":
                self._flights.append(Flight(arr["scheduled_time_timestamp"],
                                     arr["estimated_time_timestamp"],
                                     "a",
                                     aircraft_full_name,
                                     airline_full_name,
                                     arr["source"],
                                     arr["flight_number"],
                                     codeshare_flights,
                                     arr["primary_remark"] == "Cancelled",
                                     "Hobart"
                                     ))
        for arr in departures:
            if arr["airline"] in airline_mapping:
                airline_full_name = airline_mapping[arr["airline"]]
            else:
                airline_full_name = arr["airline"]
                print("[YMHB] Airline not recognised:",arr["airline"],arr["flight_number"])
                honeybadger.notify(exception=f'[YMHB] Airline not recognised: {arr["airline"]} {arr["flight_number"]}')
                self._error_flights.append(arr)
            if "aircraft_type" in arr:
                if arr["aircraft_type"] in aircraft_mapping:
                    aircraft_full_name = aircraft_mapping[arr["aircraft_type"]]
                else:
                    aircraft_full_name = arr["aircraft_type"]
                    print("[YMHB] Aircraft not recognised:",arr["aircraft_type"],arr["flight_number"])
                    honeybadger.notify(exception=f'[YMHB] Aircraft not recognised: {arr["aircraft_type"]} {arr["flight_number"]}')
                    self._error_flights.append(arr)
            else:
                aircraft_full_name = airline_full_name
                print("[YMHB] Attribute \"aircraft_type\" non-existent:",arr["flight_number"])
                honeybadger.notify(exception=f'[YMHB] Attribute \"aircraft_type\" non-existent: {arr["flight_number"]}')
                self._error_flights.append(arr)
            if "codeshare_flights" in arr:
                codeshare_flights = arr["codeshare_flights"]
            else:
                codeshare_flights = []
            if "aircraft_type" not in arr or arr["aircraft_type"] != "143":
                self._flights.append(Flight(arr["scheduled_time_timestamp"],
                                     arr["estimated_time_timestamp"],
                                     "d",
                                     aircraft_full_name,
                                     airline_full_name,
                                     arr["source"],
                                     arr["flight_number"],
                                     codeshare_flights,
                                     arr["primary_remark"] == "Cancelled",
                                     "Hobart"
                                     ))
    def flights(self):
        return self._flights

if __name__ == "__main__":
    startTime=time.time()
    YMHB = HobartAirport()
    endTime=time.time()
    print("Loaded in",endTime-startTime,"seconds.")
##    print(hba.flights)
