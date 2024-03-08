class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        arr = []
        for key, val in counter.items():
            arr.append(val)
        m = max(arr) 
        return m * arr.count(m)


        