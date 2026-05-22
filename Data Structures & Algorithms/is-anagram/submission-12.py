class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = len(s)
        s2 = len(t)

        if s1 != s2:
            return False

        anag = [0] * 26
        i =  0

        while i < s1:
            anag[ord(s[i]) - ord('a')] += 1
            anag[ord(t[i]) - ord('a')] -= 1
            i += 1

        for n in anag:
            if n != 0:
                return False

        return True