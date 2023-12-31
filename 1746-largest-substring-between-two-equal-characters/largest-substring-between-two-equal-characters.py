class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ans = -1
        for i in range(len(s)):
            cur = 0
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    ans = max(ans, j-i-1)
        return ans if len(set(s)) != len(s) else -1


        