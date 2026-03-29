class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        l,r,v=0,0,0
        while l<len(s):
            if r<len(s) and s[r] in a:
                v=max(v,r-l)
                l=(a[s[r]]+1)
                a={}
                for x in range(l,r+1):
                    a[s[x]]=x
            elif r<len(s):
                a[s[r]]=r
            else:
                v=max(v,r-l)
                l=len(s)
            r+=1
        return v
'''
if (end<len && !strs.contains(s(end))){
                strs=strs+(s(end)->end)
            }else if(end<len) {
                maxLen = Math.max(maxLen,end-start)
                start = strs(s(end))+1
                strs= strs.filter(_._2>=start)+(s(end)->end)
                //remove the chars that are before s
            }else{
                //weve reached the end of the array cant shjift the right pts
                maxLen = Math.max(maxLen,end-start)
                start=len'''