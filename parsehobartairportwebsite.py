from bs4 import BeautifulSoup
import bs4
import requests
import time
import json
from pprint import pprint
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

if __name__ == "__main__":
    hba = HobartAirport()
##    print(hba.flights)
