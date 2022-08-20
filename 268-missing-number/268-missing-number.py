class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        lst = []
        for i in range(n+1):
            lst.append(i)
            
        return sum(lst) - sum(nums)