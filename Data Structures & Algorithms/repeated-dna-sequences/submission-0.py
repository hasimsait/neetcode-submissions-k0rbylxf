class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<11:
            return []
        seen=set()
        ans=set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                ans.add(s[i:i+10])
            seen.add(s[i:i+10])
        return list(ans)