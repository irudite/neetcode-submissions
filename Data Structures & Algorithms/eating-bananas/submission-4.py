class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        andrew = 0

        while left <= right:
            rate = (left + right) // 2
            time = 0

            for p in piles:
                time += math.ceil(float(p) / rate)

            if time <= h:
                andrew = rate
                right = rate - 1
            else:
                left = rate + 1

        return andrew