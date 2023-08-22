class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        ans = ""
        while num > 26:
            letter = (num%26) + 64 
            
            # if num is a multiple of 26 then 
            if num%26 == 0:
                letter = 90 
                num -= 1
            num = num//26 
            ans += (chr(letter))
        ans += (chr(num + 64))
        return ans[::-1]