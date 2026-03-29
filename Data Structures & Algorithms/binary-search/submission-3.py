class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def s(i,j):
            print(i,j)
            if j<=i:
                return -1
            if j==i+1:
                if nums[i]!=target:
                    return -1
                return i
            if j==i+2:
                if nums[i]==target:
                    return i
                if nums[i+1]==target:
                    return i+1
                return -1
            m=i
            if (j-i)%2==0:
                m=(j-i)//2
            else:
                m=(j+1-i)//2
            if nums[i+m]==target:
                return i+m
            else:
                a=s(i,i+m)
                if a ==-1:
                    a=s(i+m,j)
                return a
        return s(0,len(nums))