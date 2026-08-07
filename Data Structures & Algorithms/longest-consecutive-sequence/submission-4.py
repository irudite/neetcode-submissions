class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapping = set()
        res = 0

        for n in nums:
            mapping.add(n)

        for i, v in enumerate(nums):
            if (v - 1) not in mapping:
                length = 1
                while (v + length) in mapping:
                    length += 1
                res = max(length, res) 

        return res