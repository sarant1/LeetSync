class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = []
        for n in nums:
            index = bisect.bisect_left(subseq, n)
            if index >= len(subseq):
                subseq.append(n)
            else:
                subseq[index] = n
        return len(subseq)
        
        