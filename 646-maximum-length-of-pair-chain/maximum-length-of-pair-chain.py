class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        print(pairs)
        total,curr = 1,0
        for i in range(1, len(pairs)):
            if pairs[curr][1] < pairs[i][0]:
                curr = i
                total += 1
        return total





