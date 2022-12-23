# 122. Best Time to Buy and Sell Stock II -Medium

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        profit=0
        while(i<len(prices)-1):
            if(prices[i]<prices[i+1]):
                profit=profit+prices[i+1]-prices[i]
            i=i+1
        return profit