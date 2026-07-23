class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lcs = [[0]*26 for w in words]
        for c in chars:
            for i in range(len(words)):
                lcs[i][ord(c)-ord('a')]+=1
        for i,w in enumerate(words):
            for c in w:
                lcs[i][ord(c)-ord('a')]-=1
                if lcs[i][ord(c)-ord('a')]<0:
                    lcs[i][0]=-1
                    break
        ct=0
        for i in range(len(words)):
            if lcs[i][0]>=0:
                ct+=len(words[i])
        return ct


