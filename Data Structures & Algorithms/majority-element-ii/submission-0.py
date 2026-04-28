class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = []
        for n in nums:
            if len(a)<3:
                found = False
                for i,x in enumerate(a):
                    if x[0]==n:
                        a[i] = (a[i][0],a[i][1]+1)
                        found = True
                        break
                if found is False:
                    a.append((n,1))
            elif a[0][0]==n:
                a[0]=(a[0][0],a[0][1]+1)
            elif a[1][0]==n:
                a[1]=(a[1][0],a[1][1]+1)
            elif a[2][0]==n:
                a[2]=(a[2][0],a[2][1]+1)
            else:
                if a[0][1]<=0:
                    a[0] = (n,1)
                elif a[1][1]<=0:
                    a[1] = (n,1)
                elif a[2][1]<=0:
                    a[2] = (n,1)
                else:
                    a[0]=(a[0][0],a[0][1]-1)
                    a[1]=(a[1][0],a[1][1]-1)
                    a[2]=(a[2][0],a[2][1]-1)
        ct = [0,0,0]
        for n in nums:
            for i,c in enumerate(a):
                if n==c[0]:
                    ct[i]+=1
        t = len(nums)//3
        r=[]
        for i,c in enumerate(a):
            if ct[i]>t:
                r.append(c[0])
        return r


