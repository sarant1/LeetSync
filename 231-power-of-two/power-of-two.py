class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = bin(n)[2:]
        if num.count("1") == 1 and n > 0:
            return True
        return False
        