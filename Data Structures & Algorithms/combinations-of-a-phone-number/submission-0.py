class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        def c(p:str,l:str)->List[str]:
            r=[]
            for k in a[l[0]]:
                r.append(p+k)
            if len(l)==1:
                return r
            else:
                rr=[]
                for rm in r:
                    for ra in c(rm,l[1:]):
                        print(ra)
                        rr.append(ra)
                return rr
        if digits=="":
            return []
        else:
            return c("",digits)
