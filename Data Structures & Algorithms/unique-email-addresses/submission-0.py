class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def p(s):
            n = s.split('@')
            return (n[0].split('+')[0].replace(".",""),n[1])
        return len({p(x) for x in emails})