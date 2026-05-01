class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wlen = len(wordList[0])
        class Word:
            def __init__(self,w):
                self.w = w
                self.neigh = set()
            def addNeigh(self,w):
                word = wordList[w]
                sw=wordList[self.w]
                a=0
                for c in range(wlen):
                    if word[c]!=sw[c]:
                        a+=1
                    if a>1:
                        return
                if a == 1:
                    self.neigh.add(w)
        wordList.append(beginWord)
        words = {}
        words[len(wordList)-1] = Word(len(wordList)-1)
        for a in range(len(wordList)-1):
            words[len(wordList)-1].addNeigh(a)
            words[a]=Word(a)
            for b in range(len(wordList)-1):
                words[a].addNeigh(b)
        stack = [(1,len(wordList)-1)]
        visited = [0 for x in range(len(wordList))]
        target = -1
        for i in range(len(wordList)):
            if wordList[i]==endWord:
                target = i
        if target == -1:
            #unreachable since node doesn't exist
            return 0
        while len(stack)!=0:
            cu=heapq.heappop(stack)
            cost = cu[0]
            wordIndex = cu[1]
            if visited[wordIndex]:
                continue
            if wordIndex == target:
                return cost
            visited[wordIndex] =1
            for x in words[wordIndex].neigh:
                if visited[x] == 0:
                    heapq.heappush(stack,(cost+1,x))
        #unreachable bc intermediate state is missing
        return 0
            



            
                

        