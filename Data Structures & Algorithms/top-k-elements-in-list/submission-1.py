class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary = {}

        for i in range(len(nums)):

            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
        
        return heapq.nlargest(k, dictionary.keys(), key=dictionary.get)
