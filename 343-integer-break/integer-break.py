class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2  


        total_threes, remainder = n // 3, n % 3 

        if remainder == 0:
            return 3 ** total_threes
        elif remainder == 1:
            return 3 ** (total_threes-1) * 4
        else:
            return 3 ** total_threes * 2



        
        