class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, prev = 0, 0
        for row in bank:
            cur = row.count("1")
            ans += (cur * prev)
            if cur:
                prev = cur
        return ans

        