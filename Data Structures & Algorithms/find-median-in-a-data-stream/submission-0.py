class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        heapq.heappush(self.small,999999)
        heapq.heappush(self.large,999999)


    def addNum(self, num: int) -> None:
        print(num,self.small,self.large)
        if len(self.large)==len(self.small):
            s=heapq.heappop(self.small) *-1
            if s>=num:
                heapq.heappush(self.small,num * -1)
                heapq.heappush(self.small,s * -1)
            else:
                heapq.heappush(self.small,s * -1)
                heapq.heappush(self.large,num)
        else:
            #3 79 insert 5
            #3 58 insert 7
            if len(self.large)>len(self.small):
                x=heapq.heappop(self.large)
                y=heapq.heappop(self.small) * -1
                if num<=x:
                    heapq.heappush(self.small,num * -1)
                    heapq.heappush(self.large,x)
                    heapq.heappush(self.small,y * -1)
                else:
                    heapq.heappush(self.large,num)
                    heapq.heappush(self.small,x * -1)
                    heapq.heappush(self.small,y * -1)
            #34 7 insert 1
            #34 7 insert 5
            else:
                x=heapq.heappop(self.large)
                y=heapq.heappop(self.small) * -1
                if num>=y:
                    heapq.heappush(self.large,num)
                    heapq.heappush(self.large,x)
                    heapq.heappush(self.small,y * -1)
                else:
                    heapq.heappush(self.small,num*-1)
                    heapq.heappush(self.large,x)
                    heapq.heappush(self.large,y)

    def findMedian(self) -> float:
        if len(self.large)==len(self.small):
            a=heapq.heappop(self.large)
            b=heapq.heappop(self.small)*-1
            heapq.heappush(self.large,a)
            heapq.heappush(self.small,b*-1)
            return (a+b)/2
        elif len(self.large)>len(self.small):
            a=heapq.heappop(self.large)
            heapq.heappush(self.large,a)
            return a
        else:
            b=heapq.heappop(self.small)*-1
            heapq.heappush(self.small,b*-1)
            return b

        
        