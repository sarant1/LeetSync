class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, ans = 0, max(nums)
        if ans < 0:
            return ans
        for num in nums:
            cur += num
            if cur < 0:
                cur = 0
            ans = max(cur, ans)
        return ans

        