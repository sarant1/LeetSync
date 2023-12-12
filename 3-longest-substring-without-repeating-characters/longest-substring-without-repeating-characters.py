class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0
        current = {}
        while r < len(s):
            if s[r] not in current:
                current[s[r]] = r
            else:
                l = current[s[r]] + 1 
                current = {}
                r = l
                continue
            ans = max(ans, r-l+1)
            r+=1
        return ans


        