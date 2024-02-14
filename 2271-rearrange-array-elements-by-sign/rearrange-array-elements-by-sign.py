class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        stack_pos = deque() 
        stack_neg = deque() 
        for num in nums:
            if num > 0:
                stack_pos.append(num)
            else:
                stack_neg.append(num)
        neg = False
        for i in range(len(nums)):
            if neg:
                nums[i] = stack_neg.popleft()
            elif not neg:
                nums[i] = stack_pos.popleft()
            neg = not neg
        return nums


        