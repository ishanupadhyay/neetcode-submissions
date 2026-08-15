class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary = {}

        for i in range(len(nums)):

            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
        
        sorted_list = sorted(dictionary.keys(), key = lambda x : dictionary[x], reverse=True)
        return sorted_list[:k]
