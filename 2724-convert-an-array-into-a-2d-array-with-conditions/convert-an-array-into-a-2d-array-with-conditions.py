class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = [0] * 201
        h = 0
        ans = []
        for i in range(len(nums)):
            counter[nums[i]]+=1
            if counter[nums[i]] > h:
                h = counter[nums[i]]
        for i in range(h):
            cur = []
            for j in range(len(counter)):
                if counter[j]:
                    cur.append(j)
                    counter[j]-=1
            ans.append(cur)
        return ans

        
        