class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def func(day, allow_sell, trans):
            if trans == 2 or day == len(prices):
                return 0
            if (day, allow_sell, trans) not in dp:
                if allow_sell:
                    dp[(day, allow_sell, trans)] = max(prices[day]+func(day+1, not allow_sell, trans+1), func(day+1, allow_sell, trans))
                else:
                    dp[(day, allow_sell, trans)] = max(-prices[day]+func(day+1, not allow_sell, trans), func(day+1, allow_sell, trans))
            return dp[(day, allow_sell, trans)]
        
        dp = dict()
        return func(0, False, 0)
        