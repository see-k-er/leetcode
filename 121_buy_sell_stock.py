class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #using two pointer technique
        left = 0 #buy
        right = 1 #sell
        profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                temp = prices[right] - prices[left]
                profit = max(profit, temp)
            else: 
                left = right
            right += 1
        
        return profit
