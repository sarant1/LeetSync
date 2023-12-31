class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        counter = [0] * 27
        ans = -1
        for i in range(len(s)):
            char = s[i]
            if counter[ord(char)-ord("a")]:
                ans = max(ans, i-counter[ord(char)-ord("a")])
            else:
                counter[ord(char)-ord("a")] = i+1
        return ans


        