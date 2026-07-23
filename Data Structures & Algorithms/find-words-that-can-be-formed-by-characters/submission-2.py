class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lcs = [0]*26
        for c in chars:
            lcs[ord(c)-ord('a')]+=1
        ct=0
        for i,w in enumerate(words):
            t=lcs.copy()
            for c in w:
                t[ord(c)-ord('a')]-=1
                if t[ord(c)-ord('a')]<0:
                    ct-=len(words[i])
                    break
            ct+=len(words[i])
            
        return ct


