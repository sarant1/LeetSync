class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        temp = defaultdict(int, chars)
        #Add all lengths of words 
        idx = 0 
        pointer = 0 
        ans = 0 
        #Working on basis of two pointers 
        while pointer < len(words):
            if idx == len(words[pointer]):
                ans += len(words[pointer])
                idx , pointer = 0 , pointer + 1 
                temp = defaultdict(int, chars)
                continue
            c = words[pointer][idx]
            if temp[c] < 1:
                idx , pointer = 0 , pointer + 1 
                temp = defaultdict(int, chars)
                continue
            idx += 1   
            temp[c]-=1
        return ans 
                

        