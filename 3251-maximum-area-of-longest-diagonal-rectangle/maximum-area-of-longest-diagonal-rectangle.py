class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        max_diag = 0
        for w, h in dimensions:
            area = w * h
            diag = sqrt(w*w + h*h) 
            if diag > max_diag:
                ans = area
                max_diag = diag
            elif diag == max_diag:
                ans = max(ans, area)
        return ans
                

        