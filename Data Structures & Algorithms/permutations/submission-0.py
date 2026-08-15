class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perm = []
        def backtrack(path, used):
            if len(path) == len(nums):
                perm.append(path.copy())
                return
            for each_num in nums:
                if each_num in used:
                    continue
                used.add(each_num)
                path.append(each_num)
                backtrack(path, used)
                path.remove(each_num)
                used.remove(each_num)
        
        backtrack(path = [],used = set())
        return perm


