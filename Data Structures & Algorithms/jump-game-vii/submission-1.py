class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=='1':
            return False
        t=len(s)-1
        zs = []
        for i,c in enumerate(s):
            if c=='0':
                heapq.heappush(zs,i)
        def s(i):
            if i==t:
                return True
            r=0
            temp=[]
            reach = False
            st=[]
            while r<=i+maxJump and len(zs)>0:
                r=heapq.heappop(zs)
                if r<(i+minJump) or r>(i+maxJump):
                    temp.append(r)
                else:
                    st.append(r)
            while len(temp)>0:
                heapq.heappush(zs,temp.pop())
            st = st[::-1]
            while len(st)>0 and not reach:
                reach = reach or s(st.pop())
            return reach
        return s(0)