class Solution:
    def findMyClose(self, s:str,i)->int:
        a=0
        while i<len(s):
            x=s[i]
            if x=='[':
                a+=1
            elif x==']':
                if a==1:
                    return i
                a-=1
            i+=1
        return -1


    def decodeString(self, s: str) -> str:
        def decode(s,start,ends):
            #print(s[start:ends])
            r=[]
            i=start
            while i<ends:
                c=s[i]
                if ord(c)>=ord('a') and ord(c)<=ord('z'):
                    r.append(c)
                else:
                    #found k
                    st=i
                    while ord(c)>=ord('0') and ord(c)<=ord('9'):
                        i+=1
                        c=s[i]
                    mult = int(s[st:i])
                    end = self.findMyClose(s,i)
                    r.append(mult*decode(s,i+1,end))
                    i=end
                i+=1
            return "".join(r)
        return decode(s,0,len(s))