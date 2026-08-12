class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i,j=0,len(nums)-1
        while i<=j:
            print(i,j)
            m=i+(j-i)//2
            l,r,k=nums[i],nums[j],nums[m]
            if l==target or r==target or k==target:
                return True
            #111111
            #345123
            if l<k:
                if target<k and target>l:
                    i+=1
                    j=m-1
                else:
                    i=m+1
                    j-=1
            elif l>k:
                if k<target and target<r:
                    i=m+1
                    j-=1
                else:
                    i+=1
                    j=m-1
            else:
                i+=1
                j-=1
            print(i,j)
            
        return False
        

