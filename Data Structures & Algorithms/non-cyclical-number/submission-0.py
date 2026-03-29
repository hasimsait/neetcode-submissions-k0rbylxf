class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def sumd(n):
            a=[int(i)*int(i) for i in str(n)]
            b=0
            for i in a:
                b+=i
            if b==1:
                return True
            elif b in seen:
                return False
            else:
                seen.add(b)
                return sumd(b)
        return sumd(n)


        