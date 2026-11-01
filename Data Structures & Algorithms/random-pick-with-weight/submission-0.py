class Solution:

    def __init__(self, w: List[int]):
        self.p=[]
        for i,we in enumerate(w):
            for _ in range(we):
                self.p.append(i)

    def pickIndex(self) -> int:
        return random.choice(self.p)        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()