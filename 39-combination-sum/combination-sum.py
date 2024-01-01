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
        candidates.sort()
        for i in range(len(candidates)):
            num = candidates[i]
            if num > target:
                break
            dfs(i, num, [num])
        return ans
        