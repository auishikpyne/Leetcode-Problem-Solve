class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        res = []
        for num in nums:
            if num % 2 == 0:
                even.append(num) 
            else:
                odd.append(num)
        for num in range(int(len(nums)/2)):
            res.append(even[num])
            res.append(odd[num])

        return res
        