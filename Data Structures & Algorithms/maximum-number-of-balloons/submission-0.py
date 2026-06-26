class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a={}
        for c in "balon":
            a[c]=0
        for c in text:
            if c in a:
                a[c]+=1
        ctr = 0
        ptr = 0
        while ctr<len(text)//7:
            if a["balloon"[ptr]]<1:
                return ctr
            else:
                a["balloon"[ptr]]-=1
                ptr +=1
                if ptr==len("balloon"):
                    ptr = 0
                    ctr+=1
        return ctr
                    
