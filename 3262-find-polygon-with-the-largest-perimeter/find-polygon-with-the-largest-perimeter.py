class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        ans = -1 
        for i in range(len(nums)):
            if nums[i] < total:
                ans = nums[i] + total
            total+=nums[i]
        return ans

            


        