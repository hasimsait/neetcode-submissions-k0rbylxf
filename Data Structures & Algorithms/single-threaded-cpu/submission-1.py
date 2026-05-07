class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        a=[]
        r = []
        ctime = 0
        for x in range(len(tasks)):
            heapq.heappush(a,(tasks[x][0],tasks[x][1],x))
        while len(a)>0:
            t=[]
            task=heapq.heappop(a)
            while task[0]<=ctime and len(a)>0:
                heapq.heappush(t,(task[1],task[2],task[0]))
                task=heapq.heappop(a)
            if len(t)>0 and task[0]>ctime:
                #avoid idling for task
                heapq.heappush(a,task)
                #pick from t
                todo = heapq.heappop(t)
                ctime = max(ctime,todo[2])+todo[0]
                r.append(todo[1])
                for task in t:
                    heapq.heappush(a,(task[2],task[0],task[1]))
            elif len(t)==0:
                #do task, either last or all require idling
                ctime = max(ctime,task[0])+task[1]
                r.append(task[2])
            elif task[0]<=ctime:
                heapq.heappush(t,(task[1],task[2],task[0]))
                #pick from t, t is entire a
                while len(t)>0:
                    todo = heapq.heappop(t)
                    ctime = max(ctime,todo[2])+todo[0]
                    r.append(todo[1])
            else:
                print(a,t,"this should never happen")
                return r
        return r


        
        #start #length #index
