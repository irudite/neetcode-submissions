class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        rate = r

        while l <= r:
            curr = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p) / curr)

            if time <= h:
                rate = curr
                r = curr - 1
            else:
                l = curr + 1

        return rate