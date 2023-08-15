class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [100000 for _ in range(amount+1)]

        for i in range(1, amount+1):
            for c in coins:
                if i-c > 0:
                    dp[i] = min(dp[i], 1+dp[i-c])
                elif i-c == 0:
                    dp[i] = 1
        return dp[-1] if dp[-1] != dp[0] else -1 