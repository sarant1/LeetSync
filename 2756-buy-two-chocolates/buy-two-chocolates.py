class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        total = sum(heapq.nsmallest(2, prices))
        return money-total if money-total >= 0 else money
        