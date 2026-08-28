class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            rate = l + ((r - l) // 2) 
            eaten = 0

            for p in piles:
                eaten += math.ceil(float(p) / rate) 

            if eaten <= h:
                r = rate - 1 
                res = rate
            else:
                l = rate + 1

        return res 