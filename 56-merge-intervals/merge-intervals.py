class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 1:
            return intervals
        ans = []
        prev = [0, -1]
        for i in range(0, len(intervals)):
            curr = intervals[i]
            if prev[1] >= curr[1]:
                continue
            if prev[1] >= curr[0]:
                if len(ans) > 0:
                    ans.pop()
                ans.append([prev[0], curr[1]])
            else:
                ans.append(curr)
            prev = ans[-1]
        return ans    




