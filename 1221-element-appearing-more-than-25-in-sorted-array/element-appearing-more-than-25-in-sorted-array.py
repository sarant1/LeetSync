class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        goal = len(arr) // 4
        cur = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                cur+=1
            else:
                cur = 1
            if cur > goal:
                return arr[i]
        return arr[-1]
        


        