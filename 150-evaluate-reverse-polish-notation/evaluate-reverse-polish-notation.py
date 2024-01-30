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
            if len(token) == 1 and ord(token) < 48:
                int1 = stack.pop()
                int2 = stack.pop()
                operator = token
                resolved_ans = resolve(int(int1), int(int2), operator)
                stack.append(resolved_ans)
            else:
                stack.append(int(token))
        return stack.pop()



             



        
                



        