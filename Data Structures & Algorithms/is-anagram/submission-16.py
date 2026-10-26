class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # rather, than immediately checking the strings against each other, we should check the lengths of each string, if they don't even equal each other then we can automatically determine that the two strings aren't anagrams. 
        if len(s) != len(t):
            return False

        # what is similar about an anagrams is the amount of identical characters each one contains. we can use extra space to determine O(n) the number of characters

        # the logic behind this loop is that each string counteracts each other via increment/decrement. if they're truly anagrams, then all values contained in count should be 0
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False 

        return True