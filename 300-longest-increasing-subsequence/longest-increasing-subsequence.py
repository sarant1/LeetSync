class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = []
        for num in nums:
            i = bisect.bisect_left(subseq, num)
            if i >= len(subseq):
                subseq.append(num)
            else:
                subseq[i] = num
        return len(subseq)
        