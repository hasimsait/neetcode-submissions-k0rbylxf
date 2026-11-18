class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n=[(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1),(1,0),(-1,0)]
        r=[]
        for row in img:
            r.append(row.copy())
        for i,row in enumerate(img):
            for j,pxl in enumerate(row):
                c=1
                for nx,ny in n:
                    if i+nx>=0 and i+nx<len(img) and j+ny>=0 and j+ny<len(img[0]):
                        c+=1
                        r[i][j]+=img[i+nx][j+ny]
                r[i][j]=r[i][j]//c
        return r
