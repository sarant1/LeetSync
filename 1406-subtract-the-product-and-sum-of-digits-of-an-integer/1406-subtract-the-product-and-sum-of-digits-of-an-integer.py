class Solution:
    def subtractProductAndSum(self, n: int) -> int:
      sum_ = 0 
      product = 1 
      for g in str(n):
        sum_+=int(g)
        product*=int(g)
      return product - sum_ 


        