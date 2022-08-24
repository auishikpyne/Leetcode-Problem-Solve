class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for char in nums:
            dic[char] = dic.get(char, 0) + 1  
            
        for i in dic: 
            if dic[i] == max(dic.values()):
                return i