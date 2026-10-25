class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        sc=0
        tokens.sort()
        l,r=0,len(tokens)-1
        while l<r:
            if power>=tokens[l]:
                sc+=1
                power-=tokens[l]
                l+=1
            elif sc>0:
                sc-=1
                power+=tokens[r]
                r-=1
            else:
                break
        if l==r and power>=tokens[l]:
            sc+=1
        return sc


