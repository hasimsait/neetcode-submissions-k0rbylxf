class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def s(n):
            return s((n-1)//26)+chr(ord('A') + ((n-1)%26)) if n>0 else ''
        return s(columnNumber)