class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        current_num = 0
        current_count = 0
        max_count = 0

        for i in nums:
            if i - 1 not in set_of_nums:
                current_num = i
                current_count = 1
            while current_num + 1 in set_of_nums:
                current_count += 1
                current_num = current_num + 1
            max_count = max(current_count, max_count)
        return max_count

        
        