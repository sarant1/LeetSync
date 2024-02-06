class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        ans = []
        pos = 0
        for string in strs:
            s = sorted(string)
            s = "".join(s)
            if s in cache:
                ans[cache[s]].append(string) 
            else:
                cache[s] = pos
                ans.append([string])
                pos+=1
        return ans
        