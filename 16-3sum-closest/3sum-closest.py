class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, diff = 0, float('inf') 
        for i in range(len(nums)):
            m=i+1
            e=len(nums)-1
            while m < e:
                cur_sum = nums[i] + nums[m] + nums[e]
                cur_diff = abs(target-cur_sum)
                if cur_diff < diff:
                    diff = cur_diff
                    ans = cur_sum 
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    m+=1
                else:
                    e-=1
        return ans








        