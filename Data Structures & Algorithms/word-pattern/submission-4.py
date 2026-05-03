class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wbyletter = {}
        letterbyw = {}
        a=s.split(' ')
        if len(pattern) != len(a):
            return False
        for i in range(len(pattern)):
            w = a[i]
            l= pattern[i]
            if (l in wbyletter and wbyletter[l]!=w) or (w in letterbyw and letterbyw[w]!=l):
                    return False
            else:
                letterbyw[w] = l
                wbyletter[l] = w
        return True