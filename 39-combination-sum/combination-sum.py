class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
        def dfs(currIndex, combSum, arr, result):
            if combSum == target:
                result.append(list(arr))
                print(arr)
                return 
            elif combSum > target:
                return
            for g in range(currIndex, len(candidates)):
                arr.append(candidates[g])
                combSum += candidates[g]
                dfs(g, combSum, arr, result)
                arr.pop()
                combSum -= candidates[g]
            return result
        return dfs(0, 0, [], [])


