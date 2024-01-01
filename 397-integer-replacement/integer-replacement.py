class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = {}
        dp[1] = 0
        dp[0] = 0
        def count(n):
            if n in dp:
                return dp[n]
            if n % 2:
                dp[n] = min(
                    1+count(n+1),
                    1+count(n-1)
                )
            else:
                dp[n] = 1+count(n//2)
            return dp[n]
        return count(n)
            
                
        

        