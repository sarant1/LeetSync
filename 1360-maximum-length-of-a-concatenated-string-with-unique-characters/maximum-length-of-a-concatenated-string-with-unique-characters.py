class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(cur, i):
            temp_cur = "".join(cur)
            if len(set(temp_cur)) != len(temp_cur):
                return 0
            amt = len(temp_cur)
            for j in range(i, len(arr)):
                cur.append(arr[j])
                amt = max(amt, dfs(cur, j))
                cur.pop()
            return amt
        ans = 0
        for i in range(len(arr)):
            ans = max(ans, dfs([], i))
        return ans
        