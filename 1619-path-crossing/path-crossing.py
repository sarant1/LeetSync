class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = set({(0, 0)})
        cur = [0, 0]
        for d in path:
            if d == "N":
                cur[0]+=1
            elif d == "S":
                cur[0]-=1
            elif d == "W":
                cur[1]-=1
            elif d == "E":
                cur[1]+=1
            if (cur[0], cur[1]) in pos:
                return True
            pos.add((cur[0], cur[1]))
        return False



        