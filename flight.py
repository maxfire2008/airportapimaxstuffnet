import datetime
class Flight:
    def __init__(self,time,est_time,arrival_departure,aircraft,airline,location,terminal,gate,flight_number,cancelled):
        self._time=time
        self._est_time=est_time
        self._arrival_departure=arrival_departure
        self._aircraft=aircraft
        self._airline=airline
        self._location=location
        self._terminal=terminal
        self._gate=gate
        self._flight_number=flight_number
        self._cancelled=cancelled
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
    @property
    def terminal(self):
        return self._terminal
    @property
    def gate(self):
        return self._gate
    @property
    def flight_number(self):
        return self._flight_number
    @property
    def cancelled(self):
        return self._cancelled
