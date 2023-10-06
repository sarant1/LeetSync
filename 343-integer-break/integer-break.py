class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2


        count_of_trees, remainder = divmod(n, 3)


        if remainder == 0:
            return 3 ** count_of_trees
        if remainder == 1:
            return 3 ** (count_of_trees - 1) * 4 
        else:
            return 3 ** count_of_trees * 2

        