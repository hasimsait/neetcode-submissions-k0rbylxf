class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sc=[]
        t=0
        for op in operations:
            if op in ["+","D","C"]:
                if op=="C":
                    t-=sc[-1]
                    sc=sc[:-1]
                elif op=="D":
                    t+=sc[-1]*2
                    sc.append(sc[-1]*2)
                else:
                    t+=sc[-1]+sc[-2]
                    sc.append(sc[-1]+sc[-2])
            else:
                t+=int(op)
                sc.append(int(op))
        return t