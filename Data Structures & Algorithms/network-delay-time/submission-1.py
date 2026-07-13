class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        a=defaultdict(list)#source->[(time,target),...]
        for edge in times:
            a[edge[0]-1].append((edge[2],edge[1]-1))
        s=[(0,k-1)]
        received = [-1]*n
        received[k-1]=0
        while len(s)>0:
            time,node=s.pop(0)
            if received[node]>time:
                received[node]=time
            if received[node]==-1:
                received[node]=time
            for edge in a[node]:
                if received[edge[1]]>time+edge[0] or received[edge[1]]==-1:
                    heapq.heappush(s,(time+edge[0],edge[1]))
        return max(received) if min(received)==0 else -1

