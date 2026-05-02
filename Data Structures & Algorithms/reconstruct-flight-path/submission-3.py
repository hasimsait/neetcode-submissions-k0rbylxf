class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        class City:
            def __init__(self,name):
                self.n = name
                self.to = []
                self.avail = []
            def addFlight(self,dest):
                self.to.append(dest)
                self.avail.append(True)
        cities = {}
        for t in tickets:
            if t[0] not in cities:
                cities[t[0]]=City(t[0])
            cities[t[0]].addFlight(t[1])
        for c in cities:
            cities[c].to.sort()
        r=["JFK"]
        def d():
            if len(r)==len(tickets)+1:
                return True
            if r[-1] not in cities:
                return False
            for i in range(len(cities[r[-1]].to)):
                if cities[r[-1]].avail[i]:
                    cities[r[-1]].avail[i]=False
                    r.append(cities[r[-1]].to[i])
                    if d():
                        return True
                    else:
                        r.pop()
                        cities[r[-1]].avail[i] = True
            return False
            
        d()
        return r

