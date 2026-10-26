class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements =  {}

        for i, v in enumerate(nums):
            complement = target - v
            if complement in complements:
                return [complements[complement], i]
            complements[v] = i