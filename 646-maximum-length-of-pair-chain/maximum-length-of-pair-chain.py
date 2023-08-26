class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr, ans = float('-inf'), 0

        for pair in pairs:
            if curr < pair[0]:
                curr = pair[1]
                ans += 1
        return ans


