class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}

        for i in range(len(nums)):
            if nums[i] in dictionary:
                continue
            else:
                dictionary[nums[i]] = i
        
        for i in range(len(nums)):
            secondnumber = target - nums[i]

            if secondnumber in dictionary.keys() and dictionary[secondnumber] != i:
                if dictionary[secondnumber] < i:
                    return [dictionary[secondnumber], i]
                else:
                    return [i, dictionary[secondnumber]]
        
        return []

        
