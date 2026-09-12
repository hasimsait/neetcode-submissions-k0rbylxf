class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        topk=defaultdict(int)
        for n in nums:
            if len(topk)<3 or n in topk:
                topk[n]+=1
            else:
                k=[x for x in topk]
                for x in k:
                    topk[x]-=1
                    if topk[x]==0:
                        del topk[x]
                        topk[n]=1
        k=[x for x in topk]
        ct=[0]*len(k)
        for n in nums:
            try:
                ct[k.index(n)]+=1
            except:
                continue
        t=len(nums)//3
        r=[]
        for i in range(len(k)):
            if ct[i]>t:
                r.append(k[i])
        return r

