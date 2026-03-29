class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])+1)[::-1]:
            a=True
            for k in strs:
                if len(k)>=i and k[:i]==strs[0][:i]:
                    a=True
                else:
                    a=False
                    break
            if a:
                return k[:i]
        return ""
