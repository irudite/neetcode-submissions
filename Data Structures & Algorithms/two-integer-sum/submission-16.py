class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in hashSet:
                return [hashSet[complement], i]

            hashSet[n] = i