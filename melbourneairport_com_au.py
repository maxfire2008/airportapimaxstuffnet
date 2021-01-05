from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
from flight import Flight

class MelbourneAirport:
    def __init__(self):
        moreflights = True
        while moreflights:
            data={
                "FlightType":1,
                "Keywords":"",
                "AirlineCode":"",
                "Date":"05/01/2021",
                "PartofDay":"",
                "Page":"0"
                }
            request=requests.post("https://www.melbourneairport.com.au/api/flight/GetFlights",data=data)
            self._json_body=json.loads(request.content)
            moreflights = self._json_body['hasNextPage']
    def flights(self):
        return self._flights

if __name__ == "__main__":
    YMML = MelbourneAirport()
