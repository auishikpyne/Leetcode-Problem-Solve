class Solution:
    def repeatedCharacter(self, s: str) -> str:
        set_s = set()
        for x in s:
            if x in set_s:
                return x
            else:
                set_s.add(x)
        