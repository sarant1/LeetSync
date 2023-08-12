class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(left, right, s):
            if len(s) == n*2:
                ans.append(s)
                return
            if left < n: 
                dfs(left+1, right, s + "(")
            if left > right:
                dfs(left, right+1, s + ")")

        ans = []
        dfs(1, 0, "(")
        return ans

