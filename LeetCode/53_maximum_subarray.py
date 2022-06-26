from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_v = nums[0]

        if len(nums) == 1:
            return curr

        for num in nums[1:]:
            curr = max(num, curr+ num)
            max_v = max(max_v, curr)

        return max_v
