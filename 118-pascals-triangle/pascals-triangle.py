class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            curr = []
            for g in range(len(ans[i-1])+1):
                if 0 <= g-1 < len(ans[i-1]):
                    left = ans[i-1][g-1] 
                else:
                    left = 0
                if g < len(ans[i-1]):
                    right = ans[i-1][g]
                else:
                    right = 0
                curr.append(right+left)
            ans.append(curr)
        return ans if numRows else [[]]





                
                

        