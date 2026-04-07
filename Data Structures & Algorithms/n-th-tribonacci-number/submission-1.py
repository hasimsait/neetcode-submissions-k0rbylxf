class Solution:
    def tribonacci(self, n: int) -> int:
        if not hasattr(Solution,"x"):
            self.x={}
            self.x[0]=0
            self.x[1]=1
            self.x[2]=1
            for i in range(3,38):
                self.x[i]=self.x[i-1]+self.x[i-2]+self.x[i-3]
        return self.x[n]


