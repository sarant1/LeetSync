class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0 
        for g in range(n, 0, -1):
            if n%g==0:
                count += 1
            if count == k:
                return n//g
        return -1
