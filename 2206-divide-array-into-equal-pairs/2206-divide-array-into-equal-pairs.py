class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
    
        for value in dic.values():
            if value % 2 != 0: 
                return False
        else:
            return True
    