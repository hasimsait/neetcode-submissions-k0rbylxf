class MyHashMap:

    def __init__(self):
        self.hmap = [[] for i in range(1024)]
        

    def put(self, key: int, value: int) -> None:
        smap=self.hmap[key%1024]
        for x,i in enumerate(smap):
            if i[0]==key:
                self.hmap[key%1024][x] = [key,value]
                return
        smap.append([key,value])

    def get(self, key: int) -> int:
        smap=self.hmap[key%1024]
        for i in smap:
            if i[0]==key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        smap=self.hmap[key%1024]
        for i,c in enumerate(smap):
            if c[0]==key:
                self.hmap[key%1024][:] = smap[:i]+smap[i+1:]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)