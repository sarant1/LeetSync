class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        loc, cur, length = 0, 1, 0

        for g in range(n):
            if target[loc] == cur:
                ans.append("Push")
                length+=1
                loc+=1
            elif target[loc] > cur:
                ans.append("Push")
                ans.append("Pop")
            cur += 1
            if length == len(target):
                break
        return ans




        