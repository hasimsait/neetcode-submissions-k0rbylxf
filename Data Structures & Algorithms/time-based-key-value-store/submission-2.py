class TimeMap:

    def __init__(self):
        self.mmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mmap:
            self.mmap[key]=[]
        self.mmap[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mmap:
            return ""
        values = self.mmap[key]
        #print(values)
        i,j,k=0,len(values)-1,0
        while i<=j:
            m=(i+j)//2
            #print(values[m],values[k])
            if values[m][0]==timestamp:
                return values[m][1]
            elif values[m][0]>timestamp:
                j=m-1
            else:
                k=m
                i=m+1
        return values[k][1] if values[k][0]<=timestamp else ""
        
