class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        a=defaultdict(list)
        for i,c in enumerate(s):
            if len(a[c])>1:
                a[c][-1] = i
            else:
                a[c].append(i)
        maxD = -1
        for c in a:
            if len(a[c])>1:
                maxD=max(a[c][-1]-a[c][0]-1,maxD)
        return maxD