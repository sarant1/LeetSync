class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        counter = set()
        for num in nums1:
            counter.add(num)
        for num in nums2:
            if num in counter:
                ans.append(num)
                counter.remove(num)
        return ans
        