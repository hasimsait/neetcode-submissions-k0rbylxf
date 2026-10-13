class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=0
        for w in words:
            if len(w)>=len(pref) and w[:len(pref)]==pref:
                a+=1
        return a