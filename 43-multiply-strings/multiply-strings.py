class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        vals = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        one, cur = 0, 1 
        for char in reversed(num1):
            one+=(vals[char] * cur)
            cur*=10
        two, cur = 0, 1
        for char in reversed(num2):
            two+=(vals[char] * cur)
            cur*=10
        return str(one * two)


        

        