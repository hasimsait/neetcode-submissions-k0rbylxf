class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        mem ={}
        def sp(i,j,k,c1,c2,last):
            if (i,j,k,c1,c2,last) in mem:
                return mem[(i,j,k,c1,c2,last)]
            if i==len(s1) and j==len(s2):
                mem[(i,j,k,c1,c2,last)]= k==len(s3) and (c1==c2 or c1==c2-1 or c1-1==c2)
            elif i==len(s1):
                t2=c2
                if last!=2:
                    t2+=1
                mem[(i,j,k,c1,c2,last)] = s3[k:]==s2[j:] and (c1==t2 or c1==t2-1 or c1-1==t2)
            elif j==len(s2):
                t1=c1
                if last!=1:
                    t1+=1
                mem[(i,j,k,c1,c2,last)] = s3[k:]==s1[i:] and (t1==c2 or t1==c2-1 or t1-1==c2)
            elif s1[i]!=s3[k] and s2[j]!=s3[k]:
                mem[(i,j,k,c1,c2,last)] = False
            elif s1[i]==s3[k] and s2[j]!=s3[k]:
                t1=c1
                if last!=1:
                    t1+=1
                mem[(i,j,k,c1,c2,last)] = sp(i+1,j,k+1,t1,c2,1)
            elif s2[i]==s3[k] and s1[j]!=s3[k]:
                t2=c2
                if last!=2:
                    t2+=1
                mem[(i,j,k,c1,c2,last)] = sp(i,j+1,k+1,c1,t2,2)
            else:
                t1=c1
                t2=c2
                if last!=1:
                    t1+=1
                if last!=2:
                    t2+=1
                mem[(i,j,k,c1,c2,last)] = sp(i+1,j,k+1,t1,c2,1) or sp(i,j+1,k+1,c1,t2,2)
            return mem[(i,j,k,c1,c2,last)]
        return len(s1)+len(s2)==len(s3) and sp(0,0,0,0,0,0)
        
            