class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        used_freq = set() 
        res = 0
        # iterating through the dict with .items() { c:freq }
        for c, freq in count.items():
            while freq in used_freq:
                freq -= 1
                res += 1
            if freq != 0:
                used_freq.add(freq)
        return res

