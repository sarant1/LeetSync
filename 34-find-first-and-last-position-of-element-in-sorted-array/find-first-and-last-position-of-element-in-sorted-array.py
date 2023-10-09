class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1 
        mid = (len(nums))//2
        while l <= r:
            if nums[mid] == target:
                l, r = mid, mid
                while l > 0 and nums[l-1] == target:
                    l -= 1
                while r < len(nums) - 1 and nums[r+1] == target:
                    r += 1
                return [l, r] 
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            mid = (r - l) // 2 + l
        return [-1, -1]






        