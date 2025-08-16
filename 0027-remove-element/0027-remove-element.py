class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:  
        run = True
        break_point = 0
        
        while run:
            for i in range(break_point, len(nums)):
                if nums[i] == val:
                    nums.pop(i)
                    break_point = i
                    break
                elif i+1 == len(nums):
                    run = False
            if len(nums) == 0 or break_point == len(nums):
                run = False

        return len(nums)