# airportapimaxstuffnet
The URL of the website is [http://airportapi.maxstuff.net](http://airportapi.maxstuff.net)

Each endpoint returns a JSON payload.

To get avalible airports use the api endpoint.

GET `/` PAYLOAD ` `

REPSONSE `[["YMHB","Hobart International Airport"],["YMML","Tullamarine Airport"]]`

To view an airports flights use the following endpoint.

GET `/` PAYLOAD `airport=YMHB`

RESPONSE
```
{
  "time": <int (scheduled time)>,
  "est_time": <int (estimated time)>,
  "arrival_departure": <str (arrival/departure) "a"/"d">,
  "aircraft": <str (aircraft name)>,
  "airline": <str (airline)>,
  "location": <str (origin/destination respectivly arrival/departure)>,
  "flight_number": <str (flight number)>,
  "code_shares": <array (contains <str (flight number)>)>,
  "cancelled": <bool (true/false)>,
  "current_location": <str (destination/origin respectivly arrival/departure)>
}
```

This is currently running on Heroku with a python buildpack.

List of third party api endpoints:
* [http://airportapi.maxstuff.net](http://airportapi.maxstuff.net) <img src="http://airportapi.maxstuff.net/status.jpeg" height="15">

**If you decide to host this project please add a PR to this page!** 
