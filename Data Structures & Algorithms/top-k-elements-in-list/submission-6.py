class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        heap = []
        result = []
        for num in nums:

            if num in dictionary:
                dictionary[num] += 1
            
            else:
                dictionary[num] = 1
        
        for num, frequency in dictionary.items():

            heapq.heappush(heap, (frequency, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for item in heap:
            freq = item[0]
            num = item[1]
            result.append(num)
        return result
