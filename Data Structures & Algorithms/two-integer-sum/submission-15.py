class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}

        for i, v in enumerate(nums):
            complement = target - v
            if complement in hashSet: 
                return [hashSet[complement], i]

            hashSet[v] = i
