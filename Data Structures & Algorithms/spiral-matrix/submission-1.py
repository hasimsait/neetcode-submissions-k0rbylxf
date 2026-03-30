class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        limits=[len(matrix[0]),len(matrix),-1,0]
        x,y,t=0,-1,0
        r=[]
        while limits[0]>limits[2] and limits[1]>limits[3]:
            d=dire[t]
            limit=limits[t]
            if t==0:
                if y==limit:
                    break
                while y<limit:
                    x+=d[0]
                    y+=d[1]
                    if y<limit:
                        r.append(matrix[x][y])
                x-=d[0]
                y-=d[1]
                limits[0]-=1
            elif t==1:
                if x==limit:
                    break
                while x<limit:
                    print(x,y)
                    x+=d[0]
                    y+=d[1]
                    if x<limit:
                        r.append(matrix[x][y])
                x-=d[0]
                y-=d[1]
                limits[1]-=1
            elif t==2:
                if y==limit:
                    break
                while y>limit:
                    x+=d[0]
                    y+=d[1]
                    if y>limit:
                        r.append(matrix[x][y])
                x-=d[0]
                y-=d[1]
                limits[2]+=1
            elif t==3:
                if x==limit:
                    break
                while x>limit:
                    x+=d[0]
                    y+=d[1]
                    if x>limit:
                        r.append(matrix[x][y])
                x-=d[0]
                y-=d[1]
                limits[3]+=1
            t+=1
            if t==4:
                t=0
        return r

       
        