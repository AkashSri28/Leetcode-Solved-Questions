class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        i, j = len(prices), 2
        dp = [[[0 for _ in range(k+1)] for _ in range(j)] for _ in range(i+1)]
        
        for trans in range(k-1, -1, -1):
            for day in range(len(prices)-1, -1, -1):
                for buy in range(1, -1, -1):
                    if buy == 0:
                        dp[day][buy][trans] = max(-prices[day]+dp[day+1][1][trans], dp[day+1][0][trans])
                    else:
                        dp[day][buy][trans] = max(prices[day]+dp[day+1][0][trans+1], dp[day+1][1][trans])
                        
        

        return dp[0][0][0]
        