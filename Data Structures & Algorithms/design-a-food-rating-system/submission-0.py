class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.p={}
        self.ftr={}
        self.ftc={}
        for i,c in enumerate(cuisines):
            f=foods[i]
            r=ratings[i]
            self.ftr[f]=r
            self.ftc[f]=c
            if c not in self.p:
                self.p[c]=[]
            self.p[c].append((-r,f))
        for c in self.p:
            heapq.heapify(self.p[c])
    def changeRating(self, food: str, newRating: int) -> None:
        heapq.heappush(self.p[self.ftc[food]],(-newRating,food))
        self.ftr[food]=newRating
    def highestRated(self, cuisine: str) -> str:
        t=heapq.heappop(self.p[cuisine])
        while -t[0]!=self.ftr[t[1]]:
            t=heapq.heappop(self.p[cuisine])
        heapq.heappush(self.p[cuisine],t)
        return t[1]
