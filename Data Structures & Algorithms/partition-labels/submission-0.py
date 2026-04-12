class Solution:
    def partitionLabels(self, sa: str) -> List[int]:
        s=sa+"\n"#so the loop includes the last partition
        indexByLetter = {}
        for i,c in enumerate(s):
            #last occurence of c
            indexByLetter[c] = i
        i=0
        currPartitionLength=0
        res = []
        curMax = -1
        for i,c in enumerate(s):
            if i>curMax:
                res.append(currPartitionLength)
                currPartitionLength=0
            currPartitionLength+=1
            curMax = max(curMax,indexByLetter[c])
        #first partition is empty
        return res[1:]