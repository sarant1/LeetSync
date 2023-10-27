class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # if odd
        for i in range(len(s)):
            li, ri = i, i
            while li-1 >= 0 and ri+1 < len(s) and s[li-1] == s[ri+1]:
                li-=1
                ri+=1
            if ri-li+1 > len(res):
                res = s[li:ri+1]
        # if even
        for i in range(len(s)-1):
            li = i 
            if s[i] == s[i+1]:
                ri = i+1
            else:
                ri = i
            while li-1 >= 0 and ri+1 < len(s) and s[li-1] == s[ri+1]:
                li-=1
                ri+=1
            if ri-li+1 > len(res):
                res = s[li:ri+1]
        return res





        