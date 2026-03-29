class MinStack:

    def __init__(self):
        self.mins = []
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        a=self.getMin()
        if a is None:
            a=val
        self.mins.append(min(a,val))
        

    def pop(self) -> None:
        del self.st[-1]
        del self.mins[-1]

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        if len(self.mins)==0:
            return None
        return self.mins[-1]
        
