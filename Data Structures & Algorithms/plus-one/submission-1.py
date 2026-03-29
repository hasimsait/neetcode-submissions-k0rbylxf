class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        def inc(i):
            if digits[i]==9:
                if i+1==len(digits):
                    digits.append(1)
                else:
                    inc(i+1)
                digits[i]=0

            else:
                digits[i] = digits[i]+1
        inc(0)
        digits.reverse()
        return digits
        