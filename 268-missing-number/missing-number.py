class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = [False] * (len(nums) + 1)
        for i in range(len(nums)):
            check[nums[i]] = True
        for i in range(len(check)):
            if not check[i]:
                return i
        return -1

        