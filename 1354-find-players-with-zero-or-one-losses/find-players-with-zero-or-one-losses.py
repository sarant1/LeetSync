class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        results = {}
        for win, lose in matches:
            if win not in results:
                results[win] = [1, 0]
            else:
                results[win][0]+=1
            if lose not in results:
                results[lose] = [0, 1]
            else:
                results[lose][1]+=1
        for player, res in results.items():
            if res[1] == 0:
                ans[0].append(player)
            if res[1] == 1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
        return ans
        