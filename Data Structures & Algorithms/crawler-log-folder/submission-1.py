class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s=0
        for c in logs:
            if c=="../":
                s=max(0,s-1)
            elif c=="./":
                continue
            else:
                s+=1
        return s