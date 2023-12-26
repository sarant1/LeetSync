class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        cache = {}
        def count(n, amt):
            if n <= 0:
                return 1 if amt == 0 else 0
            if (n, amt) in cache:
                return cache[(n, amt)]
            res = 0
            for val in range(1, k+1):
                res = (res + count(n-1, amt-val)) % mod 
            cache[(n, amt)] = res
            return res
        return count(n, target)
