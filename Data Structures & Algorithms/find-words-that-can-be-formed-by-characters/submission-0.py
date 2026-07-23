class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lct = defaultdict(int)
        for ch in chars:
            lct[ch]+=1
        def canForm(w):
            t=lct.copy()
            for c in w:
                t[c]-=1
                if t[c]<0:
                    return False
            return True
        ct = 0
        for w in words:
            if len(w)<=len(chars) and canForm(w):
                ct+=len(w)
        return ct

            

