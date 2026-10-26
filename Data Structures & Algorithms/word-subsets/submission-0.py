class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        offset=ord('a')
        c=[0]*26
        for w in words2:
            s=[0]*26
            for x in w:
                s[ord(x)-offset]+=1
            for x in range(26):
                c[x]=max(c[x],s[x])
        r=[]
        for w in words1:
            s=[0]*26
            for x in w:
                s[ord(x)-offset]+=1
            match=True
            for x in range(26):
                match=match and not c[x]>s[x]
            if match:
                r.append(w)
        return r

