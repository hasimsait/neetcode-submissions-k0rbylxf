class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        c=[0]
        cballs = 0
        for b in boxes:
            c.append(c[-1]+cballs)
            if b=='1':
                cballs+=1
        c.pop(0)
        cballs = 0
        t=[0]
        for i in range(len(boxes))[::-1]:
            t.append(t[-1]+cballs)
            if boxes[i]=='1':
                cballs+=1
        t.pop(0)
        return [c[i]+t[-i-1] for i in range(len(boxes))]
        


                
