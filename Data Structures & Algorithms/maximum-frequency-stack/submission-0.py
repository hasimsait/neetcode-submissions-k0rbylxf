class FreqStack:

    def __init__(self):
        self.a=[]
        self.cts = defaultdict(int)
        self.ctr=0

    def push(self, val: int) -> None:
        heapq.heappush(self.a,(-self.cts[val],-self.ctr,val))        
        self.cts[val]+=1
        self.ctr+=1

    def pop(self) -> int:
        v=heapq.heappop(self.a)
        self.cts[v[2]]-=1
        return v[2]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()