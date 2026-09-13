class RandomizedSet:

    def __init__(self):
        self.e={}
        self.l=[]
        self.c=0

    def insert(self, val: int) -> bool:
        if val not in self.e:
            self.c+=1
            self.e[val]=len(self.l)
            self.l.append(val)
            return True
        return False

    def cleanup(self):
        c,l=0,0
        while c<len(self.l):
            if self.l[c]==None:
                continue
            else:
                self.l[l]=self.l[c]
                l+=1
            c+=1
        self.c=l
        self.l[:]=self.l[:l]
            
    def remove(self, val: int) -> bool:
        if val in self.e:
            del self.e[val]
            self.c-=1
            return True
            if 2*self.c<len(self.l):
                cleanup()
        return False
        
    def getRandom(self) -> int:
        a=random.choice(self.l)
        while a not in self.e:
            a=random.choice(self.l)
        return a


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()