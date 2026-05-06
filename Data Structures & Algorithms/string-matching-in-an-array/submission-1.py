class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=set()
        for i,w in enumerate(words):
            for j in range(i+1,len(words)):
                w2=words[j]
                if w2==w:
                    a.add(w)
                elif w2 in w:
                    a.add(w2)
                elif w in w2:
                    a.add(w)
        return [x for x in a]
        