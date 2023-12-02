class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        charCounter = Counter(chars)
        ans = sum(len(i) for i in words)
        for st in words : 
            strMap = Counter(st)

            for key in strMap.keys():
                if key not in charCounter or strMap[key] > charCounter[key]:
                    ans -= len(st)
                    break 
        
        return ans 
                

        