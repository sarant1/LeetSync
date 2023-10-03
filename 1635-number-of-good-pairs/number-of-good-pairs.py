class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        found = defaultdict(int)
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            curr = nums[i]
            if curr in found:
                ans += found[curr]
                found[curr] += 1
            else:
                found[curr] = 1
        return ans


        