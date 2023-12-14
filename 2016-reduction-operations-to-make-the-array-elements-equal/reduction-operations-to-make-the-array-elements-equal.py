class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                ans += n - i - 1
        return ans





           