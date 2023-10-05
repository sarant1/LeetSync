class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        curr = 1
        toPush = len(nums)/3
        if toPush < 1:
            return list(set(nums))
        ans = []
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                curr = 1 
            else:
                curr += 1
            if curr > toPush:
                ans.append(nums[i])
                curr = float("-inf")
        return ans
            
            
            










            



        