class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = n*(n+1) // 2
        missingNum = total - sum(set(nums))
        position = sum(nums) - (total - missingNum)
        return [position, missingNum]
        