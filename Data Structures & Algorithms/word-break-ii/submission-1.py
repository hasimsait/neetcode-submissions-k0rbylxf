class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict.sort(key=len)
        mem = {}
        def search(s):
            if s not in mem:
                r=[]
                for w in wordDict:
                    if len(w)<len(s) and s[:len(w)]==w:
                        r+=[w+" "+x for x in search(s[len(w):])]
                    elif w==s:
                        r.append(w)
                mem[s]=r
            return mem[s]
        return search(s)
