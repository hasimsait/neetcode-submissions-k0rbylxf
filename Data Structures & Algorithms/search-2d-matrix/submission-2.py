class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b,m=0,len(matrix)-1,0
        while t<=b:
            mm=(t+b)//2
            if matrix[mm][0]==target:
                return True
            elif matrix[mm][0]<target:
                m=mm
                t=mm+1
            else:
                b=mm-1
        row=matrix[m]
        t,b=0,len(row)-1
        while t<b:
            mm=(t+b)//2
            if row[mm]==target:
                return True
            elif row[mm]<target:
                t=mm+1
            else:
                b=m-1
        return  row[b]==target
