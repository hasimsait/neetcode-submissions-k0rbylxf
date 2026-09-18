class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        r=[]
        c=-1
        cl=[]
        for w in words:
            if c+1+len(w)<=maxWidth:
                cl.append(w)
                c+=1+len(w)
            else:
                if len(cl)!=1:
                    cwl = c-len(cl)+1
                    spaces = maxWidth -cwl
                    per=spaces//(len(cl)-1)
                    sep = " "*per
                    c=per*len(cl)-per+c-len(cl)+1
                    line = []
                    for wc in cl:
                        line.append(wc)
                        line.append(sep)
                        if c<maxWidth:
                            c+=1
                            line.append(" ")
                    r.append("".join(line[:-1]))
                else:
                    r.append(cl[0]+" "*(maxWidth-c))
                c=len(w)
                cl=[w]
        last = " ".join(cl)
        last+=" "*(maxWidth-len(last))
        r.append(last)
        return r
