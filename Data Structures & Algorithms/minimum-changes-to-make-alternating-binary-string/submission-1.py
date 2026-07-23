class Solution:
    def minOperations(self, s: str) -> int:
        def sw(one):
            c=0
            for i in range(len(s)):
                if (s[i]!='1' and one) or (s[i]!='0' and not one):
                    c+=1
                one = not one
            return c

        return min(sw(True),sw(False))