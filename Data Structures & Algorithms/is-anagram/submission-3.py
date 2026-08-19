class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in dictionary:
                dictionary[s[i]] += 1
            else:
                dictionary[s[i]] = 1
        
        for i in t:
            if i in dictionary: 
                dictionary[i] -= 1
        
        for i in dictionary:
            if dictionary[i] != 0:
                return False
        
        return True

