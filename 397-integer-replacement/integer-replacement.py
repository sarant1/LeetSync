class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        def count(total, res):
            if total == 1:
                return res
            if total % 2:
                res = min(
                        count(total+1, res+1),
                        count(total-1, res+1)
                        )
            else:
                res = count(total//2, res+1)
            return res
        return count(n, 0)
            
                
        

        