class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1)+1)] for g in range(len(text2)+1)]
        
        for i in range(len(text2)-1, -1, -1):
            for g in range(len(text1)-1, -1,-1):
                if text2[i] == text1[g]:
                    dp[i][g] = 1 + dp[i+1][g+1]
                else:
                    dp[i][g] = max(dp[i+1][g], dp[i][g+1])
        print(dp)
        return dp[0][0]
                    

