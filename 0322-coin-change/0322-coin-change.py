class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def min_coin(amount):
            if amount < 0:
                return float("inf")
            if dp[amount] == -1:
                dp[amount] = float("inf")
                for coin in coins:
                    dp[amount] = min(dp[amount], 1+min_coin(amount - coin))
                
            return dp[amount]
        
        dp = [-1]*(amount+1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
                
        if min_coin(amount) != float("inf"):
            return min_coin(amount)
        return -1
    
    # TC: O(amount*len(coins))
    #     SC: O(amount)
    #         Approach: lets say amount is 11, and we have 1, 2 and 5 coins. Now, answer will be min of (1+min_coin(amount-1), 1+min_coiin(amount-2), 1+min_coin(amount-5)). dp[amount] represents min number of coins required to reach amount.