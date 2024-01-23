class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtracking(cur, i):
            temp_str = "".join(cur)
            if len(set(temp_str)) != len(temp_str):
                return 0
            amt = len(temp_str)
            for j in range(i, len(arr)):
                cur.append(arr[j])
                amt = max(amt, backtracking(cur, j))
                cur.pop()
            return amt 
        ans = 0 
        for i in range(len(arr)):
            ans = max(ans, backtracking([], i))
        return ans
        