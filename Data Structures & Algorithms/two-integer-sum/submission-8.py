class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):

            secondvalue = target - nums[i]

            if secondvalue in hashmap and hashmap[secondvalue] != i:

                return [hashmap[secondvalue], i]
            
            hashmap[nums[i]] = i
        
        return []
