class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        h = len(s)//2
        vowels = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
        v = 0
        for i in range(len(s)):
            if i >= h and s[i] in vowels:
                v-=1 
            elif s[i] in vowels:
                v+=1
        return v == 0

        