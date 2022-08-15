class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        lst = []
        for num in range(1, len(sorted_arr)):
            lst.append(abs(sorted_arr[num] - sorted_arr[num-1]))
        min_diff = min(lst)
        final_result = []
        for num in range(1, len(sorted_arr)):
            if (abs(sorted_arr[num] - sorted_arr[num-1])) == min_diff: 
                final_result.append([sorted_arr[num-1],sorted_arr[num]])
        return final_result