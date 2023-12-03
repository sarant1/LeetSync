class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            p1_x = points[i-1][0]
            p1_y = points[i-1][1] 

            p2_x = points[i][0]
            p2_y = points[i][1] 
            ans+= max(abs(p2_x-p1_x), abs(p2_y-p1_y))

        return ans

        