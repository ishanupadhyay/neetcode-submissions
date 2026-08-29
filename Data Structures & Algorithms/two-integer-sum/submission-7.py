class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            secnum = target - nums[i]

            if secnum in hashmap:

                return [hashmap[secnum], i]

            hashmap[nums[i]] = i
        
        return []
