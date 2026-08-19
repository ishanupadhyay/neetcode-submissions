class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        
        if len(arr) == 0:
            return 0

        count = 1
        maxcount = 1
        
        for i in range(1, len(arr)):

            if arr[i] == arr[i - 1] + 1:
                count += 1
                maxcount = max(maxcount, count)

            else:
                count = 1 

        return maxcount
        
        
        