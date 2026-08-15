class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}

        for i in range(len(nums)):
            secondnumber = target - nums[i]
            if secondnumber in dictionary and dictionary[secondnumber] != i:
                return [dictionary[secondnumber], i]
            else:
                dictionary[nums[i]] = i
        
        return []
        
