class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors+colors[:k-1]
        s=0
        prev = colors[0]
        alternating = True
        firstAlternating = 0
        for i in range(1,k):
            if colors[i]==prev:
                firstAlternating = i
            prev = colors[i]
        if firstAlternating==0:
            s+=1
        for i in range(k, len(colors)):
            if colors[i]==prev:
                firstAlternating = i
            if firstAlternating<=i-k+1:
                s+=1
            prev=colors[i]
        return s

