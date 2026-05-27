class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        toDel = []
        for i,j in enumerate(triplets):
            if triplets[i][0]>target[0] or triplets[i][1]>target[1] or triplets[i][2]>target[2]:
                toDel.append(i)
        for i in toDel[::-1]:
            triplets.pop(i)
        seen = [False,False,False]
        for i in triplets:
            for j in range(3):
                if i[j]==target[j]:
                    seen[j] = True
        return not(False in seen)