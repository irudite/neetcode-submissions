class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0

        profit = 0

        l, r = 0, 1
        while r < length:
            profit = max(profit, prices[r] - prices[l])
            if prices[l] <= prices[r]:
                r += 1
            else: 
                l = r
                r += 1

        return profit