class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        prev, cur = "", 0
        count = set()
        for num in arr:
            if num == prev:
                cur+=1
            else:
                if cur in count:
                    return False
                count.add(cur)
                cur = 1
            prev = num
        if cur in count:
            return False
        return True



        