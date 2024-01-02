class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = [0] * 201
        ans = []
        h = 0
        for i in range(len(nums)):
            counter[nums[i]]+=1
            if counter[nums[i]] > h:
                h = counter[nums[i]]
        for i in range(h):
            cur = []
            temp = set()
            for j in range(len(nums)):
                if counter[nums[j]] and nums[j] not in temp:
                    cur.append(nums[j])
                    counter[nums[j]]-=1
                    temp.add(nums[j])
            ans.append(list(cur))
        return ans

        
        