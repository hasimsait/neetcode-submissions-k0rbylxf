class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=set()
        for i,w in enumerate(words):
            for j,w2 in enumerate(words[i+1:]):
                if w2==w:
                    a.add(w)
                elif w2 in w:
                    a.add(w2)
                elif w in w2:
                    a.add(w)
        return [x for x in a]
        