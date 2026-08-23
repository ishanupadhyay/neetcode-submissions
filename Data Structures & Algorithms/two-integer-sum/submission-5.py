class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            secondnum = target - nums[i]
            if secondnum in hashmap:
                return [hashmap[secondnum], i]
            else:
                hashmap[nums[i]] = i
        
        return []