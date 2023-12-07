class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
      stack = []
      s = list(s)

      for i, char in enumerate(s):
          if char == "(":
              stack.append(i)
          elif char == ")":
            if stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)
      while stack:
          s[stack.pop()] = ""
      return "".join(s)
      

      
    
      







        