class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def s(i,j):
            if len(i)==0:
                return j
            if len(j)==0:
                return i
            return i[0]+s(j,i[1:])
        return s(word1,word2)
        