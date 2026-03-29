class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n={}
        for x in nums:
            if x not in n:
                n[x]=0
            n[x]+=1
        t = []
        for a in n:
            t.append((n[a],a))
        t.sort()
        for i in range(len(t)):
            t[i]=t[i][1]
        return t[-k:][::-1]

        