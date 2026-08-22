class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ct_w = 0
        for i in range(k):
            if blocks[i]=='W':
                ct_w+=1
        min_rec = ct_w
        for i in range(k,len(blocks)):
            if blocks[i-k]=='W':
                ct_w-=1
            if blocks[i] =='W':
                ct_w+=1
            min_rec = min(min_rec,ct_w)
        return min_rec


