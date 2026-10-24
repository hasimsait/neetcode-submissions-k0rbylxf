class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s=list(s)
        for sp in spaces:
            s[sp]=" "+s[sp]
        return "".join(s)
