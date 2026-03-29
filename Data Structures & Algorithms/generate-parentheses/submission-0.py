class Solution:
    def generateParenthesis(self, a: int) -> List[str]:
        res= {}
        def addP(s,n):
            # you can go in (()) to l or r ()()
            # ( ( ) ( ( ) ) )
            #a b c d e f g h i
            #->i
            #( ( ) ( ( ) ) )()
            if n>0:
                for i in range(0,len(s)):
                    addP(s[0:i]+"()"+s[i:],n-1)
                    addP(s+"()",n-1)
            else:
                res[s]=1
        if a==0:
            return []
        addP("()",a-1)
        return [x for x in res]
        
        