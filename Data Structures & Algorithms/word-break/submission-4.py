class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set()
        lenmin=999
        lenmax=0
        for word in wordDict:
            words.add(word)
            lenmin = min(lenmin,len(word))
            lenmax = max(lenmax,len(word))
        mem = {}
        def c(i):
            if len(s)-i in mem: ()
            elif len(s)<=i or s[i:] in words:
                mem[len(s)-i] = True
            else:
                for j in range(lenmin,lenmax+1)[::-1]:
                    p = s[i:i+j]
                    if p in words:
                        if c(i+j):
                            mem[len(s)-i]=True
                            return True
                mem[len(s)-i]=False
            return mem[len(s)-i]
        return c(0)

            