class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return"\\a"
        for s in strs:
            if s == "":
                s="\\e"
        return "\\b".join(strs)


    def decode(self, s: str) -> List[str]:
        if s == "\\a":
            return []
        a=s.split("\\b")
        for x in a:
            x=x.split("\\e")

        return a