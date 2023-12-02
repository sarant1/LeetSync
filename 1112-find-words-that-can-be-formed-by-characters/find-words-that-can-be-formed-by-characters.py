class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        hmap = defaultdict(int) 
        for c in chars:
            hmap[c]+=1 
        
        for word in words:
            temp = defaultdict(int, hmap)
            isValid = True
            for c in word:
                if temp[c] < 1:
                    isValid=False
                    break
                else:
                    temp[c]-=1
            if isValid:
                ans+=len(word)
            else:
                print(temp)
                print(word)
        return ans

                

        