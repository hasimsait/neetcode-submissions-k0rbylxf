class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def bCoversTC():
            for x in tc:
                if x not in b or b[x]<tc[x]:
                    return False
            return True
        tc = {x:0 for x in t}
        for x in t:
            tc[x]+=1
        b = {x:0 for x in s}
        l=0
        r=0
        minlen = len(s)+1
        minl = -1
        minr = -1
        covered=False
        while l<len(s) and r<=len(s):
            #print(s[l:r],s[minl:minr])
            if covered:
                #try striping left
                if r-l<minlen:
                    minl=l
                    minr=r
                    minlen=r-l
                b[s[l]]-=1
                l+=1
                covered = bCoversTC()
                #till no longer covered
            else:
                if r<len(s):
                    b[s[r]]+=1
                    covered = bCoversTC()
                    r+=1
                else:
                    break
        if minl!=-1:
            return s[minl:minr]
        return ""






