class UndergroundSystem:
    def __init__(self):
        self.dcs={}
        self.customers = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        inStationName,tin=self.customers[id]
        if (inStationName,stationName) in self.dcs:
            tAvg,ct = self.dcs[(inStationName,stationName)]
            self.dcs[(inStationName,stationName)] = ((ct/(ct+1))*(tAvg+(t-tin)/ct),ct+1)
        else:
            self.dcs[(inStationName,stationName)] = (t-tin,1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.dcs[(startStation,endStation)][0]
