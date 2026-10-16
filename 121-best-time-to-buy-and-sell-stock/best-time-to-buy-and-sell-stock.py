class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4
        prices = [7,1,5,3,6,4]
        """
        profit = 0 # 5
        buy = prices[0] # 1
        for price in prices: #[7,1,5,3,6,4]
            buy = min(buy, price)   # 1
            profit = max(profit, price-buy) # 2 
        if profit >= 1:
            return profit
        else:
            return 0         
            
            
           