class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        def s(i,j,c):
            if i<0 or i>=len(image) or j<0 or j>=len(image[0]) or image[i][j]!=c:
                return
            image[i][j]=-1
            for dx,dy in d:
                s(i+dx,j+dy,c)
        s(sr,sc,image[sr][sc])
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j]==-1:
                    image[i][j]=color
        return image

