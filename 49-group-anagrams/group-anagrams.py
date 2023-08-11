class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp in hashmap:
                ans[hashmap[temp]].append(word)
            else:
                hashmap[temp] = len(ans)
                ans.append([word])
        return ans
                