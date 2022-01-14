#
class Route:
    def __init__(self):
        self.__origin = ""
        self.__destination = ""
        self.__schedule = ""
        self.__seatprice = 0.0
        
    def GetOrigin(self):
        return self.__origin
    
    def SetOrigin(self, origin):
        self.__origin = origin
    
    def GetDestination(self):
        return self.__destination
        
    def SetDestination(self, destination):
        self.__destination = destination
        
    def GetSchedule(self):
        return self.__schedule
        
    def SetSchedule(self, schedule):
        self.__schedule = schedule
        
    def GetSeatPrice(self):
        return self.__seatprice
        
    def SetSeatPrice(self, seatprice):
        self.__seatprice = seatprice