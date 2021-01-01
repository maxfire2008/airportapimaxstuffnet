import json
class Flight:
    def __init__(self,time=None,est_time=None,arrival_departure=None,aircraft=None,airline=None,location=None,flight_number=None,code_shares=None,cancelled=None,current_location=None,r=None):
        if time != None and est_time != None and arrival_departure != None and aircraft != None and airline != None and location != None and flight_number != None and code_shares != None and cancelled != None and current_location != None:
            self._time=time
            self._est_time=est_time
            self._arrival_departure=arrival_departure
            self._aircraft=aircraft
            self._airline=airline
            self._location=location
##            self._terminal=terminal
##            self._gate=gate
            self._flight_number=flight_number
            self._code_shares=code_shares
            self._cancelled=cancelled
            self._current_location=current_location
        elif r != None:
            rd = json.loads(r)
            self._time=rd["time"]
            self._est_time=rd["est_time"]
            self._arrival_departure=rd["arrival_departure"]
            self._aircraft=rd["aircraft"]
            self._airline=rd["airline"]
            self._location=rd["location"]
##            self._terminal=rd["terminal"]
##            self._gate=rd["gate"]
            self._flight_number=rd["flight_number"]
            self._code_shares=rd["code_shares"]
            self._cancelled=rd["cancelled"]
            self._current_location=rd["current_location"]
        else:
            raise TypeError
    @property
    def time(self):
        return self._time
    @property
    def est_time(self):
        return self._est_time
    @property
    def arrival_departure(self):
        return self._arrival_departure
    @property
    def aircraft(self):
        return self._aircraft
    @property
    def airline(self):
        return self._airline
    @property
    def location(self):
        return self._location
##    @property
##    def terminal(self):
##        return self._terminal
##    @property
##    def gate(self):
##        return self._gate
    @property
    def flight_number(self):
        return self._flight_number
    @property
    def code_shares(self):
        return self._code_shares
    @property
    def cancelled(self):
        return self._cancelled
    @property
    def current_location(self):
        return self._current_location
##    def __str__(self):
##        return f"{self._flight_number} is going to be seen at {self._est_time} as an {self._arrival_departure.replace('a','arrival').replace('d','departure')}."
    def __str__(self):
        return json.dumps({"time":self._time,
"est_time":self._est_time,
"arrival_departure":self._arrival_departure,
"aircraft":self._aircraft,
"airline":self._airline,
"location":self._location,
##"terminal":self._terminal,
##"gate":self._gate,
"flight_number":self._flight_number,
"code_shares":self._code_shares,
"cancelled":self._cancelled,
"current_location":self._current_location}, indent=4)
    def todict(self):
        return {"time":self._time,
"est_time":self._est_time,
"arrival_departure":self._arrival_departure,
"aircraft":self._aircraft,
"airline":self._airline,
"location":self._location,
##"terminal":self._terminal,
##"gate":self._gate,
"flight_number":self._flight_number,
"code_shares":self._code_shares,
"cancelled":self._cancelled,
"current_location":self._current_location}
    def __repr__(self):
        return "Flight("+repr(self._time)+","+repr(self._est_time)+","+repr(self._arrival_departure)+","+repr(self._aircraft)+","+repr(self._airline)+","+repr(self._location)+repr(self._flight_number)+","+repr(self._cancelled)+")"

if __name__ == "__main__":
    testflight = Flight(1609380707,1609384307,"a","738","Qantas","Perth","QF2842",["JQ28","BA2842"],False)
