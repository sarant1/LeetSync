class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = ans = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], nums[i]+cur)
            ans = max(cur, ans)
        return ans

        