class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        prev = -101
        for i in range(len(nums)):
            if nums[i] != prev:
                nums[current] = nums[i]
                prev = nums[current]
                current+=1
        for _ in range(current, len(nums)):
            nums.pop()
                

