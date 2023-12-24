class Solution:
    def minOperations(self, s: str) -> int:
        # Two pass method
        pass1, pass2 = 0, 0
        zero = True
        for i in range(len(s)): 
            if (s[i] == "1" and zero) or (s[i] == "0" and not zero):
                pass1+=1
            zero = not zero
        zero = False
        for i in range(len(s)): 
            if (s[i] == "1" and zero) or (s[i] == "0" and not zero):
                pass2+=1
            zero = not zero
        return min(pass1, pass2)

        