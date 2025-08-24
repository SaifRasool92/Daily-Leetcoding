class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):

            if(prices[i] < min_price):
                min_price = prices[i]

            elif(prices[i] - min_price > max_profit):
                max_profit = prices[i] - min_price
                
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for num in prices:
            if num > buy:
                profit = max(profit,(num-buy))
            else:
                buy = num
        return profit