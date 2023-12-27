class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9+7
        dp = [0] * (target+1)
        dp[0] = 1

        for dice in range(n):
            next_dp = [0] * (target+1)
            for dice_amt in range(1, k+1):
                for total in range(dice_amt, target+1):
                    next_dp[total] = (next_dp[total] + dp[total-dice_amt]) % mod 
            dp = next_dp
        return dp[target]

