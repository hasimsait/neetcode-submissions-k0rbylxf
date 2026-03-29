class MyHashSet:
    def hashOf(self,i):
        return i%1024

    def __init__(self):
        self.array = [[] for i in range(1024)]

    def add(self, key: int) -> None:
        a=self.array[self.hashOf(key)]
        if not key in a:
            a.append(key)

    def remove(self, key: int) -> None:
        a=self.array[self.hashOf(key)]
        for i,n in enumerate(a):
            if n==key:
                del self.array[self.hashOf(key)][i]
                return

    def contains(self, key: int) -> bool:
        return key in self.array[self.hashOf(key)]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)