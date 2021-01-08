from bs4 import BeautifulSoup
import requests
import time
import json
import datetime
from pprint import pprint
from flight import Flight
class HeathrowAirport:
    def __init__(self):
        arrivalsheaders = {
    'authority': 'api-dp-prod.dp.heathrow.com',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'origin': 'https://www.heathrow.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'AMCVS_FCD067055294DE7D0A490D44%40AdobeOrg=1; check=true; _gcl_au=1.1.478502998.1610071150; s_cc=true; uuid=2a62bc39-660d-47e6-9234-5898c65bf5b6; _fbp=fb.1.1610071150899.59702599; __qca=P0-1809638032-1610071150698; _cs_c=1; cd_user_id=176dfb81d9be7-0be0a0f15387be-c791039-1fa400-176dfb81d9c314; WRIgnore=true; _cs_cvars=%7B%221%22%3A%5B%22Page%20ID%22%2C%22%2Fcontent%2Fheathrow%2Fmain%2Fgb%2Fen%2Farrivals%22%5D%2C%222%22%3A%5B%22Language%22%2C%22en-GB%22%5D%2C%223%22%3A%5B%22Breadcrumb%22%2C%22Heathrow%3A%20Welcome%20to%20Heathrow%20Airport%22%5D%2C%224%22%3A%5B%22PageName%22%2C%22en%20%7C%20heathrowairport%20%7C%20en%20%7C%20arrivals%22%5D%7D; HEATHROW_ENSIGHTEN_PRIVACY_BANNER_VIEWED=1; _cs_mk=0.5887839496506497_1610078407550; AMCV_FCD067055294DE7D0A490D44%40AdobeOrg=1585540135%7CMCIDTS%7C18636%7CMCMID%7C13191565775069135360706259051256537655%7CMCAAMLH-1610683207%7C8%7CMCAAMB-1610683207%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1610085607s%7CNONE%7CvVersion%7C4.4.0; seenRecently=1; ENS_AES=%7B%22lclt%22%3A1610078408796%2C%22lcot%22%3Anull%7D; gpv_pn=en%20%7C%20heathrowairport%20%7C%20en%20%7C%20arrivals; gpv_url=https%3A%2F%2Fwww.heathrow.com%2Farrivals; mbox=PC#10ec1bb3d78b4df19a0ce6ca6406a0cb.36_0#1673323321|session#ebd1a75e92484e22941dcc2a8942a9ff#1610080267; _cs_id=a14dc271-b4fa-a717-e862-ba4238ceabf0.1610071152.3.1610078521.1610075473.1.1644235152796.Lax.0; _cs_s=12.1; __CT_Data=gpv=12&ckp=tld&dm=heathrow.com&apv_98_www16=12&cpv_98_www16=12; s_sq=baalhrprod%252Cbaalhrglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.heathrow.com%25252Farrivals%2526link%253DLast%252520Updated%25252004%25253A01%2526region%253Dflight-list-app%2526.activitymap%2526.a%2526.c',
}
        arrivalsdata = {
            "data":"2021-01-08",
            "orderBy":"localArrivalTime"
                        }
        arrivalsresponse = requests.get("https://api-dp-prod.dp.heathrow.com/pihub/flights/arrivals",
                                headers=arrivalsheaders,
                                data=arrivalsdata,
                                )
        arrivals=json.loads(arrivalsresponse.content.decode())
        
        departuresheaders = {
    'authority': 'api-dp-prod.dp.heathrow.com',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'origin': 'https://www.heathrow.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'AMCVS_FCD067055294DE7D0A490D44%40AdobeOrg=1; AMCV_FCD067055294DE7D0A490D44%40AdobeOrg=1585540135%7CMCIDTS%7C18636%7CMCMID%7C13191565775069135360706259051256537655%7CMCAAMLH-1610675948%7C8%7CMCAAMB-1610675948%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1610078348s%7CNONE%7CvVersion%7C4.4.0; check=true; _gcl_au=1.1.478502998.1610071150; s_cc=true; uuid=2a62bc39-660d-47e6-9234-5898c65bf5b6; _fbp=fb.1.1610071150899.59702599; __qca=P0-1809638032-1610071150698; _cs_c=1; cd_user_id=176dfb81d9be7-0be0a0f15387be-c791039-1fa400-176dfb81d9c314; seenRecently=1; ENS_AES=%7B%22lclt%22%3A1610076349264%2C%22lcot%22%3Anull%7D; _cs_mk=0.5418072098287836_1610076349611; gpv_pn=en%20%7C%20heathrowairport%20%7C%20en%20%7C%20arrivals%20%7C%20terminal-5%20%7C%20flight-details; gpv_url=https%3A%2F%2Fwww.heathrow.com%2Farrivals%2Fterminal-5%2Fflight-details%2FEI8806%2F08-01-2021; WRIgnore=true; _cs_cvars=%7B%221%22%3A%5B%22Page%20ID%22%2C%22%2Fcontent%2Fheathrow%2Fmain%2Fgb%2Fen%2Fdepartures%22%5D%2C%222%22%3A%5B%22Language%22%2C%22en-GB%22%5D%2C%223%22%3A%5B%22Breadcrumb%22%2C%22Heathrow%3A%20Welcome%20to%20Heathrow%20Airport%22%5D%2C%224%22%3A%5B%22PageName%22%2C%22en%20%7C%20heathrowairport%20%7C%20en%20%7C%20departures%22%5D%7D; mbox=PC#10ec1bb3d78b4df19a0ce6ca6406a0cb.36_0#1673322015|session#0961179978b0432f84f25007774cac3d#1610078208; _cs_id=a14dc271-b4fa-a717-e862-ba4238ceabf0.1610071152.3.1610077215.1610075473.1.1644235152796.Lax.0; _cs_s=9.1; __CT_Data=gpv=9&ckp=tld&dm=heathrow.com&apv_98_www16=9&cpv_98_www16=9; s_sq=baalhrprod%252Cbaalhrglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.heathrow.com%25252Fdepartures%2526link%253DLast%252520Updated%25252003%25253A40%2526region%253Dflight-list-app%2526.activitymap%2526.a%2526.c',
}
        departuresdata = {
            "data":"2021-01-08",
            "orderBy":"localDepartureTime"
                        }
        departuresresponse = requests.get("https://api-dp-prod.dp.heathrow.com/pihub/flights/departures",
                                headers=departuresheaders,
                                data=departuresdata,
                                )
        departures=json.loads(departuresresponse.content.decode())
        
        self._debug_1622=arrivals
        self._debug_2319=departures
        aircraft_mapping = {
                "32N": "Airbus A320",
                "359": "Airbus A350",
                "": "",
                "": "",
                "": "",
                "": "",
                "": ""
            }
        self._flights = []
        self._error_flights = []
        for arr in arrivals:
            try:
                if arr['flightService']['aircraftTransport']['iataTypeCode'] in aircraft_mapping:
                    aircraft_full_name = aircraft_mapping[arr['flightService']['aircraftTransport']['iataTypeCode']]
                else:
                    aircraft_full_name = arr['flightService']['aircraftTransport']['iataTypeCode']
                    print("[EGGL] Aircraft not recognised:",arr['flightService']['aircraftTransport']['iataTypeCode'],arr['flightService']['iataFlightIdentifier'])
                    self._error_flights.append(arr)
                if 'codeShareSummary' not in arr['flightService']:
                    self._flights.append(
                                    Flight(
                                        int(datetime.datetime.strptime(arr['flightService']['aircraftMovement']['route']['portsOfCall'][1]['operatingTimes']['scheduled']['local'],"%Y-%m-%dT%H:%M:%S").timestamp()),
                                        int(datetime.datetime.strptime(arr['flightService']['aircraftMovement']['route']['portsOfCall'][1]['operatingTimes']['scheduled']['local'],"%Y-%m-%dT%H:%M:%S").timestamp()),
                                        "a",
                                        aircraft_full_name,
                                        arr['flightService']['airlineParty']['name'],
                                        arr['flightService']['aircraftMovement']['route']['portsOfCall'][0]['airportFacility']['name'],
                                        arr['flightService']['iataFlightIdentifier'],
                                        [],
                                        arr['flightService']['aircraftMovement']['aircraftMovementStatus'][0]['statusCode'] == "CX",
                                        "Heathrow"
                                            )
                                        )
            except:
                None
        for arr in departures:
            try:
                if arr['flightService']['aircraftTransport']['iataTypeCode'] in aircraft_mapping:
                    aircraft_full_name = aircraft_mapping[arr['flightService']['aircraftTransport']['iataTypeCode']]
                else:
                    aircraft_full_name = arr['flightService']['aircraftTransport']['iataTypeCode']
                    print("[EGGL] Aircraft not recognised:",arr['flightService']['aircraftTransport']['iataTypeCode'],arr['flightService']['iataFlightIdentifier'])
                    self._error_flights.append(arr)
                if 'codeShareSummary' not in arr['flightService']:
                    self._flights.append(
                                    Flight(
                                        int(datetime.datetime.strptime(arr['flightService']['aircraftMovement']['route']['portsOfCall'][0]['operatingTimes']['scheduled']['local'],"%Y-%m-%dT%H:%M:%S").timestamp()),
                                        int(datetime.datetime.strptime(arr['flightService']['aircraftMovement']['route']['portsOfCall'][0]['operatingTimes']['scheduled']['local'],"%Y-%m-%dT%H:%M:%S").timestamp()),
                                        "d",
                                        aircraft_full_name,
                                        arr['flightService']['airlineParty']['name'],
                                        arr['flightService']['aircraftMovement']['route']['portsOfCall'][1]['airportFacility']['name'],
                                        arr['flightService']['iataFlightIdentifier'],
                                        [],
                                        arr['flightService']['aircraftMovement']['aircraftMovementStatus'][0]['statusCode'] == "CX",
                                        "Heathrow"
                                            )
                                        )
            except:
                None
    def flights(self):
        return self._flights

if __name__ == "__main__":
    startTime=time.time()
    EGGL = HeathrowAirport()
    endTime=time.time()
    print("Loaded in",endTime-startTime,"seconds.")
##    arr=EGGL._debug_2319[1]
