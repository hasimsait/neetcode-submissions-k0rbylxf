class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        j=0
        ctr=0
        cu=0
        chars.append("eof")
        while j<len(chars):
            if chars[i]==chars[j]:
                ctr+=1
            elif ctr>1:
                eofnum = i+1+len(str(ctr))
                chars[i+1:eofnum] = list(str(ctr))
                chars[eofnum]=chars[j]
                i=eofnum
                cu=i
                ctr=1
            else:
                ctr=1
                chars[i+1]=chars[j]
                i+=1
                cu=i
            j+=1
        print(i,j,cu)
        return i