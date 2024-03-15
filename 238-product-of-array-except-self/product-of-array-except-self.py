class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1 
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes+=1
            else:
                product*=num
        if zeroes > 1:
            return [0] * len(nums)
        if zeroes == 1:
            for num in nums:
                if not num:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
            for num in nums:
                ans.append(product//num)
        return ans

        