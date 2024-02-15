class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        cur = 0
        sums = []
        for num in nums:
            cur+=num
            sums.append(cur)
        ans = -1 
        for i in range(len(nums)):
            if i >= 2 and nums[i] < sums[i-1]:
                ans = nums[i] + sums[i-1]
        return ans

            


        