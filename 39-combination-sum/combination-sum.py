class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(currVal, curr, g):
            if currVal > target or g >= len(candidates):
                return
            elif currVal == target:
                ans.append(list(curr))
                return
            for i in range(g, len(candidates)):
                currVal += candidates[i]
                curr.append(candidates[i])
                dfs(currVal, curr, i)
                curr.pop()
                currVal -= candidates[i] 
        dfs(0, [], 0)
        return ans



                

        