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
                chars[i+1:i+1+len(str(ctr))] = list(str(ctr))
                chars[i+1+len(str(ctr))]=chars[j]
                i=i+1+len(str(ctr))
                cu=i
                ctr=1
            else:
                ctr=1
                chars[i+1]=chars[j]
                i+=1
                cu=i
            j+=1
        print(i,j,cu)
        return cu