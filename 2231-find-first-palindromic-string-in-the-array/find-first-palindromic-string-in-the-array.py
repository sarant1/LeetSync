class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(string):
            l, r = 0, len(string)-1
            while l < r:
                if string[l] != string[r]:
                    return False
                l+=1
                r-=1
            return True

        for chars in words:
            if is_palindrome(chars):
                return chars
        return ""
        