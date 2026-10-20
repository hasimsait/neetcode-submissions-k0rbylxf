class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if len(sentence)==0 or sentence[-1]!=sentence[0]:
            return False
        s=sentence.split()
        l=s[0][0]
        for w in s:
            if w[0]!=l:
                return False
            l=w[-1]
        return True