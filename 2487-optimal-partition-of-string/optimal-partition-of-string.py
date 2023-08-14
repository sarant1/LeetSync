class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        hash_set = set()
        for i in range(len(s)):
            if s[i] in hash_set:
                count +=1 
                hash_set.clear()
                hash_set.add(s[i])
            else:
                hash_set.add(s[i])
        return count
                

