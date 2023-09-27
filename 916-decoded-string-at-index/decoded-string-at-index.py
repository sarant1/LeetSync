class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0
        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i+=1
        print(length)
        for j in range(i-1, -1, -1):
            char = s[j]
            # if it is a digit we are going to divide the length by the amount
            if char.isdigit():
                length //= int(char)
                k %= length
                print("k: ", k)
            else:
                if k == 0 or k == length:
                    return char
                length -= 1
            
            
        





        