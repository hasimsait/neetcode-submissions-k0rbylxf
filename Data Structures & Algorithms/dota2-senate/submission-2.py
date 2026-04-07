class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def p(senate,cr,cd):
            if 'D' not in senate:
                return "Radiant"
            elif 'R' not in senate:
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
            return p("".join(n),cr,cd)
        return p(senate,0,0)

