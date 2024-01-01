class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i, total, cur):
            if total == target:
                ans.append(cur[:])
                return
            if i == len(candidates) or total > target:
                return
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                dfs(j, total+candidates[j], cur)
                cur.pop()
        dfs(0, 0, [])
        return ans
        