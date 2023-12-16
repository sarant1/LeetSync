class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(j, cur, cur_list):
            if cur == target:
                ans.append(list(cur_list))
                return
            elif cur > target:
                return
            prev = -1
            for i in range(j, len(candidates)):
                if candidates[i] != prev and candidates[i] <= target:
                    cur_list.append(candidates[i])
                    dfs(i+1, cur+candidates[i], cur_list) 
                    cur_list.pop()
                    prev = candidates[i]
        dfs(0, 0, [])        
        return ans









        