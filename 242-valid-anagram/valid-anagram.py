class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0] * 26
        for i in range(len(s)):
            chars[ord(s[i])-ord("a")] += 1
            chars[ord(t[i])-ord("a")] -= 1
        for i in range(len(chars)):
            if chars[i] != 0:
                return False
        return True


        