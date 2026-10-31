class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        a=[0]*26
        for c in s:
            a[ord(c)-ord('a')]+=1
        s=[]
        last=None
        lastct=0
        while c:
            maxc=-1
            for i in range(25,-1,-1):
                if a[i]>0 and not (i==last and lastct==repeatLimit):
                    maxc=i
                    break
            if maxc<0:
                break
            a[maxc] -= 1
            if maxc==last:
                lastct+=1
            else:
                lastct=1
            last=maxc
            s.append(chr(maxc+ord('a')))
        return "".join(s)

