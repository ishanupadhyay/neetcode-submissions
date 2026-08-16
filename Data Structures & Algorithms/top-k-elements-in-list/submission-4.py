class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        
        heap = []

        for num, frequency in dictionary.items():
            heapq.heappush(heap, (frequency, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for frequency, num in heap]
