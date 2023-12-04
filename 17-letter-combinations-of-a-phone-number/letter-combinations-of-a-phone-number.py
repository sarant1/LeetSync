class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        matches = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"], 
            "5": ["j", "k", "l"], 
            "6": ["m", "n", "o"], 
            "7": ["p", "q", "r", "s"], 
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"] 
        }
        if not digits:
            return []
        ans = matches[digits[0]] 
        for i in range(1, len(digits)):
            forEach = len(ans)
            ans = list(ans * len(matches[digits[i]]))
            cur = 0
            for j in range(len(ans)):
                if j and j % forEach == 0:
                    cur += 1 
                ans[j] += matches[digits[i]][cur]
        return ans





                
            

            


                

            
        