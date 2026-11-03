class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sh=[0]*(len(s)+1)
        for st,e,direction in shifts:
            d=1 if direction else -1
            sh[st]+=d
            sh[e+1]-=d
        cur,r=0,[]
        for i,c in enumerate(s):
            cur+=sh[i]
            r.append(chr(97+(ord(c)-97+cur)%26))
        return "".join(r)
