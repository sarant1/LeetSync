class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for c in nums:
                if c > i:
                    continue
                if i - c >= 0:
                    dp[i] = dp[i] + dp[i-c] 
        return dp[target]

        