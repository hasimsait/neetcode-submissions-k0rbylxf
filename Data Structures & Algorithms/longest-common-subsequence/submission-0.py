class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo={}
        c=set()
        d=set()
        for t in text1:
            c.add(t)
        for a in text2:
            if a in c:
                d.add(a)
        a=[]
        b=[]
        for x in text1:
            if x in d:
                a.append(x)
        for y in text2:
            if y in d:
                b.append(y)
        #x=[text1-(text1/text2)]
        #y=[text2-(text1/text2)]
        def dfs(i,j):
            if i==len(a) or j==len(b):return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if a[i]==b[j]:
                memo[(i,j)] = 1+dfs(i+1,j+1)
            else:
                memo[(i,j)]= max(dfs(i+1,j),dfs(i,j+1))
            return memo[(i,j)]
        return dfs(0,0)