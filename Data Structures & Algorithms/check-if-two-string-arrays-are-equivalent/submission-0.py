class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        while word1 and word2:
            if word1[0]=="" or word2[0]=="":
                if word1[0]=="":
                    word1=word1[1:]
                if word2[0]=="":
                    word2=word2[1:]
            elif word1[0][0]!=word2[0][0]:
                return False
            else:
                word1[0] = word1[0][1:]
                word2[0] = word2[0][1:]
        return not word1 and not word2