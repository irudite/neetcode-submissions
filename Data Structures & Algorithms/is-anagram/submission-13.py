class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = [0] * 26
        idx = 0

        while idx < len(s):
            chars[ord(s[idx]) - ord('a')] += 1
            chars[ord(t[idx]) - ord('a')] -= 1
            idx += 1

        for n in chars:
            if n != 0:
                return False

        return True