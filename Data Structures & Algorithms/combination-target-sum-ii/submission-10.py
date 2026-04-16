class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = {}
        mem = {}
        def c(chosen,h,last,sumc):
            if h in mem:
                return
            if sumc!=target and last==len(candidates)-1:
                return 0
            if sumc==target:
                res[h]=chosen.copy()
                mem[h]=1
                return 1
            if sumc>target:
                return 0
            else:
                ch=0
                for j in range(last+1,len(candidates)):
                    if sumc+candidates[j]<=target:
                        hn=h+pow(100,len(chosen))*candidates[j]
                        ch+=hn
                        chosen.append(candidates[j])
                        c(chosen,hn,j,sumc+candidates[j])
                        del chosen[-1]
                mem[h]=ch
                return ch
        c([],0,-1,0)
        return [res[x] for x in res]

