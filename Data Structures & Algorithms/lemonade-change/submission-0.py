class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register={5:0,10:0,20:0}
        b=[20,10,5]
        if(len(bills)==0):
            return True
        if bills[0]!=5:
            return False
        for o in bills:
            print(o)
            register[o]+=1
            change = o-5
            i=0
            while change>0 and i<3:
                print(change)
                m= b[i]
                if m>change or register[m]==0:
                    i+=1
                elif m<=change:
                    register[m]-=1
                    change-=m
            if change>0:
                return False
        return True


