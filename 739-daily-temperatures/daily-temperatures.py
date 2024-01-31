class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            while stack and stack[-1][-1] < temperatures[i]:
                pos, temp = stack.pop()
                ans[pos] = i - pos
            stack.append((i, temperatures[i]))
        return ans



        