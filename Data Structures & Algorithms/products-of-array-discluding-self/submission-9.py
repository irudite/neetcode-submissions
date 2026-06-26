class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1

        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n

        if zeros > 1:
            return [0] * len(nums)

        res = []
        if zeros > 0:
            for n in nums:
                if n != 0:
                    res.append(0)
                else:
                    res.append(product)
        else:
            for n in nums:
                res.append(product//n)

        return res
