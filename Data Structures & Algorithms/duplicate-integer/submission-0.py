class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_set = set()

        for i in nums:
            if i in empty_set:
                return True
            empty_set.add(i)
        
        return False
         