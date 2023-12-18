class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        hi1, hi2, lo1, lo2 = float("-inf"),float("-inf"), float("inf"), float("inf") 
        for num in nums:
            if num > hi1 and num > hi2:
                hi2 = hi1
                hi1 = num
            elif num > hi2:
                hi2 = num
            if num < lo2 and num < lo1:
                lo2 = lo1  
                lo1 = num
            elif num < lo2:
                lo2 = num
        return (hi1*hi2) - (lo1*lo2)


        
