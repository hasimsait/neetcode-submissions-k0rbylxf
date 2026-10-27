class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.p=defaultdict(int)
        c=1
        for x in [big,medium,small]:
            self.p[c]=x
            c+=1

    def addCar(self, carType: int) -> bool:
        self.p[carType]-=1
        return self.p[carType]>=0
