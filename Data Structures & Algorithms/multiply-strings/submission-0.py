class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def toInt(num,prev):
            if num=="":
                return 0
            if len(num)==1:
                return prev*10 + (ord(num[0])-ord('0'))
            else:
                return toInt(num[1:],prev*10+(ord(num[0])-ord('0')))
        return str(toInt(num1,0)*toInt(num2,0))