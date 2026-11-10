class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        r=[]
        s="123456789"
        for d in range(len(str(low)),len(str(high))+1):
            for i in range(10-d):
                n=int(s[i:i+d])
                if n>=low and n<=high:
                    r.append(n)
        return r