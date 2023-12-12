class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, goal, dis = 0, 0, 0
        for i in range(len(nums)-1):
            dis = max(dis, nums[i]+i)
            if dis >= len(nums)-1:
                ans+=1 
                break
            if i == goal:
                ans+=1 
                goal = dis
        return ans

            
        