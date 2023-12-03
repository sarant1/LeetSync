class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            p1x, p1y = points[i-1][0], points[i-1][1]
            p2x, p2y = points[i][0], points[i][1]
            ans += max(abs(p2y-p1y), abs(p2x-p1x))
        return ans
        