class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        a=[set()]
        l=defaultdict(int)
        for n in nums:
            a[l[n]].add(n)
            l[n]+=1
            if l[n]==len(a):
                a.append(set())
        return [list(x) for x in a[:-1]]

