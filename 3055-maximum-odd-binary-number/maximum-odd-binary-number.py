class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones =  "1" * (s.count("1") - 1)
        zeroes = "0" * (len(s) - len(ones)-1) 
        ans = "1" + zeroes + ones
        return ans[::-1]

        