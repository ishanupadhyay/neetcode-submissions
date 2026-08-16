class Solution:

    def encode(self, strs: List[str]) -> str:

        finalstr = ""

        for string in strs:
            finalstr = finalstr + str(len(string)) + '#' + string
        
        return finalstr
        

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j = j + 1
            length = int(s[i:j])

            j = j + 1

            strs.append(s[j:j + length])

            i = j + length
        return strs



