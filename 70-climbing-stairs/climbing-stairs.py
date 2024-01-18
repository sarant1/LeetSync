class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        first_step = 1
        second_step = 1
        total = 0

        for i in range(n-1):
            total = first_step + second_step
            first_step = second_step
            second_step = total
        return total


        
        