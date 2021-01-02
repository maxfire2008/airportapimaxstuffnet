# airportapimaxstuffnet
The URL of the website is [https://airportapimaxstuffnet.wl.r.appspot.com/](https://airportapimaxstuffnet.wl.r.appspot.com/)

My implementation can be found at [https://www.maxstuff.net/planespot/](https://www.maxstuff.net/planespot/)

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

List of api endpoints and third party:
* [https://airportapimaxstuffnet.wl.r.appspot.com/](https://airportapimaxstuffnet.wl.r.appspot.com/)
* [http://airportapi.maxstuff.net](http://airportapi.maxstuff.net) **NOTE USES HTTP**

**If you decide to host this project please add a PR to this page!** 
