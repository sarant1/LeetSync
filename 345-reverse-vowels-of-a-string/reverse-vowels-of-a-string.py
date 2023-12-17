class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set({"a","A", "e", "E", "i", "I", "o", "O", "u", "U"})
        v = []
        for char in s:
            if char in vowels:
                v.append(char)
        s = list(s) 
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = v.pop()
        return "".join(s)
                  

        