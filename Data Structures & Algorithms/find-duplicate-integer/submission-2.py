class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = set()

        for n in nums:
            if n in duplicate:
                return n
            duplicate.add(n)

        