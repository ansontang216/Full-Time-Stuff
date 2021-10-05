class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        current_lowest_price = prices[0]
        for i in range(1,len(prices)):
            #buy in at the lowest price possible
            if prices[i] < current_lowest_price:
                current_lowest_price = prices[i]
            else:
                maxValue = max(maxValue,prices[i]-current_lowest_price)
        
        return maxValue