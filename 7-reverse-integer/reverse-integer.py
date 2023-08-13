class Solution:
    def reverse(self, x: int) -> int:
        num = 0 
        isNeg = False 
        if x < 0:
            isNeg = True
            x = x*-1
        multi = 1 
        y = x
        while 10 <= y:
            multi *= 10 
            y = y//10

        while 10 <= x:
            val = x % 10
            num += (val * multi)
            x = x - val
            x//=10
            multi //= 10
        num += x * multi
        if num > abs(2147483647):
            return 0
        return num if not isNeg else -1 * num 


            