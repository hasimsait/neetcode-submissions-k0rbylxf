class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wbyletter = {}
        letterbyw = {}
        c=0
        if len(pattern) != len(s.split(' ')):
            return False
        for w in s.split(' '):
            if c>=len(pattern) or (pattern[c] in wbyletter and wbyletter[pattern[c]]!=w) or (w in letterbyw and letterbyw[w]!=pattern[c]):
                    return False
            else:
                letterbyw[w] = pattern[c]
                wbyletter[pattern[c]] = w
            c+=1
        return True