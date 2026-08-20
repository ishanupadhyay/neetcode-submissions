class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        maxlength = 0
        for i in arr:
            if i - 1 not in arr:
                length = 1
                while i + 1 in arr:
                    i += 1
                    length = length + 1
                
                maxlength = max(length, maxlength)

        return maxlength