class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.c={}

    def get(self, key: int) -> int:
        a=-1
        if key in self.c:
            a=self.c[key]
            del self.c[key]
            self.c[key]=a
        return a

    def put(self, key: int, value: int) -> None:
        if key in self.c:
            del self.c[key]
        self.c[key]=value
        if len(self.c.keys())>self.capacity:
            a=[x for x in self.c.keys()]
            del self.c[a[0]]
        
