class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs = defaultdict(int) 
        for num in arr:
            occurs[num]+=1 
        count = set()
        for key, val in occurs.items():
            if val in count:
                return False
            count.add(val)
        return True



        