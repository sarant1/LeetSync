class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for i,r in roads:
            adj[i].append(r)
            adj[r].append(i)
        count = 0
        print(adj)
        for i in range(len(adj)-1):
            for j in range(i, len(adj)):
                if i == j:
                    continue
                curr_count = len(adj[i]) + len(adj[j])
                print(i, j, curr_count)
                if i in adj[j]:
                    curr_count -=1
                count = max(count, curr_count)
        return count
            


