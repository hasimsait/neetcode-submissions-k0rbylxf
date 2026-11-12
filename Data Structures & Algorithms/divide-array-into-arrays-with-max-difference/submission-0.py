class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        r=[[nums[0]]]
        for n in nums[1:]:
            if len(r[-1])==3:
                r.append([n])
            else:
                if r[-1][0]+k<n:
                    return []
                r[-1].append(n)
        return r

