class Solution:
    def __init__(self):
        self.m={}
    def encode(self, longUrl: str) -> str:
        s=0
        for c in longUrl:
            s=(s+ord(c))%1000
        s=str(s)
        if s not in self.m:
            self.m[s]=[]
        self.m[s].append(longUrl)
        return s+"#"+str(len(self.m[s])-1)
    def decode(self, shortUrl: str) -> str:
        a=shortUrl.split('#')
        if a[0] in self.m and len(self.m[a[0]])>int(a[1]):
            return self.m[a[0]][int(a[1])]
        return ""
