class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elems=[]

    def get(self, i: int) -> int:
        return self.elems[i]

    def set(self, i: int, n: int) -> None:
        self.elems[i]=n

    def pushback(self, n: int) -> None:
        if (self.capacity>len(self.elems)):
            self.elems.append(n)
        else:
            self.resize()
            self.pushback(n)

    def popback(self) -> int:
        a = self.elems[-1]
        self.elems = self.elems[0:-1]
        return a

    def resize(self) -> None:
        self.capacity*=2


    def getSize(self) -> int:
        return len(self.elems)
        
    
    def getCapacity(self) -> int:
        return self.capacity
