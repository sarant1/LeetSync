class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = []
        zero = 0
        zeroloc = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product = nums[i] * product
            else:
                zeroloc = i
                zero+=1
        if zero > 1:
            return [0] * len(nums)
        elif zero == 1:
            ans = [0] * len(nums)
            ans[zeroloc] = product
            return ans

        for n in nums:
            curr = product//n
            ans.append(curr)
        return ans
        