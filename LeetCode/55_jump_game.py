from typing import List

class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums)

        for num in nums:
            position = num