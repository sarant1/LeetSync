class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0
        profit = 0
        for n in nums:
            profit = max(rob1+n,rob2) 
            rob1 = rob2
            rob2 = profit
        return profit


