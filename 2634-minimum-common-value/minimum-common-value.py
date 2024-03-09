class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l, r = 0, 0
        while nums1[l] != nums2[r]:
            if nums1[l] > nums2[r]:
                r+=1
            else:
                l+=1
            if l == len(nums1) or r == len(nums2):
                return -1
        return nums1[l]
        
        




        