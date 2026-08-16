class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # since the actual index doesn't matter, but the value of element does, we can mess with the order
        nums = sorted(nums)

        for i, n in enumerate(nums):
            # once we've sorted the array, if the initial point is already greater than 0, there's no chance of every reaching a total sum of 0
            if i >= 0 and n > 0:
                break

            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = n + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
        return res