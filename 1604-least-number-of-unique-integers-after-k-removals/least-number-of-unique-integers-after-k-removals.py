class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = defaultdict(int)
        for num in arr:
            count[num]+=1
        sort_count = []
        for key, amt in count.items():
            sort_count.append(amt)
        sort_count.sort()
        x = 0
        while k >= 1:
            k-=sort_count[x]
            x+=1
        
        if k == 0:
            return len(sort_count) - x
        elif k < 0:
            return 1 + len(sort_count) - x

