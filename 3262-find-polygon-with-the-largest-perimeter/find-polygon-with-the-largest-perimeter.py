class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        total = 0
        ans = -1 
        for i in range(len(nums)):
            if i >= 2 and nums[i] < total:
                ans = nums[i] + total
            total+=nums[i]
        return ans

            


        