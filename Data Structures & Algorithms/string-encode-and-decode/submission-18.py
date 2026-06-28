class Solution:

    def encode(self, strs: List[str]) -> str:
        i = 0
        encoded = "" 

        while i < len(strs):
            encoded += str(len(strs[i]))  
            encoded += "#"
            encoded += strs[i]
            i += 1

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j

        return decoded