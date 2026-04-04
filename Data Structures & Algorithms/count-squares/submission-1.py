class CountSquares:

    def __init__(self):
        self.pointsByX={}
        self.pointsByY={}
        self.points = []

    def add(self, point: List[int]) -> None:
        if point[0] not in self.pointsByX:
            self.pointsByX[point[0]]=[]
        self.pointsByX[point[0]].append(point[1])
        if point[1] not in self.pointsByY:
            self.pointsByY[point[1]]=[]
        self.pointsByY[point[1]].append(point[0])
        self.points.append(point)

    def count(self, p: List[int]) -> int:
        res=0
        for p2 in self.points:
            x2=p2[0]
            y2=p2[1]
            if x2!=p[0] and y2!=p[1]:
                #so we dont count the same sq thrice!
                if p[0] in self.pointsByY[y2] and p[1] in self.pointsByX[x2]:
                    a=[x for x in self.pointsByY[y2] if x==p[0]]
                    b=[y for y in self.pointsByX[x2] if y==p[1]]
                    res+=len(a)*len(b)
        return res
        
