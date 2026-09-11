class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for s in strs:
            v=list(s)
            v.sort()
            k="".join(v)
            a[k].append(s)
        return [a[x] for x in a]