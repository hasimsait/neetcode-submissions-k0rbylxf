class Solution:
    def isPalindrome(self, s: str) -> bool:
        #0 -1
        #1 -2
        #2 -3
        alphanums = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','0','1','2','3','4','5','6','7','8','9']
        x={}
        for k in alphanums:
            x[k]=0
        k=[]
        for a in s.lower():
            if a in x:
                k.append(a)
        print(k)
        for i in range(len(k)//2):
            if k[i] != k[(-1*i -1)]:
                return False
        return True