class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = 20001
        val=0
        for i in range(n):
            m=i+1
            e=n-1
            while(m<e):
                cur_sum = nums[i] + nums[m] + nums[e]
                cur_diff = abs(cur_sum - target)
                if (cur_diff < diff):
                    diff = cur_diff
                    val = cur_sum
                if cur_sum == target:
                    return target
                elif cur_sum < target:
                    m+=1
                else:
                    e-=1
        return val








        