class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            secondnum = target - nums[i]
            if secondnum in dictionary and dictionary[secondnum] != i:
                return [dictionary[secondnum], i]
            else:
                dictionary[nums[i]] = i
        return []