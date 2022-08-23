class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1 
        lst = []
        for i,j in dic.items():
            if i == j:
                lst.append(i)
        
        if len(lst)==0:
            return '-1'
        else:
            return max(lst)
        
    