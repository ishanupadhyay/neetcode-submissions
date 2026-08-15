class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            secondnumber = target - nums[i]
            if secondnumber in nums and i != nums.index(secondnumber):
                return sorted([i,nums.index(secondnumber)])
        return []
        
