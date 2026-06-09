class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        a=[]
        for x in s:
            if x=='1':
                ones+=1
            a.append(ones)
        sc=0
        for x in range(len(a)-1):
            z = 1 + x - a[x]
            o = ones - a[x]
            sc = max(sc,z+o)
        return sc
