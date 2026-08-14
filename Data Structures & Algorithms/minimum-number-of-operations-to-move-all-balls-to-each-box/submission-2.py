class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        c=[0]
        cballs = 0
        for b in boxes:
            c.append(c[-1]+cballs)
            if b=='1':
                cballs+=1
        cballs = 0
        curs=0
        for i in range(len(boxes))[::-1]:
            curs+=cballs
            c[i+1]+=curs
            if boxes[i]=='1':
                cballs+=1
        return c[1:]
        


                
