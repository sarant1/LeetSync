class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans.append(nums[i])
                nums[i] = -1
        
        for n in nums:
            if n != -1:
                ans.append(n)
        return ans



                

        