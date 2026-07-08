class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = {x for x in allowed}
        ct=0
        for w in words:
            for c in w:
                if c not in allowed:
                    ct-=1
                    break
            ct+=1
        return ct