class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        a=defaultdict(list)
        c=[False for _ in hand]
        t=len(hand)
        for i,v in enumerate(hand):
            a[v].append(i)
        cur=0
        if len(hand)%groupSize!=0:return False
        while t>0:
            while c[cur]:
                cur+=1
            b=hand[cur]
            c[cur] = True
            t-=1
            for i in range(b+1,b+groupSize):
                if i in a and len(a[i])>0:
                    picked  = a[i].pop(0)
                    c[picked]=True
                else:
                    return False
                t-=1
        return True


            