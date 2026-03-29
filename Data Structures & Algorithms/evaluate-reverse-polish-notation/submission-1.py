class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for token in tokens:
            if token not in ["-","+","*","/"]:
                s.append(int(token))
            else:
                if token == '-':
                    n=s[-2:]
                    s=s[:-2]
                    s.append(n[0]-n[1])
                elif token == '+':
                    n=s[-2:]
                    s=s[:-2]
                    s.append(n[0]+n[1])
                elif token == '*':
                    n=s[-2:]
                    s=s[:-2]
                    s.append(n[0]*n[1])
                elif token == '/':
                    n=s[-2:]
                    s=s[:-2]
                    s.append(int(n[0]/n[1]))
        return s[0]