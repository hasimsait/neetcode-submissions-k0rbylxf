class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        r=[]
        seen = set()
        def h(l):
            p,r=0,0
            for i in l:
                r+=(22**(p+10))*i
                p+=1
            return r
        def p(chosen):
            if len(chosen)==len(nums):
                c=[nums[x] for x in chosen]
                ha= h(c)
                if ha not in seen:
                    seen.add(ha)
                    r.append(c)
            for i in range(len(nums)):
                if i not in chosen:
                    chosen.append(i)
                    p(chosen)
                    chosen.pop()
            return
        p([])
        return r
                