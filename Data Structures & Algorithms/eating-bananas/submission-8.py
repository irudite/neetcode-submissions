class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        
        while l <= r:
            rate = 0
            mid = l + ((r - l) // 2)
            for p in piles:
                rate += math.ceil(p / mid)
            if rate <= h:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1

        return res
                
