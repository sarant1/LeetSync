class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(cur, i):
            temp_str = "".join(cur)
            if len(set(temp_str)) != len(temp_str):
                return 0
            amt = len(temp_str)
            for j in range(i, len(arr)):
                cur.append(arr[j])
                amt = max(amt, dfs(cur, j+1))
                cur.pop()
            return amt
        length = 0
        for i in range(len(arr)):
            length = max(length, dfs([], i))
        return length

        