class Solution:
    def pivotInteger(self, n: int) -> int:
        cur = 0 
        while n > 0 and cur + n != ((n * (n+1)) // 2):
            cur += n
            n -= 1
        return n if n else -1
        
        