class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        x = dic.values()
        x_set = set(x)
        
        if len(x_set) == 1:
            return True
        else:
            return False
        