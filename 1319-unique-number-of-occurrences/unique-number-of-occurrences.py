class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        totals = defaultdict(int) 
        for num in arr:
            totals[num]+=1
        counts = set()
        for key, amt in totals.items():
            if amt in counts:
                return False
            counts.add(amt)
        return True



        