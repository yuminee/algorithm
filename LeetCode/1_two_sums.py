from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums):
            x = target - i
            if x in nums and nums.index(x) != idx:
                return [idx, nums.index(x)]