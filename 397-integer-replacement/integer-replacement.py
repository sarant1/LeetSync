class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        cache = {}
        def count(total, res):
            if total == 1:
                return res
            if (total, res) in cache:
                return cache[(total, res)]
            if total % 2:
                res = min(
                        count(total+1, res+1),
                        count(total-1, res+1)
                        )
            else:
                res = count(total//2, res+1)
            cache[(total, res)] = res
            return res
        return count(n, 0)
            
                
        

        