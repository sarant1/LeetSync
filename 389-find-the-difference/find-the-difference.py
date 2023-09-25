class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hmap = defaultdict(int) 

        for l in s:
            hmap[l] += 1
        for g in t:
            hmap[g] -= 1
            if hmap[g] < 0:
                return g   
        