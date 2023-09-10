class Solution:
    def countOrders(self, n: int) -> int:

        slots = 2 * n
        ans = 1
        while slots > 0:
            total = slots * (slots-1) // 2
            ans *= total
            slots -= 2
        return ans % (10**9 + 7)

        