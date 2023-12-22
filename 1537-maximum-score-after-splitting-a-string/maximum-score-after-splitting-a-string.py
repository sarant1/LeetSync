class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        ones = s.count("1")
        zeros = 0
        for i in range(len(s)-1):
            char = s[i]
            if char == "0":
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, ones+zeros)
        return ans
                 

            
        