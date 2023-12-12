class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hi, sec = -1, -1
        for num in nums:
            if num >= hi:
                sec = hi
                hi = max(hi, num)
            else:
                sec = max(sec, num)
        sec-=1
        hi-=1
        return hi*sec
        