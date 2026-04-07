class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def p(senate,cr,cd):
            ctr,ctd = 0,0
            for i in senate:
                if i=='R':
                    ctr+=1
                else:
                    ctd+=1
            if ctr>(ctd*2):
                return "Radiant"
            if ctd>(ctr*2):
                return "Dire"
            n=[]
            for i in senate:
                if i=='R' and cr==0:
                    cd+=1
                    n.append(i)
                elif i=='D' and cd==0:
                    cr+=1
                    n.append(i)
                elif i=='R' and cr>0:
                    cr-=1
                else: cd-=1
            return p(n,cr,cd)
        return p([x for x in senate],0,0)

