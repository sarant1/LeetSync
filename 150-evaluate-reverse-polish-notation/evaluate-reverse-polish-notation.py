class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def resolve(int1, int2, oper):
            if oper == "+":
                return int2+int1
            if oper == "-":
                return int2-int1
            if oper == "/":
                return int(int2/int1)
            return int1*int2
        stack = []
        for token in tokens:
            if token == "+" or token == "/" or token == "-" or token == "*":
                stack.append(resolve(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))
        return stack.pop()



             



        
                



        