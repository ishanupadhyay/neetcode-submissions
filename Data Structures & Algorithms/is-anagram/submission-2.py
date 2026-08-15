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
        
        for i in range(len(t)):

            if t[i] not in dictionary:
                return False
            else:
                dictionary[t[i]] -= 1
        
        for i in range (len(s)):

            if dictionary[s[i]] != 0:
                return False

        return True