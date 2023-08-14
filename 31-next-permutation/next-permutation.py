class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return 
        prev = nums[0] 
        dec_start = 0
        for n in range(len(nums)):
            if nums[n] > prev:
                dec_start = n
            prev = nums[n]
        if dec_start == len(nums)-1:
            temp = nums[-2]
            nums[-2] = nums[-1]
            nums[-1] = temp
        elif dec_start == 0:
            nums.reverse()
        else:
            min_swap = dec_start-1
            min_swap_index = min_swap
            for i in range(dec_start, len(nums)):
                if nums[i] > nums[min_swap]:
                    min_swap_index = i
            temp = nums[min_swap_index]
            nums[min_swap_index] = nums[dec_start-1]
            nums[dec_start-1] = temp
            
            start = dec_start
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1





            
        
        
        




            





            
                 





