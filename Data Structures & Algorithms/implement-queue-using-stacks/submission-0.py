class MyQueue:

    def __init__(self):
        self.s = []
        self.p=[]

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        if len(self.p)==0:
            while len(self.s)>0:
                self.p.append(self.s.pop())
        return self.p.pop()

    def peek(self) -> int:
        if len(self.p)==0:
            while len(self.s)>0:
                self.p.append(self.s.pop())
        return self.p[-1]
        

    def empty(self) -> bool:
        return max(len(self.s),len(self.p))==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()