class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [] 
        for i in range(n):
            ans.append([])
            for j in range(m):
                ans[i].append(matrix[j][i])
        return ans



            





        