class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = 0

        while l <= r:
            time = 0
            rate = (l + r) // 2

            for p in piles:
                time += math.ceil(p / rate)

            if time <= h:
                ans = rate
                r = rate - 1
            else:
                l = rate + 1 

        return ans