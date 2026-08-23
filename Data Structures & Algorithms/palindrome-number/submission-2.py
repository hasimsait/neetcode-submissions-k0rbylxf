class Solution:
    def isPalindrome(self, x: int) -> bool:
        def getLog10(x):
            if x<10:
                return 0
            if x!=0 and x/10>1:
                return getLog10(x/10)+1
            return -1
        if x<0 or (x!=0 and x%10==0):
            return False
        if x==0:
            return True
        i,j=getLog10(x),1
        while i>=j:
            print(i,j)
            if (x//(10**i))%(10)!=(x%10**j)//10**(j-1):
                return False
            i-=1
            j+=1
        return True
