class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        from collections import deque
        st=deque()
        def checkPop():
            if len(st)<k:
                return
            for i in range(1,k+1):
                if st[-i]!=st[-1]:
                    return
            for i in range(k):
                st.pop()
        for c in s:
            st.append(c)
            checkPop()
        return "".join(st)