class Solution:
    def pivotInteger(self, n: int) -> int:
        cur = 0 
        while cur + n != ((n * (n+1)) // 2):
            cur += n
            n -= 1
            if n == 0:
                return -1
        return n 
        
        