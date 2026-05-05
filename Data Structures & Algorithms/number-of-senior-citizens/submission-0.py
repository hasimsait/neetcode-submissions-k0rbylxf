class Solution:
    def countSeniors(self, details: List[str]) -> int:
        a=0
        for c in details:
            y=int(c[11:13])
            if y>60:
                a+=1
        return a
