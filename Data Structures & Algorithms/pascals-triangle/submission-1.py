class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def g(s):
            s=[0]+s+[0]
            t=[]
            i=1
            while i<(len(s)+1)//2:
                t.append(s[i-1]+s[i])
                i+=1
            if len(s)%2==0:
                return t+[s[i]*2]+t[::-1]
            return t+t[::-1]
        r=[[1]]
        for i in range(numRows -1):
            r.append(g(r[-1]))
        return r[:numRows]
