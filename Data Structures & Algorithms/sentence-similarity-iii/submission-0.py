class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1==sentence2:
            return True
        s1,s2=sentence1.split(),sentence2.split()
        if len(sentence2)>len(sentence1):
            s1,s2 = s2,s1
        elif len(sentence1)==len(sentence2):
            return False
        a,b=0,-1
        while a<len(s2):
            if s1[a]==s2[a]:
                a+=1
            else:
                break
        while b>=-len(s2):
            if s1[b]==s2[b]:
                b-=1
            else:
                break
        return a-b-1>=len(s2)

