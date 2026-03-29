class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ibyn = {}
        res={}
        for i,n in enumerate(nums):
            if n not in ibyn:
                ibyn[n]=[]
            ibyn[n].append(i)
        for i,n in enumerate(nums):
            #find j,k st nums[j]+nums[k]=-n, k>j>i
            if i+1<len(nums)-1:
                for x,m in enumerate(nums[i+1:]):
                    j=x+i+1
                    if -1*(m+n) in ibyn:
                        target = ibyn[-1*(m+n)]
                        if target[-1]>j:
                            res[str(n)+','+str(m)+','+str(nums[target[-1]])]=[n,m,nums[target[-1]]]
        a=[]
        for r in res:
            a.append(res[r])
        return a