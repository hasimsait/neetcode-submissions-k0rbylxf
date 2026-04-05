class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q=[[a,'a'],[b,'b'],[c,'c']]
        q.sort(reverse = True)
        
        def getMaxExcept(a: char) -> char:
            for i,x in enumerate(q):
                if x[0]<=0:
                    return ' '
                if x[1] !=a:
                    q[i]=[q[i][0]-1,q[i][1]]
                    q.sort(reverse = True)
                    return x[1]
            return ' '
        s=[]
        valid = True
        for i in range(2):
            a=getMaxExcept([])
            if a!=' ':
                s.append(a)
            else:
                valid=False
        while valid:
            avoid = s[-1] if s[-2]==s[-1] else '\n'
            a=getMaxExcept(avoid)
            if a!=' ':
                s.append(a)
            else:
                valid=False

        return "".join(s)
            

        
        
        
        
            

        