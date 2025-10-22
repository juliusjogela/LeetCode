class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins needed to make amount 0
        
        # For each amount from 1 to target amount
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                if coin <= i:
                    # Can we make amount i using this coin?
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, it's impossible
        return dp[amount] if dp[amount] != float('inf') else -1
            

        