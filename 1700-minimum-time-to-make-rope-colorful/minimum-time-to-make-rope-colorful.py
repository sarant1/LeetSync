class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        prev = ""
        prevAmt = 0
        for i in range(len(colors)):
            if colors[i] == prev:
                ans+=min(neededTime[i], prevAmt)
                prevAmt = max(neededTime[i], prevAmt)
            else:
                prevAmt = neededTime[i]
            prev = colors[i]
        return ans
        