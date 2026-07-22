class LFUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        self.frBK = {}
        self.c = capacity

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        f = self.frBK[key]
        del self.frBK[key]
        self.frBK[key]=f+1 #force it up for recency
        return self.kv[key]

    def put(self, key: int, value: int) -> None:
        if self.c<=len(self.kv) and key not in self.kv:
            minFr,minK = -1,-1
            for k in self.frBK:
                if minFr == -1 or self.frBK[k] < minFr:
                    minFr = self.frBK[k]
                    minK = k
            del self.frBK[minK]
            del self.kv[minK]
        self.kv[key]=value
        if key not in self.frBK:
            self.frBK[key] = 0
        self.frBK[key]+=1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)