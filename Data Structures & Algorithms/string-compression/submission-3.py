class Solution:
    def compress(self, chars: List[str]) -> int:
        def replaceStr(st,i):
            for c in st:
                chars[i]=c
                i+=1
            return i
        i,j,ctr=0,0,0
        chars.append("eof")
        while j<len(chars):
            if chars[i]==chars[j]:
                ctr+=1
            elif ctr>1:
                i = replaceStr(str(ctr),i+1)
                chars[i]=chars[j]
                ctr=1
            else:
                ctr=1
                chars[i+1]=chars[j]
                i+=1
            j+=1
        return i