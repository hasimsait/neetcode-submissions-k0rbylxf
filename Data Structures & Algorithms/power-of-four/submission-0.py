class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n.bit_count()==1 and (n & 0x55555555) == n
