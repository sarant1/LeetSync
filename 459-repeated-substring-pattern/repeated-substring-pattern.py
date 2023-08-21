class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        count = 1 
        while count < len(s):
            if s[0:count] == s[count:count+count]:
                run = 0
                while run <= len(s):
                    currWord = s[run:run+count]
                    nextWord = s[run+count:run+count+count]
                    if currWord == nextWord:
                        if run+count+count == len(s):
                            return True
                    else:
                        break
                    run = run+count
            count += 1
        return False


