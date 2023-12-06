class Solution:
    def totalMoney(self, n: int) -> int:
        start, cur, ans,  = 1, 1, 1
        for i in range(1, n):
            if i % 7 == 0:
                start+=1
                cur = start
            else:
                cur+=1
            ans += cur
        return ans

        