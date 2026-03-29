class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss={}
        for c in s:
            if c not in ss:
                ss[c]=0
            ss[c]+=1
        for c in t:
            if c not in ss or ss[c]==0:
                return False
            else: ss[c]-=1
        for k in ss:
            if ss[k]!=0:
                return False
        return True