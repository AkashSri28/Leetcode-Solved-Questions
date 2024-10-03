class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[float('-inf')]*2 for _ in range(n)]
        
        def helper(day, can_buy):
            if day == n:
                return 0
            if dp[day][can_buy] == float('-inf'):
                if can_buy == 1:
                    dp[day][can_buy] = max(-prices[day]+helper(day+1, 0),  helper(day+1, 1))
                else:
                    dp[day][can_buy] = max(prices[day]+helper(day+1, 1),  helper(day+1, 0))
            return dp[day][can_buy]   
            
        
        return helper(0, 1)
        