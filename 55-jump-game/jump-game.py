class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 0
        for i in range(len(nums)):
            goal = max(goal, nums[i]+i) 
            if goal >= len(nums)-1:
                return True
            if not nums[i] and goal == i:
                break
        return False
        