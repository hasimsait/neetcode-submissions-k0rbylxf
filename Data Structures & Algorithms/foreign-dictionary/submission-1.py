class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        ind = {c:0 for word in words for c in word}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            if len(w1)>len(w2) and w1[:min(len(w1),len(w2))]==w2[:min(len(w1),len(w2))]:
                return ""
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        ind[w2[j]]+=1
                    break
        #arf app apple apg -> p->g r->p now merge to get r->p->g
        q=[c for c in ind if ind[c]==0]
        r=[]
        while q:
            c=q.pop(0)
            r.append(c)
            for n in adj[c]:
                ind[n]-=1
                if ind[n]==0:
                    q.append(n)
        if len(r)<len(ind):
            return ""
        return "".join(r)


