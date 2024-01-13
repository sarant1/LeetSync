class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = [0] * 26
        t_count = [0] * 26
        for i in range(len(s)):
            s_count[ord(s[i])-ord('a')]+=1
            t_count[ord(t[i])-ord('a')]+=1
        steps = 0
        for i in range(26):
            steps += abs(s_count[i] - t_count[i])
        return steps // 2

        