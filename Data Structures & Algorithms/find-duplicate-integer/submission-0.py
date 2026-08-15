class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        used = set()

        for i in range(len(nums)):
            if nums[i] in used:
                return nums[i]
            used.add(nums[i])
        return -1
            
