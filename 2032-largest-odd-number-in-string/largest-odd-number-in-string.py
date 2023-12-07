class Solution:
    def largestOddNumber(self, num: str) -> str:
        r = len(num) - 1
        while r >= 0 and not int(num[r]) % 2:
            r-=1
        return num[:r+1]




        