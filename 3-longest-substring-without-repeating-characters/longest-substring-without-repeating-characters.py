class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        current = {}
        for r in range(len(s)):
            if s[r] in current and l <= current[s[r]]:
                l = current[s[r]] + 1
                current[s[r]] = r
            else:
                current[s[r]] = r
            ans = max(ans, r-l+1)
        return ans


        