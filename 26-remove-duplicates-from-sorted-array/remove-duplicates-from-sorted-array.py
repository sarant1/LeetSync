class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        used = set()
        for i in range(len(nums)):
            if not nums[i] in used:
                nums[current] = nums[i]
                current+=1
                used.add(nums[i])
        for _ in range(current, len(nums)):
            nums.pop()
                

