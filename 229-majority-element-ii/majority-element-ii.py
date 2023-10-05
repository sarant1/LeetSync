class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        toPush = len(nums)/3
        tallys = defaultdict(int) 

        for n in nums:
            tallys[n] += 1
            if tallys[n] > toPush:
                tallys[n] = float("-inf")
                ans.append(n)
        return ans

            



        