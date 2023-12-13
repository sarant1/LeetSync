class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        cols = [0] * len(mat[0]) 
        for i in range(len(mat)):
            cur_sum = sum(mat[i])
            if cur_sum == 1:
                for j in range(len(mat[i])):
                    if mat[i][j] and not cols[j]:
                        ans+=1
                        cols[j]+=1
                    elif mat[i][j] and cols[j] == 1:
                        ans-=1
                        cols[j]+=1
            elif cur_sum >= 2:
                for j in range(len(mat[i])):
                    if mat[i][j]:
                        cols[j]+=2
        return cols.count(1) 






        