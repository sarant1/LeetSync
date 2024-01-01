class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        arr = deque(nums)
        cur_total = 0
        s = sum(nums)
        for i in range(len(nums)):
            cur_total += (nums[i] * i)
        ans = cur_total
        for i in range(1, len(nums)):
            cur_total += s-len(nums)*nums[len(nums)-i] 
            ans = max(cur_total, ans)
        return ans if ans != float("-inf") else 0
        