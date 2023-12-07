class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = list(s)

        for i, char in enumerate(ans):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        for i in range(len(stack)):
            ans[stack[i]] = ""
        
        return "".join(ans)

      
    
      







        