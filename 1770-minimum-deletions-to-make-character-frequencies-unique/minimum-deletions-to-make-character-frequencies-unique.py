class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = {}
        arr = [0] * 26
        count = 0
        for l in s:
            arr[ord(l)-ord('a')]+=1
        for i, amt in enumerate(arr):
            if amt == 0:
                continue
            if amt in hmap:
                temp = amt
                while temp in hmap:
                    count += 1
                    temp -= 1
                    if temp == 0:
                        break
                hmap[temp] = i
            else:
                hmap[amt] = i
        return count

            


        