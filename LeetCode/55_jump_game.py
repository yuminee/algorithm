from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) -1
        for i in range(last_index, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i

        return last_index == 0 

        