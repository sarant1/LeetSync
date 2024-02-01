class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        for num in nums:
            if len(ans[-1]) == 3:
                ans.append([])
            if ans[-1] and num - ans[-1][0] > k:
                return []
            ans[-1].append(num)
        return ans


        