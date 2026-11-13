class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=deque()
        b=deque()
        for c in s:
            if c!='#':
                a.append(c)
            elif a:
                a.pop()
        for c in t:
            if c!='#':
                b.append(c)
            elif b:
                b.pop()
        return "".join(a)=="".join(b)
