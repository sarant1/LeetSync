class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c, r = 0, len(nums) - 1
        ans = len(nums)
        if len(nums) == 1:
            if nums[0] == val:
                nums[0] = -1
                return 0
            else:
                return 1
        while c < r:
            while r >= 0 and nums[r] == val:
                nums[r] = -1
                r-=1
                ans-=1
            if nums[c] == val:
                nums[c], nums[r] = nums[r], -1
                r -= 1
                ans-=1
            c+=1
        if len(nums) > 0 and nums[c] == val:
            nums[c] = -1
            ans-=1
        return ans
        