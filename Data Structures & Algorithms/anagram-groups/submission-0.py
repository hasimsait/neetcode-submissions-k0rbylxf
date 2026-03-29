class Solution:
    def hashv(self,s,factors):
        a=1
        for c in s:
            a*=factors[c]
        return a

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        factors={}
        a=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        for x in range(len(a)):
            factors[chr(ord('a')+x)]=a[x]
        #factors={'a':2,'b':2,'c':3...}
        x={}
        for s in strs:
            a = self.hashv(s,factors)
            if a not in x:
                x[a]=[]
            x[a].append(s)
        a=[]
        for k in x:
            a.append(x[k])
        return a