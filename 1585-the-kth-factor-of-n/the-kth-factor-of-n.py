class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr = []
        for g in range(1, n+1):
            if n%g==0:
                arr.append(g)
        if len(arr) >= k:
            return arr[k-1]
        else:
            return -1
