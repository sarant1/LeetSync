class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if 0 < len(cost) <= 2:
            return min(cost)
        prevprev = cost[0]
        prev = cost[1]
        cur = 0
        for i in range(2, len(cost)):
            cur = min(cost[i]+prev, cost[i]+prevprev) 
            prevprev = prev
            prev = cur 
        return min(prevprev, prev)


            



        