class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = defaultdict(int) 
        for word in words:
            for char in word:
                counter[char]+=1
        for i, total in counter.items():
            if total % len(words):
                return False
        return True

        

        