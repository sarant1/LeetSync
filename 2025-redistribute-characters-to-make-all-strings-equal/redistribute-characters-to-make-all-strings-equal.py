class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = [0] * 26
        for word in words:
            for char in word:
                counter[ord(char)-ord("a")]+=1
        for total in counter:
            if total % len(words):
                return False
        return True

        

        