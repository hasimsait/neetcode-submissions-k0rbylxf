class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for c in s:
            if st and ((c=="D" and st[-1]=="C") or (c=="B" and st[-1]=="A")):
                st.pop(len(st)-1)
            else:
                st.append(c)
        return len(st)
            

