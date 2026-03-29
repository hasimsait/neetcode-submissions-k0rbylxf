class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def sameDir(x,y):
            return ((x<0 and y<0) or (x>0 and y>0))
        if len(asteroids)==0:
            return 0

        c=[]
        for i in asteroids:
            if len(c)==0:
                c.append(i)
            else:
                s=c[-1]
                if sameDir(s,i) or s<0 and i>0:
                    c.append(i)
                else:
                    broken=False
                    while (len(c)>0):
                        a=c.pop()
                        if sameDir(a,i):
                            c.append(a)
                            c.append(i)
                            break
                        elif abs(a)>abs(i):
                            c.append(a)
                            break
                        elif abs(a)==abs(i):
                            broken=True
                            break
                    if len(c)==0 and broken is False:
                        c.append(i)
        return c




