class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        from functools import lru_cache
        cache,lArray = {},mountainArr.length()
        def getVal(i):
            if i not in cache:
                cache[i]=mountainArr.get(i)
            return cache[i]
        def bs(l, r):
            while l <= r:
                m = (l + r) // 2
                val = getVal(m)
                if val == target:
                    return m
                elif val < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        def reversebs(l, r):
            while l <= r:
                m = (l + r) // 2
                val = getVal(m)
                if val == target:
                    return m
                elif val > target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        @lru_cache(150)
        def findPeak(l,r):
            if l<0 or l>r or r>=lArray:
                return -1
            m=(l+r)//2
            isPeak = getVal(m-1)<getVal(m) and getVal(m+1)<getVal(m) if m-1>=0 and m+1<lArray else False
            if isPeak:
                if getVal(m)==target:
                    return m
                if getVal(m)<target:
                    return -1
                res=bs(l,m-1)
                if res!=-1:
                    return res
                return reversebs(m+1,r)
            if  m+1<lArray and getVal(m+1)>getVal(m) and ((m-1<0 ) or (m-1>=0 and getVal(m-1)<getVal(m))):
                #left
                if getVal(m)==target:
                    return m
                if getVal(m)<target:
                    return findPeak(m+1,r)
                else:
                    res=bs(l,m-1)
                    if res!=-1:
                        return res
                    return findPeak(m+1,r)
            else:
                #right
                if getVal(m)==target:
                    res=findPeak(l,m-1)
                    if res!=-1:
                        return res
                    return m
                if getVal(m)<target:
                    return findPeak(l,m-1)
                else:
                    res=findPeak(l,m-1)
                    if res!=-1:
                        return res
                    return reversebs(m+1,r)
        return findPeak(0,lArray-1)
            